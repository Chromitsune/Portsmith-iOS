#!/usr/bin/env python3
"""Render a portable boot-menu profile as a self-contained SVG; no device I/O."""
from __future__ import annotations

import argparse
import base64
import html
from pathlib import Path
import sys

from engine import ROOT, MenuController, load_profile


def render_svg(profile, controller, width: int, height: int) -> str:
    look = profile.look
    palette = look["palette"]
    bg = look["background"]
    entries = profile.entries
    layout = look["layout"]
    margin = float(look["geometry"].get("safe_margin_fraction", 0.06)) * min(width, height)
    selected = controller.selected_index
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             f'<rect width="100%" height="100%" fill="{bg}"/>',
             f'<text x="{width/2:.1f}" y="{margin*1.1:.1f}" text-anchor="middle" fill="{palette["text"]}" font-family="sans-serif" font-size="{max(22,int(min(width,height)*0.035))}">{html.escape(profile.title)}</text>']
    if layout == "vertical-icon-stack":
        size = min(width * 0.52, height * 0.185)
        gap = min(width, height) * float(look["geometry"].get("row_gap_fraction", 0.035))
        block = len(entries) * size + max(0, len(entries)-1) * gap
        y = max(margin * 1.6, (height - block) / 2)
        for i, entry in enumerate(entries):
            x = (width-size)/2; cy = y + i*(size+gap)
            color = palette["surface"] if entry.enabled else palette["disabled"]
            opacity = 1.0 if entry.enabled else 0.36
            if i == selected:
                parts.append(f'<rect x="{x-12:.1f}" y="{cy-12:.1f}" width="{size+24:.1f}" height="{size+24:.1f}" rx="{size*.24:.1f}" fill="none" stroke="{palette["selection"]}" stroke-width="12"/>')
            parts.append(f'<rect x="{x:.1f}" y="{cy:.1f}" width="{size:.1f}" height="{size:.1f}" rx="{size*.22:.1f}" fill="{color}" opacity="{opacity}"/>')
            icon_path = ROOT / "icons" / f"{entry.icon_id}.svg" if entry.icon_id else None
            if icon_path and icon_path.is_file():
                data = base64.b64encode(icon_path.read_bytes()).decode("ascii")
                parts.append(f'<image x="{x+size*.16:.1f}" y="{cy+size*.10:.1f}" width="{size*.68:.1f}" height="{size*.68:.1f}" href="data:image/svg+xml;base64,{data}" opacity="{opacity}"/>')
            else:
                letter = html.escape(entry.label[:1].upper())
                parts.append(f'<circle cx="{width/2:.1f}" cy="{cy+size*.43:.1f}" r="{size*.18:.1f}" fill="{palette["selection"] if entry.enabled else palette["secondary_text"]}" opacity="{opacity}"/>')
                parts.append(f'<text x="{width/2:.1f}" y="{cy+size*.49:.1f}" text-anchor="middle" fill="{palette["text"]}" font-family="sans-serif" font-size="{size*.16:.1f}" opacity="{opacity}">{letter}</text>')
            parts.append(f'<text x="{width/2:.1f}" y="{cy+size*.86:.1f}" text-anchor="middle" fill="{palette["text"]}" font-family="sans-serif" font-size="{size*.07:.1f}" opacity="{opacity}">{html.escape(entry.label)}</text>')
    elif layout == "vertical-text-list":
        row_h = min(height*0.15, width*0.17)
        gap = height*0.025
        total = len(entries)*row_h + max(0,len(entries)-1)*gap
        y0 = max(margin*1.7,(height-total)/2)
        x, row_w = width*0.12, width*0.76
        for i, entry in enumerate(entries):
            y = y0+i*(row_h+gap); opacity=1 if entry.enabled else .38
            if i == selected:
                parts.append(f'<rect x="{x-8:.1f}" y="{y-8:.1f}" width="{row_w+16:.1f}" height="{row_h+16:.1f}" rx="18" fill="none" stroke="{palette["selection"]}" stroke-width="6"/>')
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{row_w:.1f}" height="{row_h:.1f}" rx="14" fill="{palette["surface"]}" opacity="{opacity}"/>')
            parts.append(f'<text x="{x+row_h*.2:.1f}" y="{y+row_h*.52:.1f}" fill="{palette["text"]}" font-family="sans-serif" font-size="{row_h*.24:.1f}" opacity="{opacity}">{html.escape(entry.label)}</text>')
            parts.append(f'<text x="{x+row_h*.2:.1f}" y="{y+row_h*.78:.1f}" fill="{palette["secondary_text"]}" font-family="sans-serif" font-size="{row_h*.12:.1f}" opacity="{opacity}">{html.escape(entry.detail)}</text>')
    else:  # responsive-card-grid
        cols = 2 if width/height < 1.15 else 3
        if width/height < 0.65: cols=1
        gap=min(width,height)*float(look["geometry"].get("column_gap_fraction",0.035))
        rows=(len(entries)+cols-1)//cols
        card_w=(width-2*margin-(cols-1)*gap)/cols
        card_h=min(height*0.19,card_w*.72)
        total=rows*card_h+(rows-1)*gap
        y0=max(margin*1.7,(height-total)/2)
        for i,entry in enumerate(entries):
            row,col=divmod(i,cols);x=margin+col*(card_w+gap);y=y0+row*(card_h+gap);opacity=1 if entry.enabled else .38
            if i==selected:
                parts.append(f'<rect x="{x-9:.1f}" y="{y-9:.1f}" width="{card_w+18:.1f}" height="{card_h+18:.1f}" rx="26" fill="none" stroke="{palette["selection"]}" stroke-width="8"/>')
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{card_w:.1f}" height="{card_h:.1f}" rx="20" fill="{palette["surface"]}" opacity="{opacity}"/>')
            parts.append(f'<text x="{x+card_w/2:.1f}" y="{y+card_h*.48:.1f}" text-anchor="middle" fill="{palette["text"]}" font-family="sans-serif" font-size="{card_h*.22:.1f}" opacity="{opacity}">{html.escape(entry.label)}</text>')
            parts.append(f'<text x="{x+card_w/2:.1f}" y="{y+card_h*.72:.1f}" text-anchor="middle" fill="{palette["secondary_text"]}" font-family="sans-serif" font-size="{card_h*.11:.1f}" opacity="{opacity}">{html.escape(entry.detail)}</text>')
    parts.append(f'<text x="{width/2:.1f}" y="{height-margin*.35:.1f}" text-anchor="middle" fill="{palette["secondary_text"]}" font-family="sans-serif" font-size="{max(14,int(min(width,height)*.018))}">Preview only — selection returns an opaque target ID; no boot action is executed</text>')
    parts.append('</svg>')
    return '\n'.join(parts)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('profile', nargs='?', type=Path, default=Path(__file__).parent/'profiles/portable-example.json')
    parser.add_argument('--output', type=Path, default=Path('/tmp/portsmith-boot-menu-preview.svg'))
    parser.add_argument('--width', type=int, default=1440)
    parser.add_argument('--height', type=int, default=3120)
    parser.add_argument('--selected-entry')
    args=parser.parse_args()
    if args.width < 320 or args.height < 240:
        parser.error('preview canvas must be at least 320x240')
    try:
        profile=load_profile(args.profile)
        controller=MenuController(profile,args.selected_entry)
        svg=render_svg(profile,controller,args.width,args.height)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(svg)
    except (ValueError,OSError) as exc:
        parser.error(str(exc))
    print(f"Wrote host-only SVG preview {args.output}; no target action was run")
    return 0

if __name__=='__main__':
    raise SystemExit(main())
