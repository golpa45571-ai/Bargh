"""CLEAN ENGINEERING SCHEMATIC — 100% faithful to the 7 PDFs (fresh audit).
001: Q0 MCCB/CB WITH MOTOR 3 PHASE 250A | CT1..CT6 400/5A | SVA#1/#2
     (I1I1 I2I2 I3I3 + N L1 L2 L3, POWER SUPPLY on #1)
002: Lighting + PSU#1 (protector tag Q0) POWER SUPPLY AC 230V
003: Q1 Q2 Q3 — 100A MCCB 3P
004: Q5 MCCB WITH MOTOR 3PHASE 100A | CT7..CT9 400/5A | SVA#3
005: SHIVA AMVAJ TEMPERATURE CONTROLLER TRB-900 CODE : 15B2 | 180-250 VAC
     MAX 5A | PV SV REL | PH N | 18 15 16 | + - | PSU#2 (tag Q5)
006: three 1P MCCB 125A
totall: MCCB WITH MOTOR (Q0), busbar L1 L2 L3 N PE
White background, IEC-style symbols, readable & organized — a base
drawing to hand to a graphics AI. Nothing added beyond the PDFs.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 2750, 1920
FB = '/usr/share/fonts/truetype/dejavu/'
def F(sz, bold=True): return ImageFont.truetype(FB + ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'), sz)

img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)
BLACK, GRAY = (10, 10, 10), (110, 110, 110)
INST = (60, 60, 170)
CTRL = (20, 125, 45)

def text(x, y, s, sz=18, bold=False, fill=BLACK, anchor='mm', knockout=False):
    f = F(sz, bold or sz >= 20)
    if knockout:
        bb = d.textbbox((0, 0), s, font=f)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        if anchor == 'mm': x0, y0 = x - w / 2 - 5, y - h / 2 - 4 - bb[1]
        elif anchor == 'lm': x0, y0 = x - 5, y - h / 2 - 4 - bb[1]
        d.rectangle([x0, y + -h / 2 - 4, x0 + w + 10, y + h / 2 + 4], fill='white')
    d.text((x, y), s, font=f, fill=fill, anchor=anchor)

def line(pts, w=4, fill=BLACK):
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        d.line([(ax, ay), (bx, by)], fill=fill, width=w)

def dashed(pts, w=2, fill=GRAY, dash=11, gap=7):
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        L = math.hypot(bx - ax, by - ay)
        if L == 0: continue
        ux, uy = (bx - ax) / L, (by - ay) / L
        s = 0
        while s < L:
            e = min(s + dash, L)
            d.line([(ax + ux * s, ay + uy * s), (ax + ux * e, ay + uy * e)], fill=fill, width=w)
            s = e + gap

def dot(x, y, r=5):
    d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

def mccb_pole(x, y0, y1, w=4):
    m = (y0 + y1) / 2
    line([(x, y0), (x, m - 17)], w); line([(x, m + 17), (x, y1)], w)
    dot(x, m - 17, 4); dot(x, m + 17, 4)
    d.line([(x - 2, m + 15), (x + 17, m - 15)], fill=BLACK, width=w)
    d.line([(x + 3, m - 4), (x + 11, m + 4)], fill=BLACK, width=3)
    d.line([(x + 11, m - 4), (x + 3, m + 4)], fill=BLACK, width=3)

def tie(xs, y):
    dashed([(xs[0], y), (xs[-1], y)], w=2, fill=BLACK, dash=6, gap=5)

def ct(x, y, r=22):
    d.ellipse([x - r, y - r, x + r, y + r], outline=BLACK, width=3)

def arrow_up(x, y):
    d.polygon([(x - 11, y + 18), (x + 11, y + 18), (x, y - 4)], fill=BLACK)

def arrow_down(x, y):
    d.polygon([(x - 11, y - 18), (x + 11, y - 18), (x, y + 4)], fill=BLACK)

# ======================= BUSBAR =======================
busY = {'L1': 120, 'L2': 155, 'L3': 190, 'N': 225, 'PE': 260}
for name, y in busY.items():
    line([(180, y), (2660, y)], w=6)
    text(160, y, name, 28, bold=True, anchor='rm')

# ======================= INPUT / Q0 =======================
phX = {'L1': 300, 'L2': 430, 'L3': 560}
nx, px = 620, 670
for x in phX.values(): line([(x, 1150), (x, 880)])
line([(nx, 1150), (nx, busY['N'])], w=3)
line([(px, 1150), (px, busY['PE'])], w=3)
for x in phX.values(): arrow_up(x, 1030)
for x in phX.values(): mccb_pole(x, 880, 720)
tie([300, 430, 560, 660], 800)
d.ellipse([680 - 20, 800 - 20, 680 + 20, 800 + 20], outline=BLACK, width=3)
text(680, 800, 'M', 24, bold=True)
text(780, 885, 'Q0', 26, bold=True, anchor='lm')
text(780, 920, 'MCCB WITH MOTOR', 21, anchor='lm')
text(780, 952, '3 PHASE  250A', 21, anchor='lm')
for ph, x in phX.items(): line([(x, 720), (x, busY[ph])])

# ======================= CT1..CT6 + SVA#1/#2 =======================
grp = [('CT1', 'L1', 420), ('CT2', 'L2', 420), ('CT3', 'L3', 420),
       ('CT4', 'L1', 560), ('CT5', 'L2', 560), ('CT6', 'L3', 560)]
for name, ph, y in grp:
    ct(phX[ph], y)
for name, ph, y in grp:
    text(phX[ph] - 36, y - 10, name, 21, bold=True, anchor='rm')
    text(phX[ph] - 36, y + 16, '400/5A', 18, anchor='rm')

def sva(x0, y0, x1, y1, power=False):
    d.rectangle([x0, y0, x1, y1], outline=BLACK, width=3)
    text((x0 + x1) / 2, y0 + 28, 'SVA', 24, bold=True)
    for k, t in enumerate(['I1', 'I1', 'I2', 'I2', 'I3', 'I3']):
        y = y0 + 62 + k * 25
        line([(x0, y), (x0 + 16, y)], w=2)
        text(x0 + 38, y, t, 19, anchor='lm')
    for k, t in enumerate(['N', 'L1', 'L2', 'L3']):
        y = y0 + 80 + k * 25
        line([(x1 - 16, y), (x1, y)], w=2)
        text(x1 - 38, y, t, 19, anchor='rm')
    if power:
        text((x0 + x1) / 2, y1 - 22, 'POWER SUPPLY', 17)

sva(800, 320, 1110, 510, power=True)
sva(800, 560, 1110, 750)
for i, (name, ph, y) in enumerate(grp[:3]):
    dashed([(phX[ph] + 24, y), (700, y), (700, 352 + i * 25), (800, 352 + i * 25)], w=2, fill=INST, dash=8, gap=6)
for i, (name, ph, y) in enumerate(grp[3:]):
    dashed([(phX[ph] + 24, y), (712, y), (712, 622 + i * 25), (800, 622 + i * 25)], w=2, fill=INST, dash=8, gap=6)
for base in (400, 640):
    for k, bn in enumerate(('L1', 'L2', 'L3', 'N')):
        yy = base + k * 25
        dashed([(1110, yy), (1158, yy), (1158, busY[bn])], w=2, fill=INST, dash=8, gap=6)
        dot(1158, busY[bn], 4)

# ======================= FEEDERS =======================
FY0, FY1, AY = 500, 580, 950
def feeder(cx, poles, phases, tag=None, amp=None):
    xs = [cx - 55, cx, cx + 55] if poles == 3 else [cx]
    for k, x in enumerate(xs):
        line([(x, busY[phases[k]]), (x, FY0)])
        dot(x, busY[phases[k]], 4)
        mccb_pole(x, FY0, FY1)
        line([(x, FY1), (x, AY)])
    if poles == 3: tie(xs, 540)
    for bn, off in (('N', -85 if poles == 3 else -45), ('PE', 85 if poles == 3 else 45)):
        x = cx + off
        line([(x, busY[bn]), (x, AY)], w=3)
        dot(x, busY[bn], 4)
    if poles == 3: line([(xs[0], AY), (xs[-1], AY)], w=3)
    arrow_down(cx, AY + 34)
    if tag: text(cx + 80, 465, tag, 26, bold=True, anchor='lm', knockout=True)
    if amp:
        text(cx, 1020, amp, 24, bold=True)
        text(cx, 1054, 'MCCB', 20)

feeder(1250, 1, ['L1'])
text(1250, 1022, 'Lighting', 24, bold=True)
# 002: second bridge symbol in series below the pole + small aux unit on branch
line([(1250, 700), (1250, 718)], w=4); dot(1250, 700, 4); dot(1250, 718, 4)
d.line([(1244, 716), (1268, 694)], fill=BLACK, width=4)
line([(1250, 718), (1250, AY)], w=4)
dashed([(1250, 660), (1330, 660)], w=2, fill=BLACK, dash=6, gap=5)
d.rectangle([1330, 636, 1420, 684], outline=BLACK, width=3)
feeder(1480, 3, ['L1', 'L2', 'L3'], tag='Q1', amp='100A')
feeder(1710, 3, ['L1', 'L2', 'L3'], tag='Q2', amp='100A')
feeder(1940, 3, ['L1', 'L2', 'L3'], tag='Q3', amp='100A')
feeder(2130, 1, ['L1'], amp='125A')
feeder(2260, 1, ['L2'], amp='125A')
feeder(2390, 1, ['L3'], amp='125A')

q5x = 2570
xs5 = [q5x - 80, q5x, q5x + 80]
for k, x in enumerate(xs5):
    line([(x, busY[['L1','L2','L3'][k]]), (x, FY0)])
    dot(x, busY[['L1','L2','L3'][k]], 4)
    mccb_pole(x, FY0, FY1)
    line([(x, FY1), (x, AY)])
tie(xs5, 540)
x = q5x - 120
line([(x, busY['N']), (x, AY)], w=3)
dot(x, busY['N'], 4)
line([(xs5[0], AY), (xs5[-1], AY)], w=3)
arrow_down(q5x, AY + 34)
text(q5x + 104, 465, 'Q5', 26, bold=True, anchor='lm', knockout=True)
text(q5x, 1022, 'MCCB WITH MOTOR', 21, bold=True)
text(q5x, 1058, '3PHASE  100A', 21, bold=True)
d.ellipse([2300 - 20, 540 - 20, 2300 + 20, 540 + 20], outline=BLACK, width=3)
text(2300, 540, 'M', 24, bold=True)
dashed([(2320, 540), (2490, 540)], w=2, fill=BLACK, dash=5, gap=4)

# ======================= CT7..CT9 + SVA#3 =======================
ctsz = [('CT7', 2490, 760), ('CT8', 2570, 760), ('CT9', 2650, 760)]
for name, x, y in ctsz:
    ct(x, y)
sva(1700, 1090, 2040, 1280)
for i, (name, x, y) in enumerate(ctsz):
    dashed([(x + 20, y + 22), (x + 20, 1012), (1650, 1012), (1650, 1152 + i * 25), (1700, 1152 + i * 25)], w=2, fill=INST, dash=8, gap=6)
for i, (name, x, y) in enumerate(ctsz):
    text(x, 800 + i * 52, name, 21, bold=True, knockout=True)
    text(x, 826 + i * 52, '400/5A', 18, knockout=True)
for k, bn in enumerate(('L1', 'L2', 'L3', 'N')):
    yy = 1170 + 25 * k
    dashed([(2660, busY[bn]), (2702, busY[bn]), (2702, yy), (2040, yy)], w=2, fill=INST, dash=8, gap=6)

# ======================= CONTROL (002 + 005) =======================
for tx, ty in ((350, 1340), (350, 1500)):
    dot(tx, busY['L1'], 4)
    dashed([(tx, busY['L1']), (tx, ty)], w=2, fill=INST, dash=9, gap=6)
# PSU #1: protector left of box, wired into box left edge
mccb_pole(350, 1340, 1410, w=3)
text(310, 1375, 'Q0', 23, bold=True, anchor='rm')
line([(350, 1410), (350, 1375), (430, 1375)], w=3)
d.rectangle([430, 1320, 750, 1430], outline=BLACK, width=3)
text(590, 1358, 'POWER SUPPLY', 21)
text(590, 1396, 'AC 230V', 25, bold=True)
# PSU #2: protector left of box (same column), wired into box left edge
mccb_pole(350, 1500, 1570, w=3)
text(310, 1535, 'Q5', 23, bold=True, anchor='rm')
line([(350, 1570), (350, 1590), (430, 1590)], w=3)
d.rectangle([430, 1510, 750, 1620], outline=BLACK, width=3)
text(590, 1548, 'POWER SUPPLY', 21)
text(590, 1586, 'AC 230V', 25, bold=True)
PHy, Ny = 1460, 1660
line([(900, PHy), (2330, PHy)], w=3)
line([(900, Ny), (2330, Ny)], w=3)
line([(750, 1360), (820, 1360), (820, PHy)], w=3); dot(820, PHy)
line([(750, 1400), (800, 1400), (800, Ny)], w=3); dot(800, Ny)
line([(750, 1550), (830, 1550), (830, PHy)], w=3); dot(830, PHy)
line([(750, 1590), (810, 1590), (810, Ny)], w=3); dot(810, Ny)

# ---- TRB-900 ----
T = (1500, 1290, 2150, 1840)
d.rectangle(T, outline=BLACK, width=4)
mx = (T[0] + T[2]) // 2
text(mx, 1332, 'SHIVA AMVAJ', 22, bold=True)
text(mx, 1366, 'TEMPERATURE CONTROLLER', 19)
text(mx, 1410, 'TRB-900', 30, bold=True)
text(mx, 1444, 'CODE : 15B2', 18)
line([(1500, PHy), (1560, PHy)], w=3)
text(1580, PHy, 'PH', 23, bold=True, anchor='lm')
line([(1500, Ny), (1560, Ny)], w=3)
text(1580, Ny, 'N', 23, bold=True, anchor='lm')
d.rectangle([1600, 1480, 1850, 1545], outline=BLACK, width=2)
text(1635, 1512, 'PV', 20, bold=True, anchor='lm')
d.rectangle([1600, 1560, 1850, 1625], outline=BLACK, width=2)
text(1635, 1592, 'SV', 20, bold=True, anchor='lm')
d.ellipse([1955 - 13, 1497, 1955 + 13, 1523], outline=BLACK, width=3)
text(2010, 1510, 'REL', 20, bold=True, anchor='lm')
text(1955, 1580, '180-250 VAC', 19)
text(1955, 1615, 'MAX 5A', 21, bold=True)
term = [('+', 1340), ('18', 1430), ('15', 1520), ('16', 1610), ('-', 1700)]
for t, y in term:
    line([(2140, y), (2150, y)], w=3)
    text(2172, y, t, 24, bold=True, anchor='lm')
coilx = 2330
line([(2150, 1430), (coilx, 1430)], w=3)
line([(2150, 1520), (2250, 1520), (2250, 1430)], w=3); dot(2250, 1430)
d.ellipse([coilx - 31, 1535 - 31, coilx + 31, 1535 + 31], outline=BLACK, width=3)
for k in range(3):
    d.arc([coilx - 22 + k * 15, 1525, coilx - 4 + k * 15, 1545], 200, 340, fill=BLACK, width=3)
line([(coilx, 1430), (coilx, 1504)], w=3)
line([(coilx, 1566), (coilx, Ny)], w=3); dot(coilx, Ny)
line([(2150, 1610), (2190, 1610), (2190, Ny)], w=3); dot(2190, Ny)
dashed([(coilx, 1430), (coilx, 700), (2300, 700), (2300, 562)], w=3, fill=CTRL, dash=12, gap=8)

img.save('/home/user/Bargh/render/schematic_master.png')
print('saved', img.size)
