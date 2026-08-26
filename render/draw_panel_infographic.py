# -*- coding: utf-8 -*-
"""Pictorial infographic of the panel — style: 'اجزای تابلو برق' infographics
   (open-panel view + numbered Persian callouts), structure exactly per PDFs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Ellipse
from matplotlib import font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
import warnings

fm.fontManager.addfont('/home/user/fonts/Vazirmatn-Regular.ttf')
fm.fontManager.addfont('/home/user/fonts/Vazirmatn-Bold.ttf')
FP_R = fm.FontProperties(fname='/home/user/fonts/Vazirmatn-Regular.ttf')
FP_B = fm.FontProperties(fname='/home/user/fonts/Vazirmatn-Bold.ttf')

def fa(s):
    return get_display(arabic_reshaper.reshape(s))

fig, ax = plt.subplots(figsize=(16, 10), dpi=150)
ax.set_xlim(0, 16); ax.set_ylim(0, 10); ax.axis('off')
fig.patch.set_facecolor('#eef1f5')
fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)

# ================= title =================
ax.text(8, 9.62, fa('اجزای تابلو برق — بازسازی از نقشه‌های PDF'),
        fontproperties=FP_B, fontsize=17, ha='center', va='center', color='#12345a')
ax.text(8, 9.24, 'panel components infographic  ·  structure exactly per drawing set: '
        'totall.pdf + 001…006.pdf  ·  Q0 250A motorized · CT1–CT9 400/5A · SVA×3 · '
        'Lighting + Q1–Q3 100A · 3×125A 1-ph · Q5 100A motorized · TRB-900',
        fontsize=7.6, ha='center', va='center', color='#5a6a7a')

# ================= enclosure =================
ax.add_patch(FancyBboxPatch((0.40, 0.30), 12.15, 8.55,
             boxstyle='round,pad=0.02,rounding_size=0.12',
             fc='#e8ebee', ec='#7d8894', lw=2.6, zorder=1))
ax.add_patch(Rectangle((0.58, 0.48), 11.80, 8.20, fill=False,
             ec='#c3cad1', lw=1.0, zorder=1))  # inner frame hint

# ================= sidebar (legend) =================
ax.add_patch(FancyBboxPatch((12.80, 0.30), 2.90, 8.55,
             boxstyle='round,pad=0.02,rounding_size=0.12',
             fc='#ffffff', ec='#b7c1ca', lw=1.6, zorder=1))
ax.text(14.25, 8.52, fa('اجزای تابلو'), fontproperties=FP_B, fontsize=12.5,
        ha='center', va='center', color='#12345a')
ax.plot([13.05, 15.45], [8.28, 8.28], color='#12345a', lw=1.2)

items = [
    ('۱', fa('کابل ورودی ۳ فاز + نول')),
    ('۲', fa('کلید اصلی Q0 — MCCB 250A موتوری')),
    ('۳', fa('ترانس جریان CT1 تا CT6 — 400/5A')),
    ('۴', fa('مترهای SVA ورودی (دو عدد)')),
    ('۵', fa('باسبار L1 · L2 · L3 · N · PE')),
    ('۶', fa('فیدر روشنایی — 100A سه‌فاز')),
    ('۷', fa('فیدرهای Q1 تا Q3 — هرکدام 100A')),
    ('۸', fa('سه فیدر تک‌فاز 125A (L1/L2/L3)')),
    ('۹', fa('فیدر Q5 موتوری + CT7-9 + SVA3')),
    ('۱۰', fa('کنترلر دما TRB-900 (شیوا امواج)')),
    ('۱۱', fa('منابع تغذیه 230V فرمان')),
]
y = 7.98
for num, txt in items:
    ax.add_patch(Circle((13.28, y), 0.135, fc='#12345a', ec='none', zorder=6))
    ax.text(13.28, y, fa(num), fontproperties=FP_B, fontsize=7.5,
            ha='center', va='center', color='white', zorder=7)
    ax.text(13.52, y, txt, fontproperties=FP_R, fontsize=7.6,
            ha='left', va='center', color='#22303c')
    y -= 0.575
ax.add_patch(FancyBboxPatch((12.98, 1.06), 2.54, 0.86,
             boxstyle='round,pad=0.02,rounding_size=0.08',
             fc='#e9f5e9', ec='#4a7d4a', lw=1.2))
ax.text(14.25, 1.72, fa('منطق کارکرد'), fontproperties=FP_B, fontsize=8,
        ha='center', va='center', color='#1a5c1a')
ax.text(14.25, 1.42, fa('کنترلر دما TRB-900، قطع/وصل خودکار فیدر Q5'),
        fontproperties=FP_R, fontsize=6.6, ha='center', va='center', color='#1a5c1a')
ax.text(14.25, 0.62, fa('ساختار مطابق ۷ فایل PDF در گیت‌هاب'),
        fontproperties=FP_R, fontsize=6.4, ha='center', va='center', color='#7a8794')

# ================= helpers =================
def badge(n, x, y):
    ax.add_patch(Circle((x, y), 0.155, fc='#d62828', ec='white', lw=1.2, zorder=9))
    ax.text(x, y, fa(n), fontproperties=FP_B, fontsize=7.5,
            ha='center', va='center', color='white', zorder=10)

def breaker(cx, top, w, h, tag, rating, poles=3, motor=False, tag_fs=8):
    ax.add_patch(FancyBboxPatch((cx-w/2, top-h), w, h,
                 boxstyle='round,pad=0.01,rounding_size=0.04',
                 fc='#454c56', ec='#262b31', lw=1.3, zorder=5))
    ax.add_patch(Rectangle((cx-w/2+0.055, top-h+0.08), w-0.11, h-0.24,
                 fc='#69737e', ec='none', zorder=6))
    # toggle lever
    ax.add_patch(Rectangle((cx-0.045, top-h+0.22), 0.09, h*0.42,
                 fc='#d8dce0', ec='#33383e', lw=0.8, zorder=7))
    if poles == 3:
        for dx in (-w/6, w/6):
            ax.plot([cx+dx, cx+dx], [top-h+0.06, top-0.06],
                    color='#31363c', lw=0.9, zorder=7)
    ax.text(cx, top-h+0.115, rating, fontsize=5.9 if w < 0.5 else 6.6,
            ha='center', va='center', color='#eef2f5', zorder=8)
    ax.text(cx, top+0.115, tag, fontsize=tag_fs, fontweight='bold',
            ha='center', va='center', color='#15202b', zorder=8)
    if motor:
        ax.add_patch(FancyBboxPatch((cx+w/2+0.03, top-0.42), 0.34, 0.34,
                     boxstyle='round,pad=0.01,rounding_size=0.03',
                     fc='#9aa2ab', ec='#262b31', lw=1.0, zorder=6))
        ax.text(cx+w/2+0.20, top-0.25, 'M', fontsize=8, fontweight='bold',
                ha='center', va='center', zorder=7)
        return cx + w/2 + 0.20
    return None

def ct_donut(x, y, r=0.115):
    ax.add_patch(Circle((x, y), r, fill=False, ec='#1c2530', lw=1.7, zorder=7))

def meter_module(x0, y0, x1, y1, title, line2):
    ax.add_patch(FancyBboxPatch((x0, y0), x1-x0, y1-y0,
                 boxstyle='round,pad=0.01,rounding_size=0.04',
                 fc='#1d2733', ec='#0c1116', lw=1.2, zorder=5))
    ax.add_patch(Rectangle((x0+0.07, y0+0.26), (x1-x0)-0.14, 0.24,
                 fc='#0d3a1d', ec='#0a2a15', lw=0.8, zorder=6))
    ax.text((x0+x1)/2, y0+0.38, line2, fontsize=6.0, fontweight='bold',
            ha='center', va='center', color='#39ff6a', zorder=7, family='monospace')
    ax.text((x0+x1)/2, y1-0.13, title, fontsize=7.2, fontweight='bold',
            ha='center', va='center', color='white', zorder=7)
    # terminal strip
    for i in range(5):
        ax.add_patch(Rectangle((x0+0.12+i*0.16, y0+0.055), 0.10, 0.10,
                     fc='#c9a227', ec='#7a6110', lw=0.5, zorder=6))

# ================= busbar =================
bars = [('L1', 8.28, '#c87933'), ('L2', 8.08, '#c87933'), ('L3', 7.88, '#c87933'),
        ('N',  7.68, '#5b7a95'), ('PE', 7.52, '#3f9b4f')]
for name, by, col in bars:
    ax.add_patch(Rectangle((0.90, by-0.055), 11.20, 0.11, fc=col, ec='none', zorder=5))
    ax.plot([0.95, 12.0], [by+0.030, by+0.030], color='white', lw=0.7, alpha=0.55, zorder=6)
    ax.text(12.18, by, name, fontsize=6.5, fontweight='bold',
            ha='left', va='center', color='#3a2a12')
for ix in (1.6, 6.0, 11.3):
    ax.add_patch(Rectangle((ix-0.07, 7.30), 0.14, 0.14, fc='#98a2ab', ec='#6c767f', lw=0.7, zorder=4))
ax.text(6.5, 8.52, fa('باسبار اصلی'), fontproperties=FP_B, fontsize=7.5,
        ha='center', va='center', color='#8a4d1c')
badge('۵', 1.12, 8.50)

# ================= incomer =================
# incoming cable
ax.plot([1.35, 1.35], [0.50, 3.42], color='#14181c', lw=5.2, zorder=4, solid_capstyle='round')
ax.annotate('', xy=(1.35, 3.30), xytext=(1.35, 2.85),
            arrowprops=dict(arrowstyle='-|>', color='#14181c', lw=2.0))
ax.text(1.62, 1.05, fa('کابل ورودی ۳ فاز + نول'), fontproperties=FP_R,
        fontsize=7.0, ha='left', va='center', color='#22303c')
badge('۱', 0.95, 1.05)
# Q0 breaker (big)
mx = breaker(1.35, 4.42, 0.95, 1.00, 'Q0', '250A', poles=3, motor=True, tag_fs=9.5)
ax.text(2.30, 3.65, fa('کلید اصلی موتوری'), fontproperties=FP_R, fontsize=6.6,
        ha='left', va='center', color='#22303c')
ax.text(2.30, 3.44, 'MCCB 3PH · 250A', fontsize=6.2, ha='left', va='center', color='#54626f')
badge('۲', 0.78, 4.32)
# risers Q0 -> bars
for xx, by in ((1.15, 8.28), (1.35, 8.08), (1.55, 7.88)):
    ax.plot([xx, xx], [4.42, by-0.055], color='#14181c', lw=1.9, zorder=3)
# CT donuts: CT1-3 @6.95, CT4-6 @6.30
for yy in (6.95, 6.30):
    for xx in (1.15, 1.35, 1.55):
        ct_donut(xx, yy)
ax.text(0.88, 7.18, 'CT1–CT3', fontsize=6.0, ha='right', va='center', color='#22303c')
ax.text(0.88, 7.03, '400/5A', fontsize=6.0, ha='right', va='center', color='#22303c')
ax.text(0.88, 6.53, 'CT4–CT6', fontsize=6.0, ha='right', va='center', color='#22303c')
ax.text(0.88, 6.38, '400/5A', fontsize=6.0, ha='right', va='center', color='#22303c')
badge('۳', 1.98, 7.02)
# measurement leads -> SVA meters
ax.plot([1.55, 2.05], [6.95, 6.95], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([2.05, 2.05], [6.95, 5.25], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([2.05, 2.60], [5.90, 5.90], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([1.55, 1.86], [6.30, 6.30], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([1.86, 1.86], [6.30, 4.60], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([1.86, 2.60], [4.60, 4.60], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([4.30, 4.42], [7.68, 7.68], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([4.42, 4.42], [7.68, 4.55], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([4.30, 4.42], [4.55, 4.55], color='#777', lw=1.0, ls=':', zorder=3)
meter_module(2.60, 5.55, 4.30, 6.25, 'SVA #1', '3x400/5A  V:400')
meter_module(2.60, 4.30, 4.30, 5.00, 'SVA #2', '3x400/5A  V:400')
badge('۴', 2.82, 6.06)

# ================= feeders =================
feeders = [
    (2.55, 'Lighting', '100A', 3, False, fa('روشنایی'), '۶'),
    (3.65, 'Q1', '100A', 3, False, fa('فیدر Q1'), '۷'),
    (4.75, 'Q2', '100A', 3, False, fa('فیدر Q2'), None),
    (5.85, 'Q3', '100A', 3, False, fa('فیدر Q3'), None),
    (7.05, '125A', '1P', 1, False, fa('تک‌فاز L1'), '۸'),
    (7.75, '125A', '1P', 1, False, fa('تک‌فاز L2'), None),
    (8.45, '125A', '1P', 1, False, fa('تک‌فاز L3'), None),
]
for fx, tag, rating, poles, motor, cap, bdg in feeders:
    w = 0.85 if poles == 3 else 0.40
    ax.plot([fx, fx], [7.80, 6.98], color='#14181c', lw=1.8, zorder=3)
    breaker(fx, 6.98, w, 0.82, tag, rating, poles=poles, tag_fs=7.2)
    ax.annotate('', xy=(fx, 5.86), xytext=(fx, 6.12),
                arrowprops=dict(arrowstyle='-|>', color='#14181c', lw=1.5))
    ax.text(fx, 5.68, cap, fontproperties=FP_R, fontsize=6.6,
            ha='center', va='center', color='#12345a')
    if bdg:
        badge(bdg, fx - w/2 - 0.02, 6.86)

# Q5 feeder
ax.plot([9.60, 9.60], [7.80, 6.98], color='#14181c', lw=1.8, zorder=3)
breaker(9.60, 6.98, 0.85, 0.82, 'Q5', '100A', poles=3, motor=True, tag_fs=7.5)
ax.annotate('', xy=(9.60, 5.86), xytext=(9.60, 6.12),
            arrowprops=dict(arrowstyle='-|>', color='#14181c', lw=1.5))
ax.text(9.60, 5.68, fa('بار تحت فرمان دما'), fontproperties=FP_R, fontsize=6.6,
        ha='center', va='center', color='#7a2d00')
badge('۹', 9.14, 6.86)
# CT7-9 + SVA3
for xx in (9.42, 9.60, 9.78):
    ct_donut(xx, 5.30)
ax.plot([9.60, 9.60], [5.18, 4.72], color='#777', lw=1.0, ls=':', zorder=3)
ax.plot([9.60, 10.60], [4.72, 4.72], color='#777', lw=1.0, ls=':', zorder=3)
ax.text(9.95, 5.44, 'CT7–CT9 · 400/5A', fontsize=5.8, ha='left', va='center', color='#22303c')
ax.plot([11.55, 11.55], [7.68, 4.98], color='#777', lw=1.0, ls=':', zorder=3)
meter_module(10.60, 4.30, 11.95, 5.00, 'SVA #3', '3x400/5A  V:400')

# ================= control compartment =================
ax.plot([0.62, 12.35], [3.05, 3.05], color='#8b95a0', lw=1.1, ls='--', zorder=3)
ax.text(12.30, 3.22, fa('محفظه‌ی فرمان و کنترل'), fontproperties=FP_R, fontsize=6.6,
        ha='right', va='center', color='#54626f')

def psu(x0, x1, num):
    ax.add_patch(FancyBboxPatch((x0, 1.85), x1-x0, 0.75,
                 boxstyle='round,pad=0.01,rounding_size=0.04',
                 fc='#c9d0d8', ec='#5d6873', lw=1.3, zorder=5))
    for i in range(3):
        ax.plot([x0+0.15, x1-0.15], [2.44-i*0.10, 2.44-i*0.10], color='#8d98a3', lw=1.0)
    ax.text((x0+x1)/2, 2.03, f'PSU {num} · AC 230V', fontsize=6.4, fontweight='bold',
            ha='center', va='center', color='#22303c')
    for i, c in enumerate(('#3f9b4f', '#c9a227', '#3f9b4f')):
        ax.add_patch(Rectangle((x0+0.16+i*0.18, 1.90), 0.11, 0.10, fc=c, ec='none'))

psu(3.00, 4.60, 1)
psu(4.85, 6.45, 2)
badge('۱۱', 5.65, 2.72)

# TRB-900 faceplate
ax.add_patch(FancyBboxPatch((7.00, 1.05), 2.55, 1.95,
             boxstyle='round,pad=0.01,rounding_size=0.05',
             fc='#2b2f33', ec='#101315', lw=1.5, zorder=5))
ax.add_patch(Rectangle((7.18, 1.95), 2.19, 0.75, fc='#14333f', ec='#0b242d', lw=1.0, zorder=6))
ax.text(8.275, 2.52, 'PV  075.0', fontsize=7.0, ha='center', va='center',
        color='#ffb347', family='monospace', zorder=7)
ax.text(8.275, 2.18, 'SV  080.0', fontsize=7.0, ha='center', va='center',
        color='#7fd4ff', family='monospace', zorder=7)
for i in range(3):
    ax.add_patch(Circle((7.45+i*0.28, 1.62), 0.085, fc='#596270', ec='#20262c', lw=0.8, zorder=6))
ax.text(8.275, 1.28, 'TRB-900 · SHIVA AMVAJ', fontsize=5.8, ha='center', va='center',
        color='#cdd6df', zorder=7)
ax.text(8.275, 0.88, fa('کنترلر دما · کد 15B2 · رله 5A (ترمینال 15/16/18)'),
        fontproperties=FP_R, fontsize=6.0, ha='center', va='center', color='#54626f')
badge('۱۰', 7.22, 2.88)

# command path TRB -> Q5 motor operator
ax.plot([9.55, 12.20, 12.20, 10.75], [1.75, 1.75, 6.45, 6.73],
        color='#1a7a1a', lw=1.7, ls='--', zorder=4)
ax.annotate('', xy=(10.62, 6.73), xytext=(10.80, 6.70),
            arrowprops=dict(arrowstyle='-|>', color='#1a7a1a', lw=1.7))
ax.text(12.34, 4.2, fa('فرمان خودکار بر اساس دما'), fontproperties=FP_R,
        fontsize=6.6, rotation=90, ha='center', va='center', color='#1a7a1a')

# footer
ax.text(6.5, 0.12, fa('تمام تگ‌ها و امپرانس مطابق نقشه‌های اصلی: Q0=250A موتوری، CT1–CT9=400/5A، فیدرها 100A/125A، Q5 موتوری + TRB-900'),
        fontproperties=FP_R, fontsize=6.8, ha='center', va='center', color='#5a6a7a')

with warnings.catch_warnings(record=True) as wlist:
    warnings.simplefilter('always')
    fig.savefig('/home/user/Bargh/render/panel_infographic.png', dpi=150, facecolor='#eef1f5')
glyph = [str(w.message) for w in wlist if 'Glyph' in str(w.message)]
print('glyph warnings:', len(glyph))
for g in glyph[:8]:
    print(' !', g)
print('saved OK')
