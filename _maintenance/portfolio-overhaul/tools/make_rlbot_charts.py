#!/usr/bin/env python3
"""Draw the two Rocket League charts used on the notes, from the constants in rlbot_maths_tests.py.

    python -I make_rlbot_charts.py

Writes assets/rlbot/throttle-acceleration.svg and assets/rlbot/turning-radius.svg (standard library only).
The data are community-measured values (see research/rlbot-research.md), not measurements of this site's bot.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = ROOT / "assets" / "rlbot"

spec = importlib.util.spec_from_file_location("maths", HERE / "rlbot_maths_tests.py")
maths = importlib.util.module_from_spec(spec)
spec.loader.exec_module(maths)

W, H = 680, 380
L, R, T, B = 70, 24, 24, 58
PW, PH = W - L - R, H - T - B
INK, GRID, ACCENT, GREY = "#181b26", "#d9dadf", "#5a00b3", "#2d343d"


def svg_open(title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-labelledby="t d" font-family="Arial, Helvetica, sans-serif">\n  <title id="t">{title}</title>\n'
            f'  <desc id="d">{desc}</desc>\n  <rect width="{W}" height="{H}" fill="#ffffff"/>\n')


def axes(xmax, ymax, xticks, yticks, xlabel, ylabel, fmt_y=lambda v: f"{v:g}"):
    sx = lambda x: L + PW * x / xmax
    sy = lambda y: T + PH * (1 - y / ymax)
    s = ""
    for yt in yticks:
        s += f'  <line x1="{L}" y1="{sy(yt):.1f}" x2="{W - R}" y2="{sy(yt):.1f}" stroke="{GRID}" stroke-width="1"/>\n'
        s += f'  <text x="{L - 8}" y="{sy(yt) + 4:.1f}" text-anchor="end" font-size="13" fill="{GREY}">{fmt_y(yt)}</text>\n'
    for xt in xticks:
        s += f'  <line x1="{sx(xt):.1f}" y1="{T}" x2="{sx(xt):.1f}" y2="{T + PH}" stroke="{GRID}" stroke-width="1"/>\n'
        s += f'  <text x="{sx(xt):.1f}" y="{T + PH + 20}" text-anchor="middle" font-size="13" fill="{GREY}">{xt:g}</text>\n'
    s += f'  <line x1="{L}" y1="{T + PH}" x2="{W - R}" y2="{T + PH}" stroke="{INK}" stroke-width="1.5"/>\n'
    s += f'  <line x1="{L}" y1="{T}" x2="{L}" y2="{T + PH}" stroke="{INK}" stroke-width="1.5"/>\n'
    s += f'  <text x="{L + PW / 2}" y="{H - 12}" text-anchor="middle" font-size="14" fill="{INK}">{xlabel}</text>\n'
    s += (f'  <text transform="translate(18 {T + PH / 2}) rotate(-90)" text-anchor="middle" font-size="14" '
          f'fill="{INK}">{ylabel}</text>\n')
    return s, sx, sy


def polyline(points, colour, width=3, dash=None):
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'  <polyline points="{pts}" fill="none" stroke="{colour}" stroke-width="{width}" stroke-linejoin="round"{d}/>\n'


def throttle_chart():
    s = svg_open("Forward acceleration against speed on the ground",
                 "Two lines. Throttle only: 1600 uu/s squared at rest falling linearly to 160 at 1400 uu/s and to zero at 1410. "
                 "Throttle plus boost: the same curve raised by 991.667 uu/s squared until the 2300 uu/s speed cap.")
    ax, sx, sy = axes(2400, 2800, [0, 500, 1000, 1500, 2000, 2300], [0, 500, 1000, 1500, 2000, 2500],
                      "Forward speed (uu/s)", "Acceleration (uu/s²)")
    s += ax
    xs = [0, 1400, 1410, 2300]
    thr = [(sx(v), sy(maths.throttle_accel(v))) for v in xs]
    boost = [(sx(v), sy(maths.accel(v, True))) for v in (0, 1400, 1410, 2299.9)] + [(sx(2300), sy(0))]
    s += polyline(boost, ACCENT)
    s += polyline(thr, INK)
    s += f'  <line x1="{sx(2300):.1f}" y1="{T}" x2="{sx(2300):.1f}" y2="{T + PH}" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="6 5"/>\n'
    s += f'  <line x1="{sx(1410):.1f}" y1="{T}" x2="{sx(1410):.1f}" y2="{T + PH}" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="6 5"/>\n'
    s += f'  <text x="{sx(1410) + 6:.1f}" y="{T + 16}" font-size="12" fill="{GREY}">1410: throttle-only top speed</text>\n'
    s += f'  <text x="{sx(2300) - 6:.1f}" y="{T + 34}" text-anchor="end" font-size="12" fill="{GREY}">2300: speed cap</text>\n'
    s += f'  <text x="{sx(260):.1f}" y="{sy(2530):.1f}" font-size="14" font-weight="700" fill="{ACCENT}">Throttle + boost</text>\n'
    s += f'  <text x="{sx(260):.1f}" y="{sy(1370):.1f}" font-size="14" font-weight="700" fill="{INK}">Throttle only</text>\n'
    s += f'  <text x="{sx(40):.1f}" y="{sy(1600) - 10:.1f}" font-size="12" fill="{GREY}">1600</text>\n'
    return s + "</svg>\n"


def radius_chart():
    s = svg_open("Minimum turning radius against speed",
                 "Minimum turning radius grows from 145 uu at rest to 251 at 500, 426 at 1000, 725 at 1500, 909 at 1750 and 1136 at the 2300 uu/s cap.")
    ax, sx, sy = axes(2400, 1250, [0, 500, 1000, 1500, 2000, 2300], [0, 250, 500, 750, 1000],
                      "Forward speed (uu/s)", "Minimum turning radius (uu)")
    s += ax
    pts = [(sx(v), sy(maths.radius_at(v))) for v in range(0, 2301, 50)]
    s += polyline(pts, ACCENT)
    for v, _ in maths.CURVATURE:
        r = maths.radius_at(v)
        s += f'  <circle cx="{sx(v):.1f}" cy="{sy(r):.1f}" r="4.5" fill="#ffffff" stroke="{ACCENT}" stroke-width="2.5"/>\n'
        dy = -10 if v else -10
        anchor = "middle" if v < 2300 else "end"
        dx = 0 if v < 2300 else 6
        s += f'  <text x="{sx(v) + dx:.1f}" y="{sy(r) + dy:.1f}" text-anchor="{anchor}" font-size="12" fill="{INK}">{r:.0f}</text>\n'
    s += f'  <text x="{L + 10}" y="{T + 18}" font-size="12" fill="{GREY}">1 uu = 1 cm, so 1136 uu is about 11 m</text>\n'
    return s + "</svg>\n"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "throttle-acceleration.svg").write_text(throttle_chart(), encoding="utf-8")
    (OUT / "turning-radius.svg").write_text(radius_chart(), encoding="utf-8")
    print("wrote", OUT / "throttle-acceleration.svg", "and", OUT / "turning-radius.svg")


if __name__ == "__main__":
    main()
