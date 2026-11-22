#!/usr/bin/env python3
"""Render the pinned Guacamole menu UI in QEMU with all board I/O mocked.

This is a renderer preview only: it does not boot the actual shim, model ABL,
PMIC/touch/UFS, dispatch a payload, or test a physical device.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import struct
import subprocess
import tempfile
import time
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ports/guacamole-ios27/repo"
EXPECTED = "396a851ef112fd34003f0b37c3270bcd6c2e8cc2"
WIDTH, HEIGHT, STRIDE = 1440, 3120, 1440 * 4
FB_BASE = 0x9C000000


def run(args: list[str], *, cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def qmp_call(f, execute: str, arguments: dict | None = None):
    f.write(json.dumps({"execute": execute, "arguments": arguments or {}}) + "\n")
    f.flush()
    while True:
        response = json.loads(f.readline())
        if "error" in response:
            raise RuntimeError(f"QMP {execute}: {response['error']}")
        if "return" in response:
            return response["return"]


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return (struct.pack(">I", len(data)) + kind + data +
            struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF))


def framebuffer_png(raw_path: Path, output: Path) -> None:
    raw = raw_path.read_bytes()
    expected_size = WIDTH * HEIGHT * 4
    if len(raw) != expected_size:
        raise RuntimeError(f"QEMU framebuffer has {len(raw)} bytes, expected {expected_size}")
    rows = bytearray()
    for y in range(HEIGHT):
        bgra = raw[y * STRIDE:(y + 1) * STRIDE]
        rgb = bytearray(WIDTH * 3)
        rgb[0::3] = bgra[2::4]
        rgb[1::3] = bgra[1::4]
        rgb[2::3] = bgra[0::4]
        rows.append(0)  # PNG filter: None
        rows.extend(rgb)
    image = (b"\x89PNG\r\n\x1a\n" +
             png_chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)) +
             png_chunk(b"IDAT", zlib.compress(bytes(rows), 6)) +
             png_chunk(b"IEND", b""))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(image)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=ROOT / "docs/screenshots/guacamole-menu-qemu.png")
    parser.add_argument("--settle-seconds", type=float, default=5.0)
    args = parser.parse_args()

    if not (SOURCE / ".git").exists():
        parser.error(f"source submodule is not initialized: {SOURCE}")
    actual = subprocess.check_output(["git", "-C", str(SOURCE), "rev-parse", "HEAD"], text=True).strip()
    if actual != EXPECTED:
        parser.error(f"expected ios-guacamole {EXPECTED}, found {actual}")
    clang = shutil.which("clang")
    qemu = shutil.which("qemu-system-aarch64")
    if not clang or not qemu:
        parser.error("requires clang and qemu-system-aarch64 on PATH")

    shim = SOURCE / "shim"
    original = (shim / "menu.c").read_text()
    start = "/* ---- time ---- */"
    end = "/* ---- drawing ---- */"
    if original.count(start) != 1 or original.count(end) != 1:
        parser.error("upstream menu.c structure changed; review the test-only input/timer patch")
    before, tail = original.split(start, 1)
    _, after = tail.split(end, 1)
    mocked_backend = r'''/* QEMU preview fixture: the board-specific PMIC/timer backend is not run. */
static uint64_t preview_tick;
static uint64_t now(void) { return preview_tick++; }
static uint64_t ms_ticks(unsigned ms) { return ms; }
static int apid_pon = -1, apid_vup = -1, apid_vdn = -1;
static void keys_init(void) {}
#define KEY_POWER 1u
#define KEY_UP 2u
#define KEY_DOWN 4u
static unsigned keys_now(void) { return 0; }

'''

    with tempfile.TemporaryDirectory(prefix="portsmith-guacamole-menu-") as td:
        tmp = Path(td)
        (tmp / "menu_qemu.c").write_text(before + mocked_backend + end + after)
        (tmp / "main.c").write_text(r'''#include <stdint.h>
#include "console.h"
#include "menu.h"
volatile uint32_t *con_fb;
int con_quiet;
void con_clear(uint32_t bg) { (void)bg; }
void con_skip(void) {}
void con_str(const char *label, const char *s) { (void)label; (void)s; }
void con_hex(const char *label, uint64_t v) { (void)label; (void)v; }
void con_hex2(const char *label, const char *a, uint32_t va, const char *b, uint32_t vb) {
    (void)label; (void)a; (void)va; (void)b; (void)vb;
}
int touch_begin(void) { return -1; }
int touch_poll(int *x, int *y) { (void)x; (void)y; return -1; }
void touch_end(void) {}
void *memcpy(void *dst, const void *src, unsigned long n) {
    unsigned char *d = dst; const unsigned char *s = src;
    for (unsigned long i = 0; i < n; i++) d[i] = s[i];
    return dst;
}
int preview_main(void) {
    con_fb = (volatile uint32_t *)FB_BASE;
    struct menu_entry entries[5] = {
        {"iOS 27", "iPhone 14 Pro, partition ios27", 1, menu_icon_ios27, 0},
        {"macOS 27", "not installed yet", 0, menu_icon_macos27, 0},
        {"Android", "boot_a", 1, menu_icon_android, 0},
        {"Restart", "", 1, 0, 1},
        {"Power off", "", 1, 0, 1},
    };
    (void)menu_choose(entries, 5, 0, 0);
    for (;;) __asm__ volatile("wfe");
}
''')
        (tmp / "start.S").write_text(r'''.section .text.boot,"ax"
.global _start
.type _start,%function
_start:
    msr daifset, #0xf
    msr spsel, #1
    ldr x0, =_stack_top
    mov sp, x0
    bl preview_main
1:  wfe
    b 1b
.section .bss.stack,"aw",%nobits
.balign 16
_stack_bottom:
    .skip 65536
_stack_top:
''')
        linker = tmp / "link.ld"
        linker.write_text("ENTRY(_start)\nSECTIONS { . = 0x40200000; .text : { KEEP(*(.text.boot)) *(.text*) } .rodata : { *(.rodata*) *(.menuart) } .data : { *(.data*) } .bss (NOLOAD) : { *(.bss*) *(COMMON) } }\n")
        common = [clang, "--target=aarch64-none-elf", "-mcpu=cortex-a76", "-O2", "-ffreestanding",
                  "-fno-builtin", "-fno-pic", "-fno-stack-protector", "-mgeneral-regs-only",
                  "-mstrict-align", "-DBOARD_GUACAMOLE", "-I", str(shim)]
        run(common + ["-c", str(tmp / "menu_qemu.c"), "-o", str(tmp / "menu.o")])
        run(common + ["-c", str(tmp / "main.c"), "-o", str(tmp / "main.o")])
        run(common + ["-c", str(tmp / "start.S"), "-o", str(tmp / "start.o")])
        run(common + ["-c", "art.S", "-o", str(tmp / "art.o")], cwd=shim)
        elf = tmp / "menu.elf"
        run([clang, "--target=aarch64-none-elf", "-mcpu=cortex-a76", "-nostdlib", "-fuse-ld=lld",
             f"-Wl,-T,{linker}", "-Wl,--build-id=none", str(tmp / "start.o"), str(tmp / "main.o"),
             str(tmp / "menu.o"), str(tmp / "art.o"), "-o", str(elf)])

        qmp_path = tmp / "qmp.sock"
        raw_path = tmp / "framebuffer.raw"
        command = [qemu, "-machine", "virt", "-cpu", "cortex-a76", "-m", "2G", "-display", "none",
                   "-serial", "null", "-monitor", "none", "-S", "-qmp",
                   f"unix:{qmp_path},server=on,wait=off", "-device", f"loader,file={elf},cpu-num=0"]
        proc = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        try:
            for _ in range(100):
                if qmp_path.exists():
                    break
                if proc.poll() is not None:
                    raise RuntimeError(f"QEMU exited: {proc.stderr.read()}")
                time.sleep(0.1)
            else:
                raise RuntimeError("QEMU QMP socket did not appear")
            sock = socket.socket(socket.AF_UNIX)
            sock.connect(str(qmp_path))
            stream = sock.makefile("rw")
            json.loads(stream.readline())  # greeting
            qmp_call(stream, "qmp_capabilities")
            qmp_call(stream, "cont")
            time.sleep(max(0.2, args.settle_seconds))
            qmp_call(stream, "pmemsave", {"val": FB_BASE, "size": STRIDE * HEIGHT,
                                           "filename": str(raw_path)})
            qmp_call(stream, "quit")
            sock.close()
        finally:
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.terminate()
                proc.wait(timeout=5)
        framebuffer_png(raw_path, args.output)
    print(f"Wrote renderer-only QEMU framebuffer preview: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
