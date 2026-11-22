#!/usr/bin/env python3
"""Interactive host-only terminal menu; returns an opaque target ID and never boots it."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from engine import MenuController, load_profile

EVENTS = {"up", "down", "left", "right", "select", "cancel"}


def run_events(controller: MenuController, events: list[str]) -> str | None:
    """Apply scripted host events for tests/demos; never dispatch target actions."""
    for event in events:
        result = controller.handle(event)
        if event in {"select", "confirm"}:
            return result
        if event in {"cancel", "back"}:
            return None
    return None


def _curses_menu(stdscr, profile, controller):
    import curses
    curses.curs_set(0)
    stdscr.keypad(True)
    if hasattr(curses, "set_escdelay"):
        curses.set_escdelay(250)
    while True:
        stdscr.erase()
        h, w = stdscr.getmaxyx()
        title = profile.title[:max(0, w-2)]
        stdscr.addstr(1, max(0, (w-len(title))//2), title, curses.A_BOLD)
        row = 4
        for entry in profile.entries:
            marker = ">" if entry.id == controller.selected.id else " "
            text = f"{marker} {entry.label} — {entry.detail}"
            attr = curses.A_REVERSE if entry.id == controller.selected.id else curses.A_NORMAL
            if not entry.enabled:
                attr |= curses.A_DIM
            if row < h-3:
                stdscr.addnstr(row, 2, text, max(0,w-4), attr)
            row += 2
        prompt = "↑/↓ or j/k move · Enter select · q cancel (selection only; no boot action)"
        if h > 1:
            stdscr.addnstr(h-2, 1, prompt, max(0,w-2), curses.A_DIM)
        stdscr.refresh()
        key = stdscr.getch()
        if key in (curses.KEY_UP, ord('k')):
            controller.handle("up")
        elif key in (curses.KEY_DOWN, ord('j')):
            controller.handle("down")
        elif key in (curses.KEY_LEFT,):
            controller.handle("left")
        elif key in (curses.KEY_RIGHT,):
            controller.handle("right")
        elif key in (curses.KEY_ENTER, 10, 13):
            return controller.activate()
        elif key in (ord('q'), 27):
            return None


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", nargs="?", type=Path,
                        default=Path(__file__).parent/"profiles/ios-dualboot-icon-stack.json")
    parser.add_argument("--start-entry")
    parser.add_argument("--events", help="comma-separated host events (up,down,select,cancel); no terminal UI")
    args=parser.parse_args()
    try:
        profile=load_profile(args.profile)
        controller=MenuController(profile,args.start_entry)
        if args.events is not None:
            events=[event.strip().lower() for event in args.events.split(",") if event.strip()]
            unknown=set(events)-EVENTS
            if unknown: parser.error(f"unknown host event(s): {', '.join(sorted(unknown))}")
            selected=run_events(controller,events)
        else:
            if not sys.stdin.isatty(): parser.error("interactive mode needs a TTY; use --events for scripted host input")
            import curses
            selected=curses.wrapper(_curses_menu,profile,controller)
    except (OSError,ValueError) as exc:
        parser.error(str(exc))
    if selected is None:
        print("No target selected; no boot action was executed.")
        return 1
    print(f"Selected opaque target ID: {selected}")
    print("No boot action was executed.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
