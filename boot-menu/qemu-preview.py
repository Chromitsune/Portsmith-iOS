#!/usr/bin/env python3
"""Render a boot-menu data profile in a tiny ARM64 QEMU guest (mock UI only)."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import socket
import struct
import subprocess
import tempfile
import time
import zlib
from pathlib import Path

from engine import MenuController, load_profile

ROOT = Path(__file__).resolve().parent
WIDTH, HEIGHT = 1440, 3120
FB_BASE = 0x9C000000
LAYOUT = {"vertical-icon-stack": 0, "vertical-text-list": 1, "responsive-card-grid": 2}
COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")


def cstr(s: str) -> str:
    return json.dumps(s, ensure_ascii=True)


def ccolor(s: str) -> str:
    if not COLOR.fullmatch(s):
        raise ValueError(f"invalid color {s!r}")
    return "0x00" + s[1:]


def icon_token(entry) -> tuple[str, str, str]:
    ident = entry.icon_id or ""
    if ident.startswith("ios-") and ident[4:].isdigit():
        label = ident[4:]
        svg = ROOT / "icons" / f"{ident}.svg"
        colors = re.findall(r'stop-color="(#[0-9a-fA-F]{6})"', svg.read_text()) if svg.is_file() else []
        if len(colors) >= 2:
            return label, colors[0], colors[1]
        return label, "#366b9f", "#7960cd"
    if ident.startswith("android"):
        return "A", "#3d8654", "#68bf68"
    if ident.startswith("recovery"):
        return "R", "#606773", "#333842"
    return entry.label[:1].upper(), "#596170", "#343a46"


def make_scene_header(profile, controller, width: int, height: int) -> str:
    look = profile.look
    layout = LAYOUT[look["layout"]]
    p = look["palette"]
    lines = [
        "#pragma once", "#include <stdint.h>",
        f"#define SCENE_WIDTH {width}", f"#define SCENE_HEIGHT {height}",
        f"#define SCENE_LAYOUT {layout}", f"#define SCENE_COUNT {len(profile.entries)}",
        f"#define SCENE_SELECTED {controller.selected_index}",
        f"#define SCENE_BG {ccolor(look['background'])}",
        f"#define SCENE_SURFACE {ccolor(p['surface'])}",
        f"#define SCENE_SELECTION {ccolor(p['selection'])}",
        f"#define SCENE_TEXT {ccolor(p['text'])}",
        f"#define SCENE_SECONDARY {ccolor(p['secondary_text'])}",
        f"#define SCENE_DISABLED {ccolor(p['disabled'])}",
        f"#define SCENE_TITLE {cstr(profile.title)}",
        "struct preview_entry { const char *label; const char *detail; const char *icon_text; uint32_t icon_start; uint32_t icon_end; int enabled; };",
        "static const struct preview_entry scene_entries[SCENE_COUNT] = {",
    ]
    for entry in profile.entries:
        icon_text, start, end = icon_token(entry)
        lines.append(f"  {{{cstr(entry.label)}, {cstr(entry.detail)}, {cstr(icon_text)}, {ccolor(start)}, {ccolor(end)}, {1 if entry.enabled else 0}}},")
    lines.extend(["};", ""])
    return "\n".join(lines)


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)


def framebuffer_png(raw_path: Path, output: Path, width: int, height: int) -> None:
    raw = raw_path.read_bytes()
    stride = width * 4
    if len(raw) != stride * height:
        raise RuntimeError(f"QEMU framebuffer length {len(raw)} != {stride*height}")
    rows = bytearray()
    for y in range(height):
        bgra = raw[y*stride:(y+1)*stride]
        rgb = bytearray(width*3)
        rgb[0::3], rgb[1::3], rgb[2::3] = bgra[2::4], bgra[1::4], bgra[0::4]
        rows.append(0)
        rows.extend(rgb)
    image = (b"\x89PNG\r\n\x1a\n" +
             png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)) +
             png_chunk(b"IDAT", zlib.compress(bytes(rows), 6)) + png_chunk(b"IEND", b""))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(image)


def qmp_call(stream, command: str, arguments: dict | None = None):
    stream.write(json.dumps({"execute": command, "arguments": arguments or {}}) + "\n")
    stream.flush()
    while True:
        response = json.loads(stream.readline())
        if "error" in response:
            raise RuntimeError(f"QMP {command}: {response['error']}")
        if "return" in response:
            return response["return"]


def compile_and_capture(profile_path: Path, output: Path, width: int, height: int, settle: float) -> None:
    clang, qemu = shutil.which("clang"), shutil.which("qemu-system-aarch64")
    if not clang or not qemu:
        raise RuntimeError("QEMU preview requires clang and qemu-system-aarch64 on PATH")
    profile = load_profile(profile_path)
    controller = MenuController(profile)
    with tempfile.TemporaryDirectory(prefix="portsmith-menu-qemu-") as td:
        tmp = Path(td)
        (tmp / "scene.h").write_text(make_scene_header(profile, controller, width, height))
        renderer = ROOT / "qemu" / "renderer.c"
        start = ROOT / "qemu" / "start.S"
        linker = ROOT / "qemu" / "link.ld"
        common = [clang, "--target=aarch64-none-elf", "-mcpu=cortex-a76", "-O2", "-ffreestanding", "-fno-builtin", "-fno-pic", "-fno-stack-protector", "-mgeneral-regs-only", "-mstrict-align", "-I", str(tmp)]
        subprocess.run(common + ["-c", str(renderer), "-o", str(tmp / "renderer.o")], check=True)
        subprocess.run(common + ["-c", str(start), "-o", str(tmp / "start.o")], check=True)
        elf = tmp / "preview.elf"
        subprocess.run([clang, "--target=aarch64-none-elf", "-mcpu=cortex-a76", "-nostdlib", "-fuse-ld=lld", f"-Wl,-T,{linker}", "-Wl,--build-id=none", str(tmp / "start.o"), str(tmp / "renderer.o"), "-o", str(elf)], check=True)
        qmp = tmp / "qmp.sock"
        raw = tmp / "framebuffer.raw"
        cmd = [qemu, "-machine", "virt", "-cpu", "cortex-a76", "-m", "2G", "-display", "none", "-serial", "null", "-monitor", "none", "-S", "-qmp", f"unix:{qmp},server=on,wait=off", "-device", f"loader,file={elf},cpu-num=0"]
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        try:
            for _ in range(100):
                if qmp.exists(): break
                if proc.poll() is not None: raise RuntimeError(f"QEMU exited: {proc.stderr.read()}")
                time.sleep(.1)
            else: raise RuntimeError("QEMU QMP socket did not appear")
            sock = socket.socket(socket.AF_UNIX); sock.connect(str(qmp)); stream = sock.makefile("rw")
            json.loads(stream.readline())
            qmp_call(stream, "qmp_capabilities")
            qmp_call(stream, "cont")
            time.sleep(max(.2, settle))
            qmp_call(stream, "pmemsave", {"val": FB_BASE, "size": width*height*4, "filename": str(raw)})
            qmp_call(stream, "quit")
            sock.close()
        finally:
            try: proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.terminate(); proc.wait(timeout=5)
        framebuffer_png(raw, output, width, height)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path, help="profile JSON under boot-menu/profiles")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--settle-seconds", type=float, default=1.0)
    args=parser.parse_args()
    try:
        profile=load_profile(args.profile)
        width=args.width or (1920 if profile.look["layout"]=="responsive-card-grid" else 1440)
        height=args.height or (1080 if profile.look["layout"]=="responsive-card-grid" else 3120)
        if width < 320 or height < 240:
            raise ValueError("canvas must be at least 320x240")
        output=args.output or Path("docs/screenshots")/f"boot-menu-{profile.look['look_id']}-qemu.png"
        compile_and_capture(args.profile,output,width,height,args.settle_seconds)
    except (OSError,ValueError,RuntimeError,subprocess.CalledProcessError) as exc:
        parser.error(str(exc))
    print(f"Wrote QEMU render-only fixture: {output}; no boot target was executed")
    return 0

if __name__=="__main__": raise SystemExit(main())
