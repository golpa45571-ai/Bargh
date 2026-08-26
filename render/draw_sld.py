# -*- coding: utf-8 -*-
"""Single-line diagram: reconstructed understanding of the 7-PDF drawing set."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Circle
from matplotlib import font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
import warnings

# ---------- fonts ----------
fm.fontManager.addfont('/home/user/fonts/Vazirmatn-Regular.ttf')
fm.fontManager.addfont('/home/user/fonts/Vazirmatn-Bold.ttf')
FP_R = fm.FontProperties(fname='/home/user/fonts/Vazirmatn-Regular.ttf')
FP_B = fm.FontProperties(fname='/home/user/fonts/Vazirmatn-Bold.ttf')

def fa(s):
    """shape + reorder persian text"""
    return get_display(arabic_reshaper.reshape(s))

# ---------- canvas ----------
fig, ax = plt.subplots(figsize=(16, 10), dpi=150)
ax.set_xlim(0, 16); ax.set_ylim(0, 10)
ax.axis('off')
fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)

C_BUS  = '#8B0000'   # busbar
C_PWR  = '#111111'   # power conductors
C_CTRL = '#1a7a1a'   # control circuit
C_MEAS = '#777777'   # measurement taps

def X_breaker(x, y, s=0.15, lw=2.0, c=C_PWR):
    ax.plot([x-s, x+s], [y-s, y+s], color=c, lw=lw, zorder=6)
    ax.plot([x-s, x+s], [y+s, y-s], color=c, lw=lw, zorder=6)

def CT(x, y, label_lines, lx, ha_):
    ax.add_patch(Ellipse((x, y), 0.42, 0.17, fill=False, ec=C_PWR, lw=1.6, zorder=6))
    yy = y + 0.06
    for ln in label_lines:
        ax.text(lx, yy, ln, fontsize=6.0, ha=ha_, va='center', color='#333333')
        yy -= 0.13

# ---------- title ----------
ax.text(8, 9.62, fa('نمودار تک‌خطی برداشت من از کل نقشه'), fontproperties=FP_B,
        fontsize=15, ha='center', va='center', color='#0d2b52')
ax.text(8, 9.24, 'SINGLE-LINE DIAGRAM — my understanding of the complete drawing set  |  '
        'source: totall.pdf (overview) + 001…006.pdf  |  tags & ratings exactly as marked on the original',
        fontsize=8, ha='center', va='center', color='#555555')

# ---------- legend ----------
lx0 = 0.30
ax.text(lx0, 9.44, 'LEGEND', fontsize=6.5, fontweight='bold', color='#333')
ax.plot([lx0, lx0+0.55], [9.30, 9.30], color=C_BUS, lw=4)
ax.text(lx0+0.68, 9.30, fa('باسبار اصلی'), fontproperties=FP_R, fontsize=6.5, va='center')
ax.plot([lx0, lx0+0.55], [9.14, 9.14], color=C_PWR, lw=2)
ax.text(lx0+0.68, 9.14, fa('مدار قدرت'), fontproperties=FP_R, fontsize=6.5, va='center')
ax.plot([lx0, lx0+0.55], [8.98, 8.98], color=C_CTRL, lw=1.6, ls='--')
ax.text(lx0+0.68, 8.98, fa('مدار فرمان ۲۳۰ ولت'), fontproperties=FP_R, fontsize=6.5, va='center')
ax.plot([lx0, lx0+0.55], [8.82, 8.82], color=C_MEAS, lw=1.3, ls=':')
ax.text(lx0+0.68, 8.82, fa('تپ‌های اندازه‌گیری'), fontproperties=FP_R, fontsize=6.5, va='center')

# ---------- main bus ----------
ax.plot([1.0, 15.4], [8.6, 8.6], color=C_BUS, lw=5, solid_capstyle='butt', zorder=5)
ax.text(8.0, 8.80, 'MAIN BUSBAR  —  L1 · L2 · L3 · N  (+PE)', fontsize=9, fontweight='bold',
        ha='center', va='center', color=C_BUS)

# ---------- incomer ----------
XRAIL = 1.2
ax.plot([XRAIL, XRAIL], [8.6, 1.05], color=C_PWR, lw=2.2, zorder=4)
ax.annotate('', xy=(XRAIL, 1.30), xytext=(XRAIL, 0.85),
            arrowprops=dict(arrowstyle='-|>', color=C_PWR, lw=2.2))
ax.text(XRAIL, 0.66, 'INCOMING CABLE', fontsize=7.5, fontweight='bold', ha='center')
ax.text(XRAIL, 0.46, fa('کابل ورودی ۳فاز + نول از پایین (مطابق نقشه)'),
        fontproperties=FP_R, fontsize=6.3, ha='center', color='#333')
# Q0 breaker + motor op
X_breaker(XRAIL, 5.2)
ax.add_patch(Circle((0.84, 5.2), 0.15, fill=True, fc='white', ec=C_PWR, lw=1.5, zorder=6))
ax.text(0.84, 5.2, 'M', fontsize=7, ha='center', va='center', fontweight='bold')
ax.plot([0.99, 1.05], [5.2, 5.2], color=C_PWR, lw=1.2, ls='--')
ax.text(1.55, 5.33, 'Q0 — INCOMER', fontsize=8.5, fontweight='bold', va='center')
ax.text(1.55, 5.13, 'MCCB 3PHASE · 250A', fontsize=7.5, va='center')
ax.text(1.55, 4.95, 'WITH MOTOR OPERATOR', fontsize=6.8, va='center', color='#444')
# CTs on incomer
CT(XRAIL, 7.25, ['CT1–CT3', '400/5A'], 0.93, 'right')
CT(XRAIL, 6.25, ['CT4–CT6', '400/5A'], 0.93, 'right')
ax.plot([1.41, 1.80], [7.25, 7.25], color=C_MEAS, lw=1.2, ls=':')
ax.plot([1.41, 1.80], [6.25, 6.25], color=C_MEAS, lw=1.2, ls=':')
# SVA meters 1 & 2
def sva_box(x0, y0, x1, y1, title, l1, l2):
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0,
                 boxstyle='round,pad=0.02,rounding_size=0.06',
                 fc='#eaf2fb', ec='#3b6ea5', lw=1.3, zorder=5))
    cx = (x0+x1)/2
    ax.text(cx, y1-0.16, title, fontsize=8, fontweight='bold', ha='center', va='center', color='#1d4f8a')
    ax.text(cx, y1-0.36, l1, fontsize=6.0, ha='center', va='center')
    ax.text(cx, y1-0.54, l2, fontsize=6.0, ha='center', va='center')

sva_box(1.80, 6.90, 3.15, 7.60, 'SVA #1', 'I1·I2·I3  ←  CT1–CT3', 'N·L1·L2·L3  (V-taps)')
sva_box(1.80, 5.90, 3.15, 6.60, 'SVA #2', 'I1·I2·I3  ←  CT4–CT6', 'N·L1·L2·L3  (V-taps)')
ax.text(2.475, 5.70, 'both CT groups on the SAME incomer (redundant metering?)',
        fontsize=5.8, style='italic', color='#888', ha='center')
# voltage taps dashed
ax.plot([3.25, 3.25], [8.6, 6.20], color=C_MEAS, lw=1.2, ls=':')
ax.plot([3.25, 3.15], [7.25, 7.25], color=C_MEAS, lw=1.2, ls=':')
ax.plot([3.25, 3.15], [6.25, 6.25], color=C_MEAS, lw=1.2, ls=':')
ax.text(3.36, 7.60, 'V-taps: N,L1,L2,L3', fontsize=6.0, rotation=90, color='#666', va='top')

# ---------- feeders ----------
def feeder(x, tag_lines, arrow_y=5.2, cap=None, cap2=None):
    ax.plot([x, x], [8.6, arrow_y], color=C_PWR, lw=2.0, zorder=4)
    X_breaker(x, 7.7)
    yy = 7.32
    for i, (txt, sz, bold) in enumerate(tag_lines):
        ax.text(x, yy, txt, fontsize=sz, ha='center', va='center',
                fontweight='bold' if bold else 'normal')
        yy -= 0.185
    ax.annotate('', xy=(x, arrow_y-0.24), xytext=(x, arrow_y),
                arrowprops=dict(arrowstyle='-|>', color=C_PWR, lw=1.8))
    if cap:
        ax.text(x, 4.80, fa(cap), fontproperties=FP_R, fontsize=7.0, ha='center', color='#0d2b52')
    if cap2:
        ax.text(x, 4.58, fa(cap2), fontproperties=FP_R, fontsize=6.0, ha='center', color='#555')

feeder(3.65, [('Lighting', 7.5, True), ('MCCB 3P · 100A', 6.6, False)], cap='بار روشنایی')
feeder(4.75, [('Q1', 7.5, True), ('MCCB 3P · 100A', 6.6, False)], cap='فیدر سه‌فاز')
feeder(5.85, [('Q2', 7.5, True), ('MCCB 3P · 100A', 6.6, False)], cap='فیدر سه‌فاز')
feeder(6.95, [('Q3', 7.5, True), ('MCCB 3P · 100A', 6.6, False)], cap='فیدر سه‌فاز')
feeder(8.50, [('MCCB 1P · 125A', 6.8, True), ('from L1 · (+N+PE)', 6.0, False)], cap='بار تک‌فاز')
feeder(9.70, [('MCCB 1P · 125A', 6.8, True), ('from L2 · (+N+PE)', 6.0, False)], cap='بار تک‌فاز')
feeder(10.90, [('MCCB 1P · 125A', 6.8, True), ('from L3 · (+N+PE)', 6.0, False)], cap='بار تک‌فاز')
ax.text(9.70, 4.30, 'confirmed by you: each 125A MCCB is single-phase, one per phase (L1 / L2 / L3)',
        fontsize=6.2, style='italic', color='#777', ha='center')

# ---------- Q5 feeder ----------
X5 = 12.7
ax.plot([X5, X5], [8.6, 5.2], color=C_PWR, lw=2.0, zorder=4)
X_breaker(X5, 7.7)
ax.add_patch(Circle((13.02, 7.7), 0.16, fill=True, fc='white', ec=C_PWR, lw=1.5, zorder=6))
ax.text(13.02, 7.7, 'M', fontsize=7.5, ha='center', va='center', fontweight='bold')
ax.plot([X5+0.16, 12.86], [7.7, 7.7], color=C_PWR, lw=1.2, ls='--')
ax.text(X5, 7.32, 'Q5 — MCCB 3P · 100A', fontsize=7.0, fontweight='bold', ha='center', va='center')
ax.text(X5, 7.13, 'WITH MOTOR', fontsize=6.4, ha='center', va='center', color='#444')
CT(X5, 6.5, ['CT7–CT9', '400/5A'], 12.42, 'right')
ax.plot([12.91, 13.75], [6.5, 6.5], color=C_MEAS, lw=1.2, ls=':')
sva_box(13.75, 6.15, 15.45, 6.90, 'SVA #3', 'I1·I2·I3  ←  CT7–CT9', 'N·L1·L2·L3  from bus')
ax.plot([14.60, 14.60], [8.6, 6.90], color=C_MEAS, lw=1.2, ls=':')
ax.text(14.72, 8.45, 'V-taps', fontsize=6.0, rotation=90, color='#666', va='top')
ax.annotate('', xy=(X5, 4.96), xytext=(X5, 5.2),
            arrowprops=dict(arrowstyle='-|>', color=C_PWR, lw=1.8))
ax.text(X5, 4.80, fa('بار تحت فرمان دما'), fontproperties=FP_B, fontsize=7.2,
        ha='center', color='#7a2d00')
ax.text(X5, 4.58, fa('فن / المنت حرارتی (استنتاج من)'), fontproperties=FP_R,
        fontsize=6.0, ha='center', color='#555')

# command line: TRB-900 relay -> Q5 motor operator
ax.plot([13.40, 13.40], [2.0, 7.25], color=C_CTRL, lw=1.6, ls='--')
ax.plot([13.40, 13.28], [7.25, 7.48], color=C_CTRL, lw=1.6, ls='--')
ax.annotate('', xy=(13.14, 7.62), xytext=(13.24, 7.50),
            arrowprops=dict(arrowstyle='-|>', color=C_CTRL, lw=1.6))
ax.text(13.53, 5.3, 'TRB-900 RELAY → Q5 MOTOR OPERATOR (auto ON/OFF)',
        fontsize=6.2, rotation=90, color=C_CTRL, va='center')

# ---------- control strip ----------
ax.add_patch(FancyBboxPatch((2.60, 0.35), 12.85, 3.20,
             boxstyle='round,pad=0.02,rounding_size=0.08',
             fc='#f4faf4', ec='#4a7d4a', lw=1.5, zorder=2))
ax.text(2.85, 3.30, fa('مدار فرمان ۲۳۰ ولت AC'), fontproperties=FP_B, fontsize=9,
        ha='left', va='center', color='#1a5c1a')
ax.text(6.30, 3.30, '—  CONTROL SUPPLY & AUTOMATIC CONTROL', fontsize=7.5,
        ha='left', va='center', color='#557')

# PSUs
for (bx0, bx1, num, tag) in [(3.0, 5.1, '#1', "feed breaker tagged 'Q0' (dup!)"),
                             (5.5, 7.6, '#2', "feed breaker tagged 'Q5' (dup!)")]:
    cx = (bx0+bx1)/2
    ax.add_patch(FancyBboxPatch((bx0, 2.55), bx1-bx0, 0.55,
                 boxstyle='round,pad=0.02,rounding_size=0.05',
                 fc='#eef7ee', ec='#4a7d4a', lw=1.2, zorder=5))
    ax.text(cx, 2.92, f'AC 230V POWER SUPPLY · {num}', fontsize=6.8, fontweight='bold',
            ha='center', va='center')
    ax.text(cx, 2.72, tag, fontsize=5.8, ha='center', va='center', color='#666')
    ax.plot([cx, cx], [2.55, 2.30], color=C_CTRL, lw=1.6)

# rails
ax.plot([3.20, 8.15], [2.30, 2.30], color=C_CTRL, lw=2.0)
ax.plot([3.20, 8.15], [1.70, 1.70], color='#888', lw=1.6)
ax.text(3.12, 2.30, 'L', fontsize=6.5, fontweight='bold', ha='right', color=C_CTRL)
ax.text(3.12, 1.70, 'N', fontsize=6.5, ha='right', color='#888')
ax.plot([8.15, 8.35], [2.30, 2.30], color=C_CTRL, lw=2.0)
ax.plot([8.15, 8.35], [1.70, 1.70], color='#888', lw=1.6)

# TRB-900
ax.add_patch(FancyBboxPatch((8.35, 1.05), 2.95, 2.05,
             boxstyle='round,pad=0.02,rounding_size=0.06',
             fc='#fdf1e3', ec='#c07830', lw=1.4, zorder=5))
tx = 9.825
ax.text(tx, 2.92, 'TRB-900 — TEMPERATURE CONTROLLER', fontsize=7.4, fontweight='bold',
        ha='center', va='center', color='#8a4b00')
ax.text(tx, 2.70, 'SHIVA AMVAJ · CODE: 15B2', fontsize=6.3, ha='center', va='center')
ax.text(tx, 2.48, 'Supply: 180–250 VAC  ← control rails', fontsize=6.3, ha='center', va='center')
ax.text(tx, 2.26, 'Display: PV (actual) / SV (set) / REL led', fontsize=6.3, ha='center', va='center')
ax.text(tx, 2.04, 'Relay output: MAX 5A — terminals 15/16/18', fontsize=6.3, ha='center', va='center')
ax.text(tx, 1.82, 'sensor: thermocouple (not drawn in the PDFs)', fontsize=5.8,
        style='italic', color='#999', ha='center', va='center')
ax.text(tx, 1.50, fa('کنترلر دما — فرمان خودکار وصل/قطع فیدر Q5'),
        fontproperties=FP_R, fontsize=6.5, ha='center', va='center', color='#8a4b00')
ax.text(tx, 1.28, fa('مطابق توپولوژی فایل 005'),
        fontproperties=FP_R, fontsize=5.8, ha='center', va='center', color='#a06a30')

# relay output contact + link up
ax.plot([11.30, 11.70], [2.0, 2.0], color=C_CTRL, lw=1.6)
ax.plot([11.70, 11.92], [2.14, 2.0], color=C_CTRL, lw=1.8)
ax.plot([11.92, 13.40], [2.0, 2.0], color=C_CTRL, lw=1.6, ls='--')
ax.plot([11.70, 11.70], [2.0, 1.88], color=C_CTRL, lw=1.6)
ax.text(11.78, 2.24, 'REL 15/16/18', fontsize=5.6, color=C_CTRL, ha='center')

# notes
ax.text(2.85, 0.85, 'Per 005.pdf: TRB-900 relay (terms 15/16/18) switches the command branch (coil) of Q5 motor operator.',
        fontsize=6.3, style='italic', color='#666', ha='left')
ax.text(2.85, 0.60, fa('دو منبع تغذیه ۲۳۰ ولت: یکی در ناحیه روشنایی (تگ Q0) و یکی در ناحیه Q5 (تگ Q5)'),
        fontproperties=FP_R, fontsize=6.5, color='#555', ha='left')

# footer
ax.text(8, 0.14, fa('بازسازی از تحلیل برداری ۷ فایل PDF | تگ‌ها و جریان‌های نامی مطابق نقشه اصلی'),
        fontproperties=FP_R, fontsize=7.0, color='#666', ha='center')

# ---------- save with glyph check ----------
with warnings.catch_warnings(record=True) as wlist:
    warnings.simplefilter('always')
    fig.savefig('/home/user/Bargh/render/SLD_understanding.png', dpi=150,
                facecolor='white', bbox_inches=None)
glyph_issues = [str(w.message) for w in wlist if 'Glyph' in str(w.message) or 'missing' in str(w.message).lower()]
print('glyph warnings:', len(glyph_issues))
for g in glyph_issues[:10]:
    print('  !', g)
print('saved OK')
