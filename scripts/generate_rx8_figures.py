"""Generate the original SVG diagrams used by the compact RX-8 notebook."""

from __future__ import annotations

import html
import math
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "assets" / "rx8" / "generated"
BLUE = "#176b87"
ORANGE = "#c85f20"
RED = "#a73535"
GREEN = "#2f7d5a"
INK = "#17212b"
MUTED = "#60717d"
PALE = "#edf4f6"


def esc(value: object) -> str:
    return html.escape(str(value))


def text(x: float, y: float, value: object, css: str = "label", anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" class="{css}" text-anchor="{anchor}">{esc(value)}</text>'


def line(x1: float, y1: float, x2: float, y2: float, css: str = "line", marker: bool = False) -> str:
    end = ' marker-end="url(#arrow)"' if marker else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{css}"{end}/>'


def box(x: float, y: float, w: float, h: float, label: str, sub: str = "", css: str = "box") -> str:
    body = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" class="{css}"/>'
    body += text(x + w / 2, y + 28, label, "box-title", "middle")
    if sub:
        body += text(x + w / 2, y + 50, sub, "small", "middle")
    return body


def frame(title: str, description: str, body: str, width: int = 1000, height: int = 560) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{esc(title)}</title><desc id="desc">{esc(description)}</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><path d="M0 0 L10 3.5 L0 7z" fill="context-stroke"/></marker></defs>
<style>
text{{font-family:Arial,sans-serif;fill:{INK}}}.title{{font-size:25px;font-weight:700}}.label{{font-size:14px}}.small{{font-size:12px;fill:{MUTED}}}.box-title{{font-size:15px;font-weight:700}}.line{{stroke:{MUTED};stroke-width:2;fill:none}}.arrow{{stroke:{BLUE};stroke-width:3;fill:none}}.hot{{stroke:{ORANGE};stroke-width:4;fill:none}}.cold{{stroke:{BLUE};stroke-width:4;fill:none}}.dash{{stroke-dasharray:8 6}}.grid{{stroke:#d8e1e5;stroke-width:1}}.box{{fill:{PALE};stroke:{BLUE};stroke-width:2}}.warn{{fill:#fbebeb;stroke:{RED};stroke-width:2}}.good{{fill:#e6f3ec;stroke:{GREEN};stroke-width:2}}
</style><rect width="100%" height="100%" fill="white"/>{text(42, 42, title, 'title')}{body}</svg>'''


def gear_speed() -> str:
    ratios = (("1", 3.760), ("2", 2.269), ("3", 1.645), ("4", 1.187), ("5", 1.000), ("6", 0.843))
    colours = ("#263b73", BLUE, GREEN, "#9b7610", ORANGE, RED)
    final_drive = 4.444
    circumference = math.pi * 0.6597
    left, top, w, h = 76, 82, 820, 390
    body = ""
    for mph in range(0, 201, 25):
        yy = top + h - mph / 200 * h
        body += line(left, yy, left + w, yy, "grid") + text(left - 10, yy + 4, mph, "small", "end")
    for rpm in range(0, 10000, 1000):
        xx = left + rpm / 9500 * w
        body += line(xx, top, xx, top + h, "grid") + text(xx, top + h + 22, rpm, "small", "middle")
    for (name, ratio), colour in zip(ratios, colours):
        points = []
        for rpm in range(0, 9501, 100):
            mph = rpm * 60 * circumference / (ratio * final_drive * 1000 * 1.609344)
            points.append(f"{left + rpm / 9500 * w:.1f},{top + h - min(mph, 200) / 200 * h:.1f}")
        body += f'<polyline points="{" ".join(points)}" fill="none" stroke="{colour}" stroke-width="2.5"/>'
        mph_end = 9500 * 60 * circumference / (ratio * final_drive * 1000 * 1.609344)
        body += text(left + w + 9, top + h - min(mph_end, 200) / 200 * h + 4, name, "label")
    body += line(left, top + h, left + w, top + h) + line(left, top, left, top + h)
    body += text(485, 535, "Engine speed (rpm)", "label", "middle")
    body += text(18, 285, "Road speed (mph)", "label")
    body += text(930, 500, "225/45R18", "small", "end")
    return frame("Y16M-D calculated road speed", "Road speed by engine speed for all six gears, a 4.444 final drive and nominal 225/45R18 tyre.", body)


def shift_drop() -> str:
    ratios = (3.760, 2.269, 1.645, 1.187, 1.000, 0.843)
    starts = (8500, 9000, 9500)
    body = text(425, 80, "Before shift", "small", "middle") + text(610, 80, "After shift", "small", "middle")
    for row in range(5):
        y = 105 + row * 82
        body += text(90, y + 30, f"{row + 1} → {row + 2}", "box-title")
        for col, start in enumerate(starts):
            after = round(start * ratios[row + 1] / ratios[row])
            x = 260 + col * 225
            body += box(x, y, 180, 52, f"{start:,} → {after:,}", "rpm", "box")
    body += text(500, 535, "Calculated ratio change only; shift time and road-speed loss are excluded.", "small", "middle")
    return frame("Y16M-D upshift RPM drop", "Engine speed after each upshift from 8500, 9000 and 9500 rpm.", body)


def fan_logic() -> str:
    x = lambda temp: 100 + (temp - 90) / 15 * 800
    body = ""
    for temp in range(90, 106):
        body += line(x(temp), 105, x(temp), 455, "grid") + text(x(temp), 477, f"{temp}°", "small", "middle")
    body += text(95, 88, "Coolant temperature", "label")
    bands = (("Rising: off", 90, 97, 135, "#dceaf0"), ("Rising: both low", 97, 101, 210, "#b8dfcf"), ("Rising: both high", 101, 105, 285, "#efb5a5"), ("Falling: high → low at 98°C", 98, 105, 360, "#f3caac"), ("Falling: low → off at 94°C", 94, 98, 420, "#cce5d9"))
    for label, start, end, y, colour in bands:
        body += f'<rect x="{x(start)}" y="{y}" width="{x(end)-x(start)}" height="38" rx="5" fill="{colour}" stroke="#61717a"/>'
        body += text((x(start) + x(end)) / 2, y + 24, label, "label", "middle")
    body += text(500, 525, "A/C pressure can request fans independently; ECT failure requests high speed.", "small", "middle")
    return frame("Series 1 cooling-fan temperature logic", "Fan low and high thresholds with falling-temperature hysteresis.", body)


def coolant_layout() -> str:
    body = box(60, 215, 145, 70, "Water pump", "thermostat inlet")
    body += box(270, 190, 175, 120, "Engine housings", "front · intermediate · rear")
    body += box(535, 215, 145, 70, "Thermostat", "80–84°C starts")
    body += box(785, 180, 155, 140, "Radiator", "upper feed / lower return")
    body += box(285, 390, 145, 70, "Heater matrix", "RHD firewall")
    body += box(515, 390, 145, 70, "Throttle body", "warming loop")
    body += box(720, 55, 180, 80, "Expansion tank", "degas and bleed")
    body += line(205, 250, 270, 250, "cold", True)
    body += line(445, 230, 535, 230, "hot", True)
    body += line(680, 230, 785, 230, "hot", True)
    body += f'<path d="M785 285 C700 350 300 345 205 270" class="cold" marker-end="url(#arrow)"/>'
    body += f'<path d="M565 285 C540 340 475 340 445 270" class="cold dash" marker-end="url(#arrow)"/>'
    body += text(505, 335, "cold bypass", "small", "middle")
    body += f'<path d="M350 310 L350 390" class="hot" marker-end="url(#arrow)"/>'
    body += f'<path d="M430 425 C470 425 480 425 515 425" class="cold" marker-end="url(#arrow)"/>'
    body += f'<path d="M660 425 C705 410 690 300 635 285" class="cold" marker-end="url(#arrow)"/>'
    body += f'<path d="M420 190 C470 95 620 95 720 95" class="hot" marker-end="url(#arrow)"/>'
    body += f'<path d="M785 195 C770 155 775 125 790 135" class="hot" marker-end="url(#arrow)"/>'
    body += text(80, 505, "Blue: cooled/return and bypass", "small") + text(330, 505, "Orange: hot outlet/bleed", "small")
    return frame("Series 1 coolant routing", "Functional hose-routing diagram showing pump, engine, thermostat, radiator, heater, throttle loop, expansion tank, cold bypass and warm radiator flow.", body)


def jacking_points() -> str:
    body = f'<path d="M310 80 Q260 130 255 235 L255 430 Q265 500 340 515 L660 515 Q735 500 745 430 L745 235 Q740 130 690 80 Z" fill="#f4f6f7" stroke="{INK}" stroke-width="3"/>'
    body += text(500, 72, "FRONT", "box-title", "middle")
    body += f'<rect x="355" y="135" width="290" height="50" rx="8" fill="#dbe7eb" stroke="{INK}"/>'
    body += f'<circle cx="500" cy="160" r="18" fill="{ORANGE}"/>' + text(500, 165, "J", "box-title", "middle")
    body += text(500, 115, "centre of front crossmember", "label", "middle")
    body += f'<path d="M420 390 L580 390 L625 460 L375 460 Z" fill="#dbe7eb" stroke="{INK}" stroke-width="2"/>'
    body += f'<circle cx="500" cy="420" r="18" fill="{ORANGE}"/>' + text(500, 425, "J", "box-title", "middle")
    body += text(500, 482, "solid centre of differential case", "label", "middle")
    for x, y in ((285, 185), (715, 185), (285, 395), (715, 395)):
        body += f'<rect x="{x-14}" y="{y-28}" width="28" height="56" rx="5" fill="{GREEN}" stroke="{INK}"/>'
    body += text(225, 298, "reinforced sill support areas", "label", "end")
    body += line(235, 292, 275, 210, "line", True) + line(235, 302, 275, 380, "line", True)
    for x, y, label in ((500, 235, "sump"), (500, 330, "gearbox / PPF"), (500, 455, "diff cover")):
        body += f'<path d="M{x-10} {y-10} L{x+10} {y+10} M{x+10} {y-10} L{x-10} {y+10}" stroke="{RED}" stroke-width="5"/>'
        body += text(x + 18, y + 5, label, "small")
    body += text(805, 165, "J = central jack", "small") + text(805, 190, "green = axle stand", "small")
    return frame("RX-8 jacking and support points", "Top-down underside diagram identifying the centre front crossmember, centre differential case and four reinforced sill support positions, plus areas not to load.", body)


def ppf_datum() -> str:
    body = f'<circle cx="165" cy="330" r="92" fill="#e1e6e8" stroke="{INK}" stroke-width="3"/>'
    body += text(165, 335, "gearbox", "box-title", "middle")
    body += f'<circle cx="850" cy="355" r="105" fill="#e1e6e8" stroke="{INK}" stroke-width="3"/>'
    body += text(850, 360, "differential", "box-title", "middle")
    body += f'<path d="M235 360 L770 395 L775 430 L235 395 Z" fill="#c5d9e1" stroke="{BLUE}" stroke-width="3"/>'
    body += text(520, 413, "PPF lower surface", "label", "middle")
    body += f'<rect x="245" y="235" width="205" height="35" fill="#d7d7d7" stroke="{INK}" stroke-width="2"/>'
    body += text(347, 220, "installed front tunnel member", "label", "middle")
    body += line(290, 270, 290, 390, "hot")
    body += f'<path d="M282 280 L290 270 L298 280 M282 380 L290 390 L298 380" stroke="{ORANGE}" stroke-width="3" fill="none"/>'
    body += text(310, 332, "A = 48.4–56.4 mm", "box-title")
    body += text(500, 500, "Measure lower PPF surface to lower tunnel-member surface at Mazda's front datum.", "small", "middle")
    return frame("Power Plant Frame dimension A", "Side-view diagram showing the PPF height measurement between its lower surface and the installed front tunnel member.", body)


def compression_waveform() -> str:
    left, top, w, h = 72, 90, 860, 360
    duration = 2.64
    peaks = [(0.15 + i * 0.24, (790, 620, 805)[i % 3], "ABC"[i % 3]) for i in range(11)]
    points = []
    for n in range(1000):
        t = duration * n / 999
        pressure = 8.0
        for peak_t, amplitude, _ in peaks:
            dt = t - peak_t
            width = 0.025 if dt < 0 else 0.060
            pressure += amplitude * math.exp(-((dt / width) ** 2))
        x = left + t / duration * w
        y = top + h - pressure / 900 * h
        points.append(f"{x:.1f},{y:.1f}")
    body = ""
    for pressure in range(0, 901, 200):
        y = top + h - pressure / 900 * h
        body += line(left, y, left + w, y, "grid") + text(left - 10, y + 4, pressure, "small", "end")
    minimum_y = top + h - 680 / 900 * h
    body += f'<line x1="{left}" y1="{minimum_y}" x2="{left+w}" y2="{minimum_y}" stroke="{RED}" stroke-width="2" stroke-dasharray="8 6"/>'
    body += text(left + w - 5, minimum_y - 8, "680 kPa minimum @ 250 rpm", "small", "end")
    body += f'<polyline points="{" ".join(points)}" fill="none" stroke="{BLUE}" stroke-width="2.5"/>'
    for i, (peak_t, amplitude, group) in enumerate(peaks):
        x = left + peak_t / duration * w
        y = top + h - (amplitude + 8) / 900 * h
        colour = RED if group == "B" else GREEN
        body += f'<circle cx="{x}" cy="{y}" r="5" fill="white" stroke="{colour}" stroke-width="3"/>'
        body += text(x, y - 11, group, "small", "middle")
        if i == 0:
            next_x = left + peaks[1][0] / duration * w
            body += line(x, 472, next_x, 472, "hot") + text((x + next_x) / 2, 495, "0.240 s adjacent", "small", "middle")
        if i == 3:
            first_x = left + peaks[0][0] / duration * w
            body += line(first_x, 520, x, 520, "cold") + text((first_x + x) / 2, 542, "0.720 s same group", "small", "middle")
    body += line(left, top + h, left + w, top + h) + line(left, top, left, top + h)
    body += text(20, 280, "Pressure (kPa)", "label") + text(920, 475, "Time", "label", "end")
    body += text(930, 70, "SYNTHETIC — weak B group", "small", "end")
    return frame("Rotary compression waveform", "Synthetic pressure-time waveform at 250 rpm showing repeating A B C groups, a weak B event and adjacent and same-group timing.", body)


def manual_fan() -> str:
    body = box(55, 150, 150, 80, "Ignition feed", "added 1 A fuse")
    body += box(260, 150, 150, 80, "Dash switch", "drives added coil")
    body += box(465, 135, 180, 110, "Added relay", "coil 85/86 · NO 30/87")
    body += box(740, 120, 200, 140, "Factory fan relay 1", "A: switched B+ · E: low control")
    body += line(205, 190, 260, 190, "arrow", True) + line(410, 190, 465, 190, "arrow", True)
    body += f'<path d="M555 245 L555 350 L720 350 L720 220 L740 220" class="arrow" marker-end="url(#arrow)"/>'
    body += box(470, 360, 170, 70, "Chassis ground", "clean earth")
    body += line(555, 350, 555, 360, "arrow", True)
    body += box(735, 335, 205, 90, "PCM output 5X", "original ground request")
    body += line(835, 335, 835, 260, "arrow", True)
    body += text(690, 318, "30 earth · 87 to terminal E", "small", "middle")
    body += text(500, 500, "Never apply 12 V to terminal E or PCM 5X. Relays 2/3 and PCM 5AD remain untouched.", "box-title", "middle")
    return frame("Manual low-speed fan request", "Added relay wiring that grounds the factory fan relay number 1 terminal E control node while retaining PCM control.", body)


def fuel_module() -> str:
    body = f'<path d="M260 95 L740 95 L700 500 L300 500 Z" fill="#f4f6f7" stroke="{INK}" stroke-width="3"/>'
    body += text(500, 125, "factory reservoir cup", "box-title", "middle")
    body += f'<rect x="415" y="165" width="170" height="225" rx="36" fill="#d9e8ed" stroke="{BLUE}" stroke-width="3"/>'
    body += text(500, 235, "KEMSO 10910", "box-title", "middle") + text(500, 260, "approx. Ø38 mm", "label", "middle")
    body += f'<rect x="390" y="205" width="220" height="55" rx="10" fill="#eadcf1" stroke="#754587" stroke-width="3"/>'
    body += text(500, 290, "PA11-HP retaining clip", "label", "middle")
    body += f'<path d="M500 165 C560 115 650 135 670 180" class="hot" marker-end="url(#arrow)"/>'
    body += text(685, 185, "submerged hose to outlet", "small")
    body += f'<path d="M465 390 L345 465 L515 465 Z" fill="#d8d2a8" stroke="#756c32" stroke-width="2"/>'
    body += text(335, 485, "strainer low in cup", "small")
    body += f'<path d="M640 165 Q760 280 630 435" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="7 5"/>'
    body += text(780, 300, "sender arm full sweep", "label", "middle")
    body += text(90, 205, "Check:", "box-title")
    for i, value in enumerate(("polarity", "outlet load", "wire chafe", "cup passages", "module seal")):
        body += text(105, 235 + i * 28, f"• {value}", "label")
    return frame("RX-8 fuel-pump module checkpoints", "Sectional functional diagram showing KEMSO pump retention, submerged hose, low strainer position, sender-arm clearance and reservoir cup.", body)


def sohn_path() -> str:
    body = text(245, 90, "FACTORY", "box-title", "middle")
    body += box(55, 125, 150, 70, "Engine sump") + box(280, 125, 165, 70, "Front-cover feed")
    body += box(160, 250, 170, 70, "Factory OMP") + box(160, 385, 170, 70, "Four nozzles")
    body += line(205, 160, 280, 160, "arrow", True) + line(360, 195, 300, 250, "arrow", True) + line(245, 320, 245, 385, "arrow", True)
    body += text(755, 90, "SEPARATE SUPPLY", "box-title", "middle")
    body += box(555, 125, 170, 70, "Vented reservoir", "Bio-Rotary oil")
    body += box(790, 125, 155, 70, "Supply hose", "air-free route")
    body += box(665, 250, 180, 70, "Custom adapter", "closes sump feed")
    body += box(665, 355, 180, 70, "Factory OMP", "PCM control retained")
    body += box(665, 465, 180, 60, "Four nozzles")
    body += line(725, 160, 790, 160, "arrow", True) + line(865, 195, 815, 250, "arrow", True)
    body += line(755, 320, 755, 355, "arrow", True) + line(755, 425, 755, 465, "arrow", True)
    body += text(500, 300, "→", "title", "middle")
    return frame("Factory and custom Sohn oil paths", "Comparison of factory sump-fed metering oil with a vented separate reservoir feeding the same factory OMP and four nozzles.", body)


def write_outputs() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    figures = {
        "gear-speed-curves.svg": gear_speed(),
        "shift-rpm-drop.svg": shift_drop(),
        "fan-temperature-logic.svg": fan_logic(),
        "coolant-system-layout.svg": coolant_layout(),
        "chassis-jacking-points.svg": jacking_points(),
        "ppf-datum.svg": ppf_datum(),
        "compression-waveform.svg": compression_waveform(),
        "manual-fan-request.svg": manual_fan(),
        "fuel-pump-module.svg": fuel_module(),
        "sohn-oil-path.svg": sohn_path(),
    }
    for name, content in figures.items():
        (OUT / name).write_text(content, encoding="utf-8", newline="\n")
    print(f"Generated {len(figures)} RX-8 figures in {OUT}")


if __name__ == "__main__":
    write_outputs()
