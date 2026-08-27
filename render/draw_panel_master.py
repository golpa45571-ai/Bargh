"""MASTER PANEL RENDER v3 — clean from-scratch render of the PDF circuit.
Circuit = MASTER_CIRCUIT_MEMORY.md (7 PDFs), 100%:
Q0 250A 3PH MCCB WITH MOTOR | CT1..CT9 400/5A | SVA x3 | busbar L1 L2 L3 N PE
feeders: Lighting, Q1-Q3 100A MCCB 3P, 3x 125A MCCB 1P, Q5 100A 3PH WITH MOTOR
PSU x2 AC 230V (tags Q0/Q5) | TRB-900 (PV SV REL, PH N, 18 15 16, MAX 5A)
M x2 + green dashed command: TRB relay -> coil -> Q5 operator
Nothing beyond the 42 verbatim labels is drawn.
"""
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math

W, H = 2200, 1400
FB = '/usr/share/fonts/truetype/dejavu/'
def F(sz, bold=False): return ImageFont.truetype(FB + ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'), sz)

img = Image.new('RGB', (W, H), (36, 38, 41))
d = ImageDraw.Draw(img)
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)

def vgrad(xy, c0, c1):
    x0, y0, x1, y1 = xy
    for i in range(y1 - y0):
        t = i / max(1, y1 - y0 - 1)
        d.line([(x0, y0 + i), (x1, y0 + i)], fill=tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3)))

def hgrad(xy, c0, c1):
    x0, y0, x1, y1 = xy
    for i in range(x1 - x0):
        t = i / max(1, x1 - x0 - 1)
        d.line([(x0 + i, y0), (x0 + i, y1)], fill=tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3)))

def module(xy, body=(78, 82, 86), r=6, alpha=110):
    x0, y0, x1, y1 = xy
    sd.rounded_rectangle([x0 + 4, y0 + 6, x1 + 4, y1 + 6], r, fill=(0, 0, 0, alpha))
    vgrad(xy, tuple(min(255, v + 26) for v in body), tuple(max(0, v - 18) for v in body))
    d.rounded_rectangle(xy, r, outline=(30, 32, 34), width=2)
    d.rounded_rectangle([x0 + 2, y0 + 2, x1 - 2, y1 - 2], max(2, r - 1), outline=tuple(min(255, v + 46) for v in body))

def screw(x, y, r=7):
    d.ellipse([x - r, y - r, x + r, y + r], fill=(188, 190, 194), outline=(90, 92, 96), width=2)
    d.ellipse([x - r + 2, y - r + 2, x + r - 2, y + r - 2], outline=(232, 234, 238))
    ang = (x * 13 + y * 7) % 180
    dx, dy = r * math.cos(math.radians(ang)), r * math.sin(math.radians(ang))
    d.line([(x - dx, y - dy), (x + dx, y + dy)], fill=(70, 72, 76), width=2)

def label_plate(xy, lines, szs=None, pad=6, gap=4, bg=(238, 236, 228), fg=(28, 30, 32)):
    x0, y0, x1, y1 = xy
    d.rounded_rectangle(xy, 4, fill=bg, outline=(120, 118, 110))
    n = len(lines); szs = szs or [16] * n
    total = sum(szs) + gap * (n - 1) + 2 * pad
    cy = y0 + (y1 - y0 - total) // 2
    for txt, sz in zip(lines, szs):
        f = F(sz, bold=(sz >= 18))
        bb = d.textbbox((0, 0), txt, font=f)
        d.text((x0 + (x1 - x0 - (bb[2] - bb[0])) / 2, cy), txt, font=f, fill=fg)
        cy += sz + gap

def toggle(x, y, w=30, h=64):
    vgrad((x, y, x + w, y + h), (58, 60, 62), (34, 36, 38))
    d.rounded_rectangle([x, y, x + w, y + h], 4, outline=(18, 18, 20), width=2)
    vgrad((x + 4, y + 6, x + w - 4, y + 26), (215, 212, 200), (150, 146, 136))
    d.rounded_rectangle([x + 4, y + 6, x + w - 4, y + 26], 3, outline=(60, 58, 54))

def donut_ct(cx, cy, r=24, name='', side='left'):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(30, 34, 40), outline=(12, 14, 16), width=3)
    d.ellipse([cx - r + 6, cy - r + 6, cx + r - 6, cy + r - 6], outline=(74, 80, 90))
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=plate_color_at(cx, cy))
    if name:
        narrow = side == 'below'
        f1, f2 = (F(13, True), F(11)) if narrow else (F(14, True), F(12))
        wbox, hbox = (54, 34) if narrow else (78, 36)
        if side == 'left': lx, ly = cx - r - 10 - wbox, cy - hbox // 2
        elif side == 'right': lx, ly = cx + r + 10, cy - hbox // 2
        else: lx, ly = cx - wbox // 2, cy + r + 4
        d.rounded_rectangle([lx, ly, lx + wbox, ly + hbox], 3, fill=(240, 238, 230), outline=(110, 108, 100))
        dy2 = 18 if narrow else 19
        for txt, f, dy in ((name, f1, 3), ('400/5A', f2, dy2)):
            bb = d.textbbox((0, 0), txt, font=f)
            d.text((lx + (wbox - (bb[2] - bb[0])) / 2, ly + dy), txt, font=f, fill=(25, 27, 30))

def dashed(pts, fill=(40, 150, 60), w=3, dash=12, gap=8):
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        L = math.hypot(bx - ax, by - ay)
        if L == 0: continue
        ux, uy = (bx - ax) / L, (by - ay) / L
        s = 0
        while s < L:
            e = min(s + dash, L)
            d.line([(ax + ux * s, ay + uy * s), (ax + ux * e, ay + uy * e)], fill=fill, width=w)
            s = e + gap

def wire(pts, fill=(38, 40, 44), w=6):
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        sd.line([(ax + 3, ay + 5), (bx + 3, by + 5)], fill=(0, 0, 0, 80), width=w)
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        d.line([(ax, ay), (bx, by)], fill=fill, width=w)

def ctext(x, y, txt, sz, bold=True, fg=(250, 250, 248), stroke=None, st_w=3):
    f = F(sz, bold)
    bb = d.textbbox((0, 0), txt, font=f)
    pos = (x - (bb[2] - bb[0]) / 2, y - (bb[3] - bb[1]) / 2 - bb[1])
    if stroke: d.text(pos, txt, font=f, fill=fg, stroke_width=st_w, stroke_fill=stroke)
    else: d.text(pos, txt, font=f, fill=fg)

# ---------- enclosure + interior ----------
d.rounded_rectangle([18, 18, W - 18, H - 18], 26, fill=(52, 55, 58), outline=(20, 21, 23), width=4)
d.rounded_rectangle([30, 30, W - 30, H - 30], 20, outline=(78, 81, 85), width=2)
px0, py0, px1, py1 = 46, 46, W - 46, H - 46
arr = np.zeros((py1 - py0, px1 - px0, 3), dtype=np.uint8)
c_ul, c_ur, c_ll, c_lr = (np.array(c, float) for c in [(96, 90, 82), (150, 143, 132), (128, 121, 110), (196, 190, 178)])
for yy in range(py1 - py0):
    t = yy / (py1 - py0 - 1)
    arr[yy] = np.linspace(c_ul * (1 - t) + c_ll * t, c_ur * (1 - t) + c_lr * t, px1 - px0).astype(np.uint8)
img.paste(Image.fromarray(arr), (px0, py0))
d.rectangle([px0, py0, px1, py1], outline=(60, 58, 52))
def plate_color_at(x, y):
    return tuple(arr[min(max(y, py0), py1 - 1) - py0, min(max(x, px0), px1 - 1) - px0])
for sx, sy in [(64, 64), (W - 64, 64), (64, H - 64), (W - 64, H - 64), (W // 2, 50), (W // 2, H - 50), (50, H // 2), (W - 50, H // 2)]:
    screw(sx, sy, 9)
def din_rail(y, x0=120, x1=2080):
    vgrad((x0, y, x1, y + 16), (168, 170, 174), (120, 122, 126))
    d.rectangle([x0, y, x1, y + 16], outline=(90, 92, 96))
    d.line([(x0, y + 3), (x1, y + 3)], fill=(205, 207, 210)); d.line([(x0, y + 12), (x1, y + 12)], fill=(96, 98, 102))
din_rail(600); din_rail(884)

# ---------- BUSBARS ----------
BUS_X0, BUS_X1 = 150, 2060
bus_y = {'L1': 470, 'L2': 500, 'L3': 530, 'N': 560, 'PE': 590}
bus_c = {'L1': (206, 158, 82), 'L2': (206, 158, 82), 'L3': (206, 158, 82), 'N': (96, 120, 158), 'PE': (120, 148, 96)}
for name, by in bus_y.items():
    c0 = bus_c[name]
    hgrad((BUS_X0, by, BUS_X1, by + 13), tuple(min(255, v + 34) for v in c0), tuple(max(0, v - 36) for v in c0))
    d.rectangle([BUS_X0, by, BUS_X1, by + 13], outline=tuple(max(0, v - 60) for v in c0))
    d.line([(BUS_X0, by + 2), (BUS_X1, by + 2)], fill=tuple(min(255, v + 60) for v in c0))
    d.rounded_rectangle([92, by - 8, 146, by + 21], 4, fill=(40, 42, 45), outline=(18, 19, 21))
    ctext(119, by + 6, name, 20, fg=(245, 245, 240))
for sx in range(300, 2050, 260):
    for by in bus_y.values():
        d.rectangle([sx, by - 2, sx + 12, by + 15], fill=(70, 66, 60), outline=(40, 38, 34))

# ---------- input cable (per PDF: from bottom) ----------
cable_x = 92
d.rounded_rectangle([cable_x - 16, 640, cable_x + 16, H - 46], 8, fill=(28, 29, 31), outline=(12, 12, 14))
wire([(cable_x, 640), (cable_x, 250), (150, 250)], fill=(44, 46, 50), w=10)
wire([(cable_x, 655), (cable_x, 300), (150, 300)], fill=(70, 96, 140), w=6)
wire([(cable_x, 668), (cable_x, 345), (150, 345)], fill=(110, 140, 90), w=6)

# ---------- Q0 ----------
module((150, 80, 340, 340), body=(56, 60, 64))
for tx in (195, 245, 295): toggle(tx, 120, 34, 76)
label_plate((162, 224, 328, 332), ['Q0', 'MCCB', '250A', '3 PHASE', 'WITH MOTOR'], [26, 18, 20, 15, 15], gap=3)
module((150, 26, 226, 72), body=(96, 100, 104), r=4, alpha=60)
d.ellipse([178, 36, 212, 68], outline=(30, 32, 34), width=3, fill=(150, 152, 156))
ctext(195, 52, 'M', 22, fg=(25, 27, 30))
dashed([(195, 72), (195, 80)], fill=(46, 160, 66), w=3)

# Q0 -> CT1..CT6 -> busbar
cond_x = (380, 510, 640)
for i, cx in enumerate(cond_x):
    wire([(cx, 340), (cx, bus_y[['L1', 'L2', 'L3'][i]] + 6)])
    donut_ct(cx, 372, 26, f'CT{i + 1}', side='left')
    donut_ct(cx, 448, 26, f'CT{i + 4}', side='left')

# ---------- SVA meters #1 #2 ----------
def sva_meter(xy, power_supply=False):
    x0, y0, x1, y1 = xy
    module(xy, body=(50, 54, 58), r=8)
    d.rounded_rectangle([x0 + 14, y0 + 14, x1 - 14, y0 + 112], 5, fill=(186, 202, 168), outline=(96, 104, 84), width=2)
    ctext((x0 + x1) // 2, y0 + 44, 'SVA', 30, fg=(30, 46, 30))
    for k in range(6):
        d.rectangle([x0 + 30 + k * ((x1 - x0 - 60) / 6), y0 + 84, x0 + 30 + (k + .6) * ((x1 - x0 - 60) / 6), y0 + 96], fill=(120, 138, 105))
    if power_supply:
        d.rounded_rectangle([x0 + 10, y0 + 122, x1 - 10, y0 + 152], 3, fill=(240, 238, 230), outline=(120, 118, 110))
        ctext((x0 + x1) // 2, y0 + 137, 'POWER SUPPLY', 13, fg=(30, 32, 34))
    ts = (x0 + 10, y1 - 80, x1 - 10, y1 - 12)
    d.rounded_rectangle(ts, 4, fill=(232, 230, 222), outline=(110, 108, 100))
    fts = F(15)
    row1 = ['I1', 'I1', 'I2', 'I2', 'I3', 'I3']; row2 = ['N', 'L1', 'L2', 'L3']
    step = (ts[2] - ts[0] - 16) / 6
    for k, t in enumerate(row1):
        sx = ts[0] + 8 + step * (k + .5); screw(sx, ts[1] + 17, 6)
        bb = d.textbbox((0, 0), t, font=fts); d.text((sx - (bb[2] - bb[0]) / 2, ts[1] + 27), t, font=fts, fill=(30, 32, 34))
    step2 = (ts[2] - ts[0] - 16) / 4
    for k, t in enumerate(row2):
        sx = ts[0] + 8 + step2 * (k + .5); screw(sx, ts[3] - 35, 6)
        bb = d.textbbox((0, 0), t, font=fts); d.text((sx - (bb[2] - bb[0]) / 2, ts[3] - 25), t, font=fts, fill=(30, 32, 34))
sva_meter((720, 80, 930, 340), power_supply=True)
sva_meter((960, 80, 1170, 340))
# CT secondaries -> meters
for cx in cond_x:
    dashed([(cx + 26, 372), (700, 372), (700, 250), (720, 250)], fill=(58, 62, 70), w=2, dash=8, gap=6)
    dashed([(cx + 26, 448), (708, 448), (708, 268), (720, 268)], fill=(58, 62, 70), w=2, dash=8, gap=6)
# voltage taps: from bus RIGHT edge via right-margin corridor (per PDF: common targets at right edge)
for k, bn in enumerate(('L1', 'L2', 'L3', 'N')):
    v = 2108 + 8 * k
    ty = 150 + 18 * k
    dashed([(BUS_X1, bus_y[bn] + 6), (v, bus_y[bn] + 6), (v, ty), (1176, ty)], fill=(150, 140, 96), w=2, dash=7, gap=6)          # -> SVA2
    dashed([(v, ty), (v, 356 + 6 * k), (904 - 42 * k, 356 + 6 * k), (904 - 42 * k, 340)], fill=(150, 140, 96), w=2, dash=7, gap=6)  # -> SVA1 (below modules)

# ---------- FEEDERS ----------
FY0, FY1 = 640, 860
def feeder(xy, poles, lines, szs, plate_h=96):
    module(xy, body=(74, 78, 82))
    x0, y0, x1, y1 = xy; w = x1 - x0
    pw = 30 if poles == 1 else 28
    gap = (w - poles * pw) / (poles + 1)
    for p in range(poles):
        toggle(int(x0 + gap + p * (pw + gap)), y0 + 26, pw, 64)
    label_plate((x0 + 6, y1 - plate_h, x1 - 6, y1 - 10), lines, szs, gap=3)

def bus_taps(x0, x1, phases):
    for pi, ph in enumerate(phases):
        bx = (x0 + x1) / 2 if len(phases) == 1 else x0 + (x1 - x0) * (pi + 1) / (len(phases) + 1)
        wire([(bx, bus_y[ph] + 13), (bx, FY0)], fill=(150, 116, 62), w=7)

feeders_spec = [
    ((160, FY0, 250, FY1), 1, ['Lighting'], [20], ['L1'], 56),
    ((270, FY0, 380, FY1), 3, ['Q1', '100A', 'MCCB'], [20, 19, 16], ['L1', 'L2', 'L3'], 76),
    ((400, FY0, 510, FY1), 3, ['Q2', '100A', 'MCCB'], [20, 19, 16], ['L1', 'L2', 'L3'], 76),
    ((530, FY0, 640, FY1), 3, ['Q3', '100A', 'MCCB'], [20, 19, 16], ['L1', 'L2', 'L3'], 76),
    ((660, FY0, 716, FY1), 1, ['125A', 'MCCB'], [18, 15], ['L1'], 60),
    ((736, FY0, 792, FY1), 1, ['125A', 'MCCB'], [18, 15], ['L2'], 60),
    ((812, FY0, 868, FY1), 1, ['125A', 'MCCB'], [18, 15], ['L3'], 60),
    ((900, FY0, 1060, FY1), 3, ['Q5', 'MCCB', '100A', '3PHASE', 'WITH MOTOR'], [20, 16, 17, 14, 13], ['L1', 'L2', 'L3'], 106),
]
for xy, poles, lines, szs, phases, ph in feeders_spec:
    feeder(xy, poles, lines, szs, plate_h=ph); bus_taps(xy[0], xy[2], phases)
    for k in range(poles):
        bx = xy[0] + (xy[2] - xy[0]) * (k + 1) / (poles + 1)
        wire([(bx, xy[3]), (bx, xy[3] + 46)], fill=(40, 42, 46), w=6)
# M operator on Q5
module((1080, 606, 1150, 646), body=(96, 100, 104), r=4, alpha=60)
d.ellipse([1106, 612, 1138, 642], outline=(30, 32, 34), width=3, fill=(150, 152, 156))
ctext(1122, 627, 'M', 20, fg=(25, 27, 30))
dashed([(1122, 646), (1122, FY0 + 20)], fill=(46, 160, 66), w=3)

# ---------- Q5 load: CT7-9 -> SVA#3 ----------
q5c = (925, 980, 1035)
for i, cx in enumerate(q5c):
    wire([(cx, FY1 + 46), (cx, 990)], fill=(40, 42, 46), w=6)
    donut_ct(cx, 946, 20, f'CT{7 + i}', side='below')
sva_meter((1600, 1030, 1810, 1270))
# CT7-9 secondaries -> SVA3 (corridor x1100-1140, below TRB)
for k, cx in enumerate(q5c):
    vx = 1100 + 20 * k
    dashed([(cx + 22, 946), (vx, 946), (vx, 1344 + 4 * k), (1620, 1344 + 4 * k), (1620, 1270)], fill=(58, 62, 70), w=2, dash=8, gap=6)
# SVA3 voltage taps: far-right corridor x2160-2186
for k, bn in enumerate(('L1', 'L2', 'L3', 'N')):
    v = 2160 + 6 * k
    ty = 940 + 16 * k
    dashed([(BUS_X1, bus_y[bn] + 6), (v, bus_y[bn] + 6), (v, ty), (1650 + 45 * k, ty), (1650 + 45 * k, 1030)], fill=(150, 140, 96), w=2, dash=7, gap=6)

# ---------- PSUs ----------
def psu(xy, tag):
    x0, y0, x1, y1 = xy
    module(xy, body=(120, 122, 118))
    label_plate((x0 + 10, y0 + 14, x1 - 10, y0 + 86), ['POWER SUPPLY', 'AC 230V'], [17, 19], gap=5)
    for k in range(2): screw(x0 + 34 + k * (x1 - x0 - 68), y1 - 26, 7)
    pb = (x1 + 14, y0 + 6, x1 + 58, y1 - 6)
    module(pb, body=(70, 74, 78), r=4, alpha=60)
    toggle((pb[0] + pb[2]) // 2 - 11, pb[1] + 14, 22, 38)
    ctext((pb[0] + pb[2]) // 2, pb[3] - 22, tag, 16, fg=(245, 245, 240))
psu((160, 960, 330, 1150), 'Q0')
psu((430, 960, 600, 1150), 'Q5')
dashed([(168, bus_y['L1'] + 13), (140, 620), (140, 940), (160, 940)], fill=(150, 140, 96), w=2, dash=9, gap=7)
dashed([(606, bus_y['L1'] + 13), (620, 620), (620, 940), (606, 940)], fill=(150, 140, 96), w=2, dash=9, gap=7)
# 230V rails to TRB terminals
wire([(330, 1150), (330, 1368), (1246, 1368), (1246, 1312)], fill=(38, 40, 44), w=4)
wire([(600, 1150), (600, 1384), (1310, 1384), (1310, 1312)], fill=(70, 96, 140), w=4)
ctext(356, 1330, 'PH', 15, fg=(240, 240, 235), stroke=(40, 42, 45))
ctext(626, 1330, 'N', 15, fg=(240, 240, 235), stroke=(40, 42, 45))

# ---------- TRB-900 (x1180-1560) ----------
tx0, ty0, tx1, ty1 = 1180, 940, 1560, 1330
module((tx0, ty0, tx1, ty1), body=(38, 40, 43), r=10, alpha=130)
mx = (tx0 + tx1) // 2
ctext(mx, ty0 + 34, 'SHIVA AMVAJ', 20, fg=(235, 235, 228))
ctext(mx, ty0 + 66, 'TEMPERATURE CONTROLLER', 17, fg=(210, 210, 202))
ctext(mx, ty0 + 98, 'TRB-900', 26, fg=(250, 250, 248))
ctext(mx, ty0 + 130, 'CODE: 15B2', 16, fg=(180, 182, 186))
for dy, nm in ((152, 'PV'), (240, 'SV')):
    d.rounded_rectangle([tx0 + 74, ty0 + dy, tx1 - 74, ty0 + dy + 60], 6, fill=(24, 46, 26), outline=(70, 96, 70), width=2)
    ctext(tx0 + 44, ty0 + dy + 30, nm, 20, fg=(120, 200, 120))
    for seg in range(4):
        d.rectangle([tx0 + 112 + seg * 58, ty0 + dy + 22, tx0 + 144 + seg * 58, ty0 + dy + 42], fill=(42, 74, 44))
d.ellipse([tx0 + 46, ty0 + 322, tx0 + 78, ty0 + 354], fill=(60, 150, 70), outline=(28, 60, 32), width=2)
ctext(tx0 + 112, ty0 + 338, 'REL', 20, fg=(150, 225, 150))
ctext(tx0 + 220, ty0 + 338, '180-250 VAC', 16, fg=(225, 226, 228))
ctext(tx0 + 330, ty0 + 338, 'MAX 5A', 17, fg=(240, 240, 235))
term_y = ty1 - 26
for k, t in enumerate(('PH', 'N')):
    sx = tx0 + 70 + k * 64; screw(sx, term_y, 8); ctext(sx, term_y - 40, t, 16, fg=(235, 235, 228))
ctext(tx0 + 176, term_y - 40, '+', 18, fg=(235, 235, 228))
ctext(tx0 + 198, term_y - 40, '−', 18, fg=(235, 235, 228))
for k, t in enumerate(('18', '15', '16')):
    sx = tx0 + 240 + k * 60; screw(sx, term_y, 8); ctext(sx, term_y - 40, t, 17, fg=(235, 235, 228))

# ---------- command: TRB relay -> coil -> M(Q5) ----------
coil = (880, 1040, 960, 1096)
d.rounded_rectangle(coil, 6, fill=(238, 236, 228), outline=(60, 62, 66), width=3)
for k in range(3):
    d.arc([coil[0] + 14 + k * 24, coil[1] + 12, coil[0] + 34 + k * 24, coil[1] + 44], 200, 340, fill=(28, 30, 32), width=3)
dashed([(tx0 + 220, term_y + 8), (tx0 + 220, 1356), (920, 1356), (920, coil[3])], fill=(46, 160, 66), w=3)      # 18 -> coil
dashed([(tx0 + 280, term_y + 8), (tx0 + 280, 1332), (960, 1332), (960, coil[3])], fill=(46, 160, 66), w=3)      # 15 -> coil
dashed([(tx0 + 340, term_y + 8), (tx0 + 340, 1388), (630, 1388), (630, 1384)], fill=(46, 160, 66), w=3)          # 16 -> N
dashed([(1090, coil[1] + 28), (1090, 700), (1122, 700), (1122, 646)], fill=(46, 160, 66), w=3, dash=10, gap=7)   # coil -> M(Q5)

img = Image.alpha_composite(img.convert('RGBA'), shadow).convert('RGB')
img.save('/home/user/Bargh/render/panel_master_circuit.png')
print('saved', img.size)
