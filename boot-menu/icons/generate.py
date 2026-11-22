#!/usr/bin/env python3
"""Generate original, generic rounded-square version badges (no Apple assets/logos)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent
COLORS = {
  12: ("#4267b2", "#8a4fff"), 13: ("#2877c7", "#5943c8"),
  14: ("#087f9b", "#713bd1"), 15: ("#3b56c4", "#a047c2"),
  16: ("#d69358", "#65598f"), 17: ("#13a889", "#296ad3"),
  18: ("#6550dc", "#d45f9b"), 26: ("#3967a7", "#ad5d8c"),
  27: ("#366b9f", "#7960cd"),
}

TEMPLATE = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img" aria-labelledby="title desc">
  <title id="title">Portsmith generic iOS {version} menu badge</title>
  <desc id="desc">Original abstract version token; not official Apple iconography.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
    <linearGradient id="ribbon" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".28"/><stop offset="1" stop-color="#ffffff" stop-opacity=".02"/></linearGradient>
  </defs>
  <rect x="16" y="16" width="480" height="480" rx="108" fill="url(#bg)"/>
  <circle cx="88" cy="92" r="156" fill="#ffffff" opacity=".09"/>
  <path d="M20 335 C145 235 295 395 495 205 L495 430 C320 560 160 350 18 495 Z" fill="url(#ribbon)"/>
  <text x="256" y="207" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="70" font-weight="600" letter-spacing="2">iOS</text>
  <text x="256" y="366" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="180" font-weight="700">{version}</text>
</svg>
'''

for version, (c1, c2) in COLORS.items():
    (OUT / f"ios-{version}.svg").write_text(TEMPLATE.format(version=version, c1=c1, c2=c2))
print(f"Generated {len(COLORS)} generic iOS-version badges in {OUT}")
