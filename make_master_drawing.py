# -*- coding: utf-8 -*-
"""
Bargh — Master power & control drawing (readable re-typesetting of totall.pdf + 001..006).
All tags, ratings, wire numbers, terminal markings and conductor sizes are exactly as
printed in the source PDFs (per power_circuit.md). Junction dots only where the source
draws a connection.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

W, H = 486.0, 216.0
DPI = 240
fig = plt.figure(figsize=(W / 16.6, H / 16.6), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
ax.add_patch(Rectangle((0, 0), W, H, fc='white', ec='none', zorder=0))

C = dict(R='#d8121c', S='#e8c400', T='#8f9296', N='#25c2e8', E='#22b14c',
         ct='#c8102e', ctrl='#101010', mag='#c724b1', red2='#e0301e',
         gray='#9aa0a8', green2='#2e9e44', cyan='#1ba8cc', cyanec='#25c2e8',
         note='#4a5a6a')
TERMSUB = ['11₁', '11₂', '12₁', '12₂', '13₁', '13₂']
BB = dict(fc='white', ec='none', pad=0.6)

def line(x1, y1, x2, y2, c=C['ctrl'], lw=1.15):
    if lw <= 0: return
    ax.plot([x1, x2], [y1, y2], color=c, lw=lw, solid_capstyle='round', zorder=3)
def poly(pts, c=C['ctrl'], lw=1.15):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=c, lw=lw, solid_capstyle='round', solid_joinstyle='round', zorder=3)
def dot(x, y, c=C['ctrl'], r=0.5):
    ax.add_patch(Circle((x, y), r, color=c, zorder=5))
def tapdot(x, y, c, r=1.05):
    ax.add_patch(Circle((x, y), r, color=c, zorder=5))
def term(x, y, c='#555', r=0.62):
    ax.add_patch(Circle((x, y), r, fc='white', ec=c, lw=0.8, zorder=5))
def txt(x, y, s, size=6.4, color='#111', ha='left', va='center', style='normal',
        weight='normal', rot=0, bbox=False):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, style=style,
            weight=weight, rotation=rot, zorder=6,
            bbox=(dict(**BB) if bbox else None))
def sz(x, y, s, rot=0, size=6.4, color='#111', bbox=False):
    txt(x, y, s, size=size, style='italic', weight='bold', rot=rot, color=color, bbox=bbox)
def wn(x, y, s, size=6.4, ha='left', bbox=True):
    txt(x, y, s, size=size, color=C['mag'], weight='bold', ha=ha, bbox=bbox)
def note(x, y, s, size=5.4, ha='left', rot=0):
    txt(x, y, s, size=size, ha=ha, style='italic', color=C['note'], rot=rot)
def _arw(x1, y1, x2, y2, c):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1), zorder=3,
                arrowprops=dict(arrowstyle='-|>', color=c, lw=1.0, mutation_scale=7))
def arrD(x, y1, y2, c): _arw(x, y1, x, y2, c)
def arrU(x, y1, y2, c): _arw(x, y1, x, y2, c)
def arrR(x1, x2, y, c): _arw(x1, y, x2, y, c)
def arrL(x1, x2, y, c): _arw(x1, y, x2, y, c)

def zone(x, y, w, h, tag, tab_dy=0.0):
    ax.add_patch(Rectangle((x, y), w, h, fc='none', ec='#c3cdd7', lw=1.0,
                           ls=(0, (7, 4)), zorder=1))
    tw = 21.5
    ax.add_patch(Rectangle((x + w - tw, y + h - 5.1 - tab_dy), tw, 5.1, fc='#0d2b45', ec='none', zorder=2))
    txt(x + w - tw / 2, y + h - 2.55 - tab_dy, tag, size=6.4, color='white', ha='center', va='center', weight='bold')

def ct_sym(x, y, name, lab_on_left=True):
    ax.add_patch(Rectangle((x - 2.6, y - 1.9), 1.5, 3.8, color=C['ct'], zorder=5))
    ax.add_patch(Rectangle((x + 1.1, y - 1.9), 1.5, 3.8, color=C['ct'], zorder=5))
    txt(x - 2.9, y + 2.6, 'P1', size=5.0, ha='center')
    txt(x - 2.9, y - 3.0, 'P2', size=5.0, ha='center')
    ha = 'right' if lab_on_left else 'left'
    dx = -4.3 if lab_on_left else 5.0
    txt(x + dx, y + 1.7, name, size=5.8, ha=ha, weight='bold', bbox=True)
    txt(x + dx, y + 0.1, '400/5A', size=5.4, ha=ha, bbox=True)
    txt(x + dx, y - 1.4, 'SVA', size=5.4, ha=ha, bbox=True)

def mccb(x, y, poles=3, sp=7.0, motor=False, cphase=None, lw=1.35):
    top = y + 6.0; bl = y + 3.0; trip_bot = y - 3.1
    for i in range(poles):
        px = x + i * sp
        cc = (cphase[i] if cphase else C['ctrl'])
        line(px, top, px, bl, cc, lw)
        term(px, bl, '#333', 0.55)
        ax.plot([px, px + 2.0], [bl, bl + 2.3], color='#111', lw=1.1, zorder=5)
        dot(px + 2.0, bl + 2.3, '#111', 0.42)
        line(px, trip_bot, px, y - 6.0, cc, lw)
    ax.add_patch(Rectangle((x - 2.6, trip_bot), poles * sp, 3.1, fc='white', ec='#111', lw=1.0, zorder=4))
    for i in range(poles):
        px = x + i * sp
        poly([(px - 1.05, trip_bot), (px - 1.05, trip_bot + 1.05),
              (px + 0.1, trip_bot + 1.05), (px + 0.1, trip_bot + 1.9)], '#111', 0.85)
        txt(px + 1.3, trip_bot + 0.95, 'I>', size=5.5, weight='bold')
    if motor:
        ax.add_patch(Circle((x - 5.6, trip_bot + 1.55), 1.6, fc='white', ec='#111', lw=1.0, zorder=5))
        txt(x - 5.6, trip_bot + 1.55, 'M', size=5.7, ha='center', va='center', weight='bold')
        line(x - 4.0, trip_bot + 1.55, x - 2.6, trip_bot + 1.55, '#111', 0.9)

def shunt(x, y, to_right=2.6, y_end=None):
    ax.add_patch(Rectangle((x, y), 2.4, 2.4, fc='white', ec='#111', lw=0.95, zorder=5))
    ax.plot([x, x + 2.4], [y, y + 2.4], color='#111', lw=0.95, zorder=6)
    line(x + 2.4, y + 1.2, x + 2.4 + to_right, y + 1.2, '#111', 0.9)

def fuse(x, y, lab=None, lab2=None, col=None):
    col = col or C['red2']
    ax.add_patch(Rectangle((x - 2.6, y - 0.95), 5.2, 1.9, fc='white', ec=col, lw=1.2, zorder=5))
    ax.plot([x - 3.1, x + 3.1], [y - 1.6, y + 1.6], color=col, lw=1.1, zorder=6)
    if lab:  txt(x, y + 2.5, lab, size=5.8, ha='center', color=C['green2'], weight='bold')
    if lab2: txt(x, y - 2.9, lab2, size=5.5, ha='center', color=C['green2'])

def switch1(x, y, name, up=True):
    term(x, y, '#111', 0.6)
    line(x, y, x, y + 1.9, '#111', 1.05)
    if up:
        ax.plot([x, x + 2.1], [y + 1.9, y + 3.8], color='#111', lw=1.15, zorder=5)
        dot(x + 2.1, y + 3.8, '#111', 0.5)
    else:
        ax.plot([x, x - 2.1], [y + 1.9, y + 3.8], color='#111', lw=1.15, zorder=5)
        dot(x - 2.1, y + 3.8, '#111', 0.5)
    txt(x, y + 5.2, name, size=6.0, ha='center', color=C['mag'], weight='bold')

def aux_box(x, y, name, w=9.5, h=8.5, t1='13', t2='14'):
    ax.add_patch(Rectangle((x, y), w, h, fc='white', ec='#111', lw=1.05, zorder=5))
    txt(x + 0.5, y + h - 1.3, name, size=5.5, weight='bold', style='italic')
    xm = x + w * 0.58
    line(xm, y + h, xm, y + h - 1.7, '#111', 1.05)
    line(xm, y + 1.7, xm, y, '#111', 1.05)
    ax.plot([xm, xm + 1.6], [y + h - 1.7, y + h - 3.0], color='#111', lw=1.1, zorder=6)
    txt(xm + 1.9, y + h - 2.1, t1, size=5.4)
    txt(xm + 1.9, y + 1.7, t2, size=5.4)
    return xm

def meter(x, y, w, h, title, left_terms, right_terms=None, right_names=None,
          ys_left=None, ys_right=None):
    ax.add_patch(Rectangle((x, y), w, h, fc='#f4fdff', ec=C['cyanec'], lw=1.2, zorder=4))
    txt(x + w / 2, y + h + 1.7, title, size=7.2, ha='center', weight='bold', color='#0a7fae', bbox=True)
    n = len(left_terms)
    ys = ys_left if ys_left else [y + h - 2.5 - i * ((h - 5.0) / (n - 1)) for i in range(n)]
    for i, lab in enumerate(left_terms):
        term(x, ys[i], '#333', 0.7)
        txt(x + 1.35, ys[i] + 0.62, lab, size=5.4)
        txt(x + 1.2, ys[i] - 1.15, TERMSUB[i], size=4.1, color=C['mag'])
    yr = None
    if right_terms:
        m = len(right_terms)
        yr = ys_right if ys_right else [y + h - 2.5 - i * ((h - 5.0) / (m - 1)) for i in range(m)]
        for i, (lab, cc) in enumerate(right_terms):
            term(x + w, yr[i], '#333', 0.7)
            if cc:
                line(x + w + 0.7, yr[i], x + w + 5.0, yr[i], cc, 1.0)
                dot(x + w + 5.0, yr[i], cc, 0.65)
                wn(x + w + 6.0, yr[i], lab, size=5.9)
            else:
                wn(x + w + 2.0, yr[i], lab, size=5.9)
        if right_names:
            for i, nm in enumerate(right_names):
                if nm: txt(x + w - 2.2, yr[i] + 0.8, nm, size=4.8, ha='right', color='#345')
    return ys, yr

# ================= TITLE =================
ax.add_patch(Rectangle((8, H - 15.5), W - 16, 11.0, fc='#0d2b45', ec='none', zorder=1))
txt(W / 2, H - 7.3, 'MASTER POWER & CONTROL DRAWING — ONE FULLY CONNECTED COMPOSITE (per totall.pdf)',
    size=13.0, color='white', ha='center', weight='bold')
txt(W / 2, H - 12.3,
    'every device tag, rating, wire number, terminal marking and conductor size exactly as printed on the source  •  all runs wired end-to-end  •  junction dots only where the source draws a connection',
    size=7.0, color='#cfe3ff', ha='center')

# ================= MAIN BUS =================
by = dict(R=196, S=191.5, T=187, N=182.5, E=178)
BX1 = 472
for k in ['R', 'S', 'T', 'N', 'E']:
    line(16, by[k], BX1, by[k], C[k], 2.0)
for nm, k in [('L1', 'R'), ('L2', 'S'), ('L3', 'T'), ('N', 'N'), ('PE', 'E')]:
    txt(14.4, by[k], nm, size=7.5, ha='right', weight='bold', style='italic')
    sz(24, by[k] + 1.35, '25*5Mm² CU', size=6.9)
txt(150, 198.6, 'INCOMING SUPPLY — main five-conductor bus', size=6.5,
    weight='bold', color='#234', style='italic')

# =====================================================================
# ZONE 001
# =====================================================================
DX = dict(R=52, S=60, T=68, N=76, E=84)
for k in ['R', 'S', 'T', 'N', 'E']:
    tapdot(DX[k], by[k], C[k])
    line(DX[k], by[k], DX[k], 11.5, C[k], 1.4)
    txt(DX[k], 9.0, k, size=6.4, ha='center', color=C['green2'], weight='bold')
def ct_bank(cts, mx, mys, nums, lab_x):
    for i, (nm, dxx, cty) in enumerate(cts):
        ct_sym(dxx, cty, nm, lab_on_left=(i % 2 == 0))
        for j in (0, 1):
            k = i * 2 + j
            yy = mys[k]
            line(dxx + 2.7, yy, mx - 0.8, yy, '#111', 1.0)
            wn(lab_x, yy + 1.0, str(nums[k]), size=5.8)
            sz(lab_x + 2.4, yy + 1.0, '1*2.5 mm²', size=5.2)

DLY, _ = meter(128, 145, 34, 27.5, 'DATA LOGGER', ['I1+', 'I1-', 'I2+', 'I2-', 'I3+', 'I3-'],
               ys_left=[169.3, 166.5, 164.5, 161.7, 159.7, 156.9])
txt(126.4, 158.75, 'POWER SUPPLY', size=5.1, rot=90, ha='center', color='#345')
ct_bank([('CT1', 52, 167.9), ('CT2', 60, 163.1), ('CT3', 68, 158.3)], 128,
        DLY, [17, 18, 19, 20, 21, 22], 76)
K1Y, _ = meter(128, 112, 34, 30, 'KWH1', ['I1+', 'I1-', 'I2+', 'I2-', 'I3+', 'I3-'],
               ys_left=[139.3, 136.5, 134.5, 131.7, 129.7, 126.9])
ct_bank([('CT4', 52, 137.9), ('CT5', 60, 133.1), ('CT6', 68, 128.3)], 128,
        K1Y, [11, 12, 13, 14, 15, 16], 76)
mccb(52, 97, 3, 8, motor=True, cphase=[C['R'], C['S'], C['T']])
txt(41.5, 101.5, 'Q0', size=7.6, ha='right', weight='bold')
txt(41.5, 98.9, 'MCCB WITH MOTOR', size=6.1, ha='right')
txt(41.5, 96.4, '3 PHASE 250A', size=6.1, ha='right')
for i, k in enumerate(['R', 'S', 'T']):
    sz(DX[k] + 4.6, 90, '25*5Mm² CU', rot=90, size=6.2, bbox=True)
# ---- F.KWH1&SIG 6A 3PHASE Type:C (breakers below bus, feeds meter voltage taps) ----
FXx = [216, 223.5, 231]
for i, k in enumerate(['R', 'S', 'T']):
    tapdot(FXx[i], by[k], C[k])
    line(FXx[i], by[k], FXx[i], 183.2, C[k], 1.2)
    sz(FXx[i] - 1.6, 190.6, '1*1.5mm²', rot=90, size=5.6, bbox=True)
ax.plot([FXx[0] - 2.3, FXx[2] + 2.3], [181.6, 181.6], color=C['mag'], lw=1.9, zorder=5)
for px in FXx:
    term(px, 182.7, C['mag'], 0.55); term(px, 180.5, C['mag'], 0.55)
for i, px in enumerate(FXx):
    wn(px + 1.0, 185.2, str(35 + i), size=5.9)
    line(px, 180.5, px, 118.5, '#111', 1.1)
    wn(px + 1.0, 177.0, str(38 + i), size=5.9)
    sz(px - 1.7, 132, '1*2.5mm²', rot=90, size=5.4, bbox=True)
txt(246.5, 166.6, 'F.KWH1&SIG', size=6.6, weight='bold')
txt(246.5, 164.1, '6A 3PHASE', size=5.9)
txt(246.5, 161.7, 'Type:C', size=5.9)
tapdot(227.6, by['N'], C['N'])
line(227.6, by['N'], 227.6, 118.5, '#222', 0.95)
wn(228.8, 172.6, '41', size=5.7)
# ---- meter taps: nets exactly as drawn in the master ----
def _seat(mx, yy, num, nm=None):
    term(mx, yy, '#333', 0.7)
    if nm: txt(mx - 2.2, yy + 0.8, nm, size=4.8, ha='right', color='#345')
    wn(mx + 1.6, yy + 1.15, num, size=5.7)
for yy, num, nm in [(170, '23', None), (165.5, '24', None), (161, '25', 'N'), (156.5, '26', 'L1'),
                    (152, '27', 'L2'), (147.5, '28', 'L3'), (140, '29', 'N'), (135.5, '30', 'L1'),
                    (131, '31', 'L2'), (126.5, '32', 'L3'), (122, '33', None), (117.5, '34', None)]:
    _seat(162, yy, num, nm)
# N net: N bus -> 23 -> 25 -> 29 (one cyan conductor, as master draws)
tapdot(171, by['N'], C['N'])
line(171, by['N'], 171, 140, C['N'], 1.05)
line(162.7, 161, 171, 161, C['N'], 1.05)
line(162.7, 140, 171, 140, C['N'], 1.05)
line(162.7, 170, 167.6, 170, C['N'], 1.05)
line(167.6, 170, 167.6, 161, C['N'], 1.05)
dot(167.6, 161, C['N'], 0.55)
# L net: 24 -> down -> 26 -> drop 38 ; 30 -> drop 38
line(162.7, 165.5, 175.6, 165.5, C['R'], 1.0)
line(175.6, 165.5, 175.6, 156.5, C['R'], 1.0)
line(162.7, 156.5, 216, 156.5, C['R'], 1.0)
dot(175.6, 156.5, C['R'], 0.5)
line(162.7, 135.5, 216, 135.5, C['R'], 1.0)
# S net: 27 & 31 -> drop 39
line(162.7, 152, 223.5, 152, C['S'], 1.0)
line(162.7, 131, 223.5, 131, C['S'], 1.0)
# T net: 28 & 32 -> drop 40
line(162.7, 147.5, 231, 147.5, '#8f9296', 1.0)
line(162.7, 126.5, 231, 126.5, '#8f9296', 1.0)
for dxx2, dyy2, dcc2 in [(216, 156.5, C['R']), (223.5, 152, C['S']), (231, 147.5, C['T']),
                         (216, 135.5, C['R']), (223.5, 131, C['S']), (231, 126.5, C['T'])]:
    dot(dxx2, dyy2, dcc2, 0.55)
# 33 / 34 : terminal marks only — master draws no conductor there
SBx, SBy, SBw, SBh = 209, 104, 34, 14.5
ax.add_patch(Rectangle((SBx, SBy), SBw, SBh, fc='white', ec=C['cyanec'], lw=1.15, zorder=4))
for i, (px, cc) in enumerate(zip(FXx, [C['R'], C['S'], C['T']])):
    txt(px - 0.2, SBy + SBh - 2.0, ['R H1', 'S H2', 'T H3'][i], size=5.7, ha='center', color=C['green2'], weight='bold')
    ax.plot([px, px], [111.6, 108.2], color=cc, lw=1.1, zorder=6, solid_capstyle='round')
    ax.plot([px - 0.8, px + 0.8], [109.9, 109.9], color=cc, lw=1.1, zorder=6)
    wn(px + 1.5, 106.0, str(42 + i), size=5.9, ha='left')
for px in FXx:
    ax.plot([px, px], [108.2, 104.0], color=C['cyan'], lw=1.0, zorder=6)
line(216, 104, 243, 104, C['cyan'], 1.0)
line(243, 104, 243, by['N'], C['cyan'], 1.0)
dot(243, by['N'], C['cyan'], 0.6)

# =====================================================================
# ZONE 002
# =====================================================================
def ckt(y, tapk, w1, fz, w2, x_end, col):
    tx = DX[tapk]
    dot(tx, y, C[tapk], 0.6)
    line(tx, y, tx + 1.2, y, col, 1.2)
    wn(tx + 2.2, y + 1.3, w1, size=6.1)
    if fz:
        line(tx + 1.2, y, 107 - 3.1, y, col, 1.2)
        fuse(107, y, fz, col=C['mag'])
        line(107 + 3.1, y, x_end, y, col, 1.2)
    else:
        line(tx + 1.2, y, x_end, y, col, 1.2)
    if w2: wn(x_end - 4.4, y + 1.3, w2, size=6.1)
    sz(87, y + 1.4, '1*1.5mm²', size=5.9, bbox=True)
ckt(74, 'R', '9', 'F.CONTROL', '10', 222.7, '#111')
term(222.7, 62, '#111', 0.65)
line(222.7, 74, 222.7, 62, '#111', 1.05)
ckt(68.5, 'S', '7', 'F.SOCKET', '8', 112.4, C['red2'])
dot(112.4, 68.5, C['red2'], 0.95)
txt(114.2, 70.1, 'S0', size=5.6, ha='left', color=C['green2'], weight='bold', style='italic')
ckt(63, 'T', '6', 'F.LIGHTING', '5', 186.5, C['red2'])
tx = DX['N']; y = 57.5
dot(tx, y, C['N'], 0.6); line(tx, y, 118, y, C['cyan'], 1.2)
wn(97, y + 1.3, '1', size=6.1); sz(103, y + 1.4, '1*1.5mm²', size=5.9, bbox=True)
switch1(122, 57.5, '')
txt(118.8, 62.0, 'S1', size=6.0, ha='right', color=C['mag'], weight='bold')
yb = 51.5
line(115.5, y, 115.5, yb, C['cyan'], 1.0)
line(115.5, yb, 127.0, yb, C['cyan'], 1.0)
switch1(129.5, yb, '')
txt(129.5, 49.4, 'S2', size=6.0, ha='center', color=C['mag'], weight='bold')
wn(124.0, yb + 0.9, '2', size=5.4); wn(133.6, yb + 0.9, '3', size=5.4)
line(131.6, yb + 3.8, 139.5, yb + 3.8, C['cyan'], 1.0)
line(139.5, yb + 3.8, 139.5, y, C['cyan'], 1.0)
line(122, y, 139.5, y, C['cyan'], 1.15)
wn(145, y + 1.3, '4', size=6.1)
line(139.5, y, 152, y, C['cyan'], 1.15)
ax.add_patch(Rectangle((152, y - 1.9), 4.2, 3.8, fc=C['red2'], ec='#111', lw=0.85, zorder=5))
ax.add_patch(Rectangle((156.2, y - 1.9), 18.5, 3.8, fc='white', ec=C['red2'], lw=1.1, zorder=5))
txt(165.4, y, 'Lighting', size=6.2, ha='center', color=C['green2'], weight='bold')
poly([(174.7, y), (181.5, y), (181.5, 63), (186.5, 63)], C['red2'], 1.05)
dot(181.5, 63, C['red2'], 0.6)
# control string — exactly as the master draws it
xmK = aux_box(226.4, 66.5, 'KWH1')
line(231.9, 75, 231.9, 78.5, '#111', 1.05)
line(231.9, 78.5, 243.3, 78.5, '#111', 1.05)
line(243.3, 78.5, 243.3, 74.4, '#111', 1.05)
term(243.3, 74.4, '#111', 0.6)
ax.plot([243.3, 245.4], [74.4, 72.6], color='#111', lw=1.05, zorder=5)
dot(245.4, 72.6, '#111', 0.5)
line(243.3, 72.6, 243.3, 62, '#111', 1.05)
line(231.9, 66.5, 231.9, 62, '#111', 1.05)
txt(241.7, 76.9, 'S1', size=6.0, ha='right', color=C['mag'], weight='bold')
wn(246.4, 75.8, '23', size=5.4)
wn(244.7, 63.6, '24', size=5.4)
txt(230.3, 79.2, 'X.KWH1 11', size=5.0, ha='right', style='italic')
txt(230.3, 63.6, 'X.KWH1 12', size=5.0, ha='right', style='italic')
QBx, QBy, QBw, QBh = 218, 40, 32, 22
ax.add_patch(Rectangle((QBx, QBy), QBw, QBh, fc='white', ec='#111', lw=1.2, zorder=4))
txt(217.2, 64.6, 'Q0', size=6.9, weight='bold')
txt(220.4, 49.6, 'AC 230V', size=4.6, bbox=True); txt(220.4, 47.6, 'POWER SUPPLY', size=4.2, bbox=True)
shunt(222.7, 51, to_right=0.0)
txt(221.2, 58.2, 'P1', size=5.4, ha='right'); txt(221.2, 43.6, 'P2', size=5.4, ha='right')
term(231.9, 62, '#111', 0.65); txt(231.9, 60.2, 'N', size=5.6, weight='bold', ha='center')
term(243.3, 62, '#111', 0.65); txt(243.3, 60.2, 'O', size=5.6, weight='bold', ha='center')
line(222.7, 40, 222.7, 13.5, '#111', 1.05)
sz(224.2, 26.5, '1*1.5mm²', rot=90, size=5.2)
line(222.7, 13.5, 272, 13.5, '#111', 1.05)
arrR(272, 275.5, 13.5, '#111')
txt(274.0, 15.3, 'N0', size=6.7, style='italic', weight='bold')

# =====================================================================
# ZONE 003 — Q1 Q2 Q3
# =====================================================================
for i, (nm, f0) in enumerate([('Q1', 297), ('Q2', 321), ('Q3', 345)]):
    pxs = [f0 - 4, f0 + 2, f0 + 8]
    for j, k in enumerate(['R', 'S', 'T']):
        tapdot(pxs[j], by[k], C[k]); line(pxs[j], by[k], pxs[j], 141.0, C[k], 1.45)
    line(f0 + 13, by['N'], f0 + 13, 122, C['N'], 1.1); tapdot(f0 + 13, by['N'], C['N'])
    line(f0 + 16.5, by['E'], f0 + 16.5, 122, C['E'], 1.1); tapdot(f0 + 16.5, by['E'], C['E'])
    shunt(pxs[0] - 7.4, 133.5)
    mccb(pxs[0], 136, 3, 6, cphase=[C['R'], C['S'], C['T']])
    txt(f0 + 4, 146.5, f'{nm} · MCCB · 3PHASE · 100A', size=6.1, ha='center', weight='bold', bbox=True)
    for j, k in enumerate(['R', 'S', 'T']):
        line(pxs[j], 127.5, pxs[j], 97.5, C[k], 1.45)
        sz(pxs[j] - 2.0, 110, '20*5Mm² CU', rot=90, size=6.1, bbox=True)
        arrD(pxs[j], 97.5, 93.8, C[k])
        txt(pxs[j] + 1.1, 94.8, ['R', 'S', 'T'][j], size=6.2, color=C['green2'], weight='bold')
    for px, kk, lab in [(f0 + 13, 'N', 'N'), (f0 + 16.5, 'E', 'E')]:
        line(px, 122, px, 97.5, C[kk], 1.1); arrD(px, 97.5, 93.8, C[kk])
        txt(px + 1.1, 94.8, lab, size=6.2, color=C['green2'], weight='bold')

# =====================================================================
# ZONE 004 — Q5 · CT7–9 · KWH2 · MCB · F.CONTROL
# =====================================================================
qx = [386, 392, 398]
for j, k in enumerate(['R', 'S', 'T']):
    tapdot(qx[j], by[k], C[k]); line(qx[j], by[k], qx[j], 142.5, C[k], 1.4)
mccb(qx[0], 136, 3, 6, motor=True, cphase=[C['R'], C['S'], C['T']])
txt(375.5, 137.6, 'Q5 · MCCB WITH MOTOR · 3PHASE 100A', size=5.3, ha='left', weight='bold', bbox=True)
for j in range(3):
    wn(qx[j] + 1.1, 150.4, str(47 + j), size=5.9)
    sz(qx[j] - 2.0, 147.3, '1*2.5mm²', rot=90, size=5.5, bbox=True)
for j, k in enumerate(['R', 'S', 'T']):
    line(qx[j], 129.5, qx[j], 124.0, C[k], 1.4)
    wn(qx[j] + 1.1, 124.9, str(50 + j), size=5.9)
line(404, by['E'], 404, 112, C['gray'], 0.9); tapdot(404, by['E'], C['E'], 0.7)
line(407.5, by['E'], 407.5, 112, C['gray'], 0.9); tapdot(407.5, by['E'], C['E'], 0.7)
txt(402.9, 112.3, '53', size=5.5, color='#667', ha='right', bbox=True)
txt(406.4, 112.3, '54', size=5.5, color='#667', ha='right', bbox=True)
arrD(404, 112, 108.5, C['gray']); arrD(407.5, 112, 108.5, C['gray'])
K2Y, _ = meter(414, 100, 30, 34, 'KWH2', ['I1+', 'I1-', 'I2+', 'I2-', 'I3+', 'I3-'],
               ys_left=[131.5, 125.7, 119.9, 114.1, 108.3, 102.5])
K2RY = [131.5, 125.7, 119.9, 114.1]
for i, (nm, dxx, cty) in enumerate([('CT7', 386, 128.6), ('CT8', 392, 117.8), ('CT9', 398, 107)]):
    for xx in (dxx - 2.6, dxx + 1.1):
        ax.add_patch(Rectangle((xx, cty - 1.9), 1.5, 3.8, color=C['ct'], zorder=5))
    txt(374.2, cty, nm, size=5.2, weight='bold')
    txt(dxx - 3.2, cty + 0.4, 'P1', size=4.4, ha='right')
    txt(dxx - 3.2, cty - 2.0, 'P2', size=4.4, ha='right')
    for j in (0, 1):
        k = i * 2 + j
        yy = K2Y[k]
        line(dxx + 2.7, yy, 413.2, yy, '#111', 0.95)
        wn(399.4, yy + 1.0, str(55 + k), size=5.5)
        sz(401.6, yy + 1.0, '1*2.5 mm²', size=4.9)
txt(374.2, 113.0, '400/5A · SVA', size=5.0, bbox=True)
for yy, num in [(106.6, '61'), (100.9, '62')]:
    line(404.7, yy, 413.1, yy, '#111', 1.0)
    arrL(400.7, 404.7, yy, '#111')
    wn(405.5, yy - 1.9, num, size=4.6, ha='left')
for j, (px, k) in enumerate([(420, 'R'), (427, 'S'), (434, 'T')]):
    tapdot(px, by[k], C[k]); line(px, by[k], px, 159.0, C[k], 1.1)
ax.add_patch(Rectangle((417.5, 153.5), 20, 4.4, fc='white', ec='#111', lw=1.05, zorder=5))
for j, px in enumerate([420, 427, 434]):
    wn(px, 161.0, str(64 + j), size=5.7, ha='center')
    line(px, 153.5, px, 127.0, '#111', 1.0)
    txt(px + 1.0, 151.8, str(67 + j), size=5.6, color=C['mag'], weight='bold')
txt(439.5, 165.0, 'MCB · 3PHASE 16A ·', size=5.5, weight='bold')
txt(439.5, 162.4, 'Type:C', size=5.5, weight='bold')
for j, (px, nm) in enumerate([(420, 'L1'), (427, 'L2'), (434, 'L3')]):
    ty = K2RY[j + 1]
    line(px, 127.0, px, ty, '#111', 1.0)
    line(px, ty, 444.2, ty, '#111', 1.0)
    term(444, ty, '#333', 0.6)
    txt(442.9, ty + 0.95, nm, size=5.2, ha='right', bbox=True)
tapdot(416, by['N'], C['N']); poly([(416, by['N']), (416, 148), (447, 148), (447, K2RY[0]), (444.7, K2RY[0])], C['N'], 1.0)
wn(418.5, 149.3, '63', size=5.7)
txt(442.9, K2RY[0] + 0.95, 'N', size=5.2, ha='right', bbox=True)
term(444, K2RY[0], '#333', 0.6)
sz(448.6, 140, '1*2.5mm²', rot=90, size=5.1)
# F.CONTROL 6A/32A 1PHASE  45->46
tapdot(380, by['N'], C['N']); poly([(380, by['N']), (380, 168), (383.5, 168)], '#111', 1.0)
wn(381.0, 170.2, '45', size=5.9)
fuse(389, 168, 'F.CONTROL', '6A/32A 1PHASE', col=C['mag'])
line(392.1, 168, 395, 168, '#111', 1.0)
wn(396.4, 170.2, '46', size=5.9)
line(395, 168, 395, 78.5, '#111', 1.0)

# =====================================================================
# ZONE 005 — aux contacts · R2 · Q5 supply · TIMER · N0
# =====================================================================
cx2 = 294.7
line(395, 78.5, 294.7, 78.5, '#111', 1.0)
line(294.7, 78.5, 294.7, 76.0, '#111', 1.05)
txt(293.4, 79.2, 'X.KWH2  11', size=5.2, ha='right', style='italic')
dot(348.2, 78.5, '#111', 0.5)
line(348.2, 78.5, 348.2, 37, '#111', 1.0)
dot(371, 78.5, '#111', 0.5)
line(371, 78.5, 371, 32.6, '#111', 1.0)
line(371, 32.6, 368.9, 32.6, '#111', 1.0)
aux_box(cx2 - 4.8, 68.0, 'KWH2', h=8.0)
line(cx2, 68.0, cx2, 63.5, '#111', 1.05); dot(cx2, 63.5)
txt(cx2 + 1.3, 62.5, 'X.KWH2  12', size=5.5, style='italic')
sx2 = 312
line(cx2, 63.5, sx2, 63.5, '#111', 1.05)
line(sx2, 63.5, sx2, 72.0, '#111', 1.05)
term(sx2, 72.0, '#111', 0.6)
wn(sx2 + 2.6, 74.8, '23', size=5.5)
line(sx2, 72.0, sx2, 73.7, '#111', 1.05)
ax.plot([sx2, sx2 + 2.0], [73.7, 72.1], color='#111', lw=1.05, zorder=5)
dot(sx2 + 2.0, 72.1, '#111', 0.45)
txt(sx2 + 4.2, 76.4, 'S1', size=6.0, weight='bold', color=C['mag'])
line(sx2, 72.0, sx2, 11.3, '#111', 1.05)
dot(sx2, 11.3, '#111', 0.5)
wn(sx2 + 1.4, 63.8, '24', size=5.2)
# R2 coil
ax.add_patch(Rectangle((322, 62.0), 15, 11, fc='white', ec='#111', lw=1.05, zorder=5))
txt(329.5, 70.7, 'RELAY', size=5.4, ha='center'); txt(329.5, 68.2, 'R2', size=6.2, ha='center', weight='bold')
ax.add_patch(Rectangle((326.5, 63.5), 4.4, 3.4, fc='white', ec='#111', lw=0.9, zorder=6))
ax.plot([326.5, 330.9], [63.5, 66.9], color='#111', lw=0.9, zorder=6)
wn(332.2, 68.2, 'A1', size=5.2, ha='left')
wn(332.2, 64.2, 'A2', size=5.2, ha='left')
line(319, 46.4, 319, 54.5, '#111', 1.0)
line(319, 54.5, 341, 54.5, '#111', 1.0)
line(341, 54.5, 341, 68.2, '#111', 1.0)
line(341, 68.2, 337.4, 68.2, '#111', 1.0)
line(337.4, 64.2, 344, 64.2, '#111', 1.0)
line(344, 64.2, 344, 11.3, '#111', 1.0)
dot(344, 11.3, '#111', 0.5)
# N0 rail (shared line: coil A2 and Q5 P2 drop onto it)
line(290, 11.3, 348.2, 11.3, '#111', 1.05)
arrL(290, 286.2, 11.3, '#111')
txt(284.8, 12.6, 'N0', size=6.6, style='italic', weight='bold', ha='right')
# Q5 control box
Q5x, Q5y, Q5w, Q5h = 336, 15, 32, 22
ax.add_patch(Rectangle((Q5x, Q5y), Q5w, Q5h, fc='white', ec='#111', lw=1.2, zorder=4))
txt(Q5x + 1.1, Q5y + Q5h - 2.2, 'Q5', size=6.9, weight='bold')
txt(Q5x + 2.2, Q5y + 9.4, 'AC 230V', size=5.5); txt(Q5x + 2.2, Q5y + 7.2, 'POWER SUPPLY', size=5.5)
shunt(Q5x + 11, Q5y + 8.0, to_right=0.0)
txt(Q5x + 12.2, Q5y + 12.4, 'P1', size=5.6, ha='center'); txt(Q5x + 12.2, Q5y + 5.6, 'P2', size=5.6, ha='center')
term(Q5x + Q5w, Q5y + Q5h - 4.4, '#111', 0.65); txt(Q5x + Q5w - 1.7, Q5y + Q5h - 4.4, 'C', size=5.9, ha='right', weight='bold')
term(Q5x + Q5w, Q5y + 4.0, '#111', 0.65); txt(Q5x + Q5w - 1.7, Q5y + 4.0, 'NC', size=5.9, ha='right', weight='bold')
line(Q5x + 12.2, Q5y, Q5x + 12.2, 11.3, '#111', 1.05)
dot(Q5x + 12.2, 11.3, '#111', 0.5)
sz(Q5x + 14.2, 26.5, '1*1.5mm²', rot=90, size=5.5)
# R2 NO contact (13 / 14)
ax.add_patch(Rectangle((350, 40), 18, 9.5, fc='white', ec='#111', lw=1.05, zorder=5))
txt(351.0, 47.1, 'RELAY', size=5.4); txt(351.0, 44.9, 'R2', size=6.1, weight='bold')
ax.plot([362, 364.0], [51.2, 49.8], color='#111', lw=1.0, zorder=6)
wn(365.2, 51.6, '13', size=5.4)
line(362, 40, 362, 38.6, '#111', 1.0)
wn(365.2, 38.9, '14', size=5.4)
# NC -> 13 up the right of the box ; C -> 46 riser
poly([(368, 19.0), (374.5, 19.0), (374.5, 52.5), (362, 52.5)], '#111', 1.0)
line(362, 52.5, 362, 51.2, '#111', 1.0)
dot(362, 52.5, '#111', 0.55)

# TIMER
Txx, Txy, TTw, TTh = 286, 18, 44, 28
ax.add_patch(Rectangle((Txx, Txy), TTw, TTh, fc='#f7f7f7', ec='#111', lw=1.3, zorder=5))
txt(Txx + TTw / 2, Txy + TTh + 1.8, 'TIMER', size=7.6, ha='center', weight='bold')
txt(Txx + TTw / 2, Txy + TTh - 3.1, 'TEMPERATURE CONTROLLER', size=5.9, ha='center', weight='bold')
txt(Txx + TTw / 2, Txy + TTh - 6.1, '180-250 VAC', size=5.7, ha='center')
txt(Txx + 2.4, Txy + TTh - 6.1, 'PH', size=5.3)
txt(Txx + TTw - 4.4, Txy + TTh - 6.1, 'N', size=5.3)
ax.add_patch(Rectangle((Txx + 2.8, Txy + 7.0), 16.5, 10.2, fc='#0f1d2b', ec='#333', lw=0.9, zorder=6))
txt(Txx + 4.3, Txy + 14.5, 'PV', size=5.1, color='#8fd6ff')
txt(Txx + 4.3, Txy + 11.7, 'SV', size=5.1, color='#8fd6ff')
txt(Txx + 4.3, Txy + 8.6, 'REL', size=4.9, color='#ffd23f')
ax.add_patch(Circle((Txx + 12.8, Txy + 14.5), 0.62, fc=C['red2'], ec='none', zorder=7))
txt(Txx + 15.1, Txy + 14.8, '+', size=5.5, color='#e8e8e8')
txt(Txx + 15.1, Txy + 12.0, '–', size=5.5, color='#e8e8e8')
txt(Txx + 29.5, Txy + 19.6, 'TRB-900', size=6.0, ha='center', weight='bold')
txt(Txx + 27.6, Txy + 16.4, 'SHIVA', size=5.5, ha='center', weight='bold')
txt(Txx + 31.2, Txy + 13.4, 'AMVAJ', size=5.5, ha='center', weight='bold')
txt(Txx + 30.2, Txy + 9.8, 'CODE : 15B2', size=5.1, ha='center')
for i, (tno, px) in enumerate([('18', Txx + 6), ('15', Txx + 19.5), ('16', Txx + 34)]):
    term(px, Txy, '#111', 0.65)
    line(px, Txy - 0.7, px, Txy - 2.1, '#111', 1.0)
    txt(px + 1.3, Txy - 2.1, tno, size=5.6, color=C['mag'], weight='bold')
txt(Txx + TTw - 2.0, Txy + 1.8, 'MAX 5A', size=5.6, weight='bold', ha='right')
poly([(Txx + 34, Txy - 2.1), (Txx + 34, Txy - 3.6), (330, Txy - 3.6), (330, 38.6), (362, 38.6)], '#111', 1.0)
dot(362, 38.6, '#111', 0.55)

# =====================================================================
# ZONE 006 — three untagged 1PHASE 125A MCCBs
# =====================================================================
colx = [390, 414, 438]
for i, (cx, bk, ey) in enumerate(zip(colx, ['R', 'S', 'T'], [80, 77.5, 75])):
    rx = 462 + i * 3.5
    tapdot(rx, by[bk], C[bk]); line(rx, by[bk], rx, ey - 2.6 * i, C[bk], 1.1)
    poly([(rx, ey - 2.6 * i), (cx, ey - 2.6 * i), (cx, 66.5)], C[bk], 1.1)
    wn(cx + 1.1, 64.6, str(70 + i * 4), size=6.0)
    txt(cx - 2.4, 61.0, 'MCCB', size=6.0, ha='right', weight='bold')
    txt(cx - 2.4, 58.7, '1PHASE 125A', size=5.7, ha='right')
    line(cx, 66.5, cx, 55.5, '#111', 1.2)
    term(cx, 55.5, '#111', 0.6)
    ax.plot([cx, cx + 2.1], [55.5, 57.5], color='#111', lw=1.1, zorder=5)
    dot(cx + 2.1, 57.5, '#111', 0.5)
    ax.add_patch(Rectangle((cx - 2.7, 50.8), 5.4, 3.8, fc='white', ec='#111', lw=1.0, zorder=5))
    poly([(cx - 1.15, 50.8), (cx - 1.15, 52.0), (cx + 0.05, 52.0), (cx + 0.05, 53.1)], '#111', 0.9)
    txt(cx + 1.1, 51.6, 'I>', size=5.4, weight='bold')
    shunt(cx - 7.3, 53.3)
    line(cx, 50.8, cx, 46.0, '#111', 1.15)
    for j, (lab, num, cc) in enumerate([('R', 71 + i * 3, C[bk]),
                                        ('N', 72 + i * 3, C['N']),
                                        ('E', 73 + i * 3, C['E'])]):
        px = cx - 4 + j * 4
        poly([(cx, 46.0), (cx, 44.0), (px, 44.0)], '#111', 1.0)
        line(px, 44.0, px, 14.0, cc, 1.15)
        txt(px - 0.9, 40.5, str(num), size=5.3, ha='right', color=C['mag'], weight='bold', bbox=True)
        txt(px - 0.9, 37.6, lab, size=5.4, ha='right', color=C['green2'], weight='bold', bbox=True)
        sz(px - 2.4, 26, '1*2.5mm²', rot=90, size=5.0)
        dot(px, 14.4, cc, 0.55)
        arrD(px, 14.0, 11.2, cc)
        txt(px, 12.4, '148', size=5.2, ha='center', color=C['mag'], weight='bold', bbox=True)
ncx = 452
tapdot(ncx, by['N'], C['N'], 0.7)
line(ncx, by['N'], ncx, 66.0, C['gray'], 0.9)
poly([(ncx, 66.0), (376, 66.0), (376, 28.2)], C['gray'], 0.9)
term(376, 27, '#111', 0.65)
txt(377.4, 25.2, 'NC', size=6.0, weight='bold')
sz(377.9, 42, '1*1.5mm²', rot=90, size=5.2)

# ================= FOOTER =================
ax.add_patch(Rectangle((8, 2.0), W - 16, 5.8, fc='#eef3f8', ec='#9fb4c8', lw=0.8, zorder=1))
txt(10, 4.9,
    'R/S/T/N·PE risers from the incoming bus feed Q0 (through CT1–CT6) and the lighting · socket · control circuits — every run above lands on a terminal, breaker, strip or labelled continuation arrow',
    size=5.6, color='#223', va='center')
txt(W - 10, 4.9, 'wire numbers in magenta · conductor sizes in bold italic · connections exactly as drawn in the source master',
    size=5.7, ha='right', style='italic', color='#456', va='center')

fig.savefig('/home/user/Bargh/bargh_master_diagram.png', facecolor='white')
fig.savefig('/home/user/Bargh/bargh_master_diagram.svg', facecolor='white')
print('saved')
