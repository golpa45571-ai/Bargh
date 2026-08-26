# -*- coding: utf-8 -*-
"""Pixel-precise correction of the AI panel image to match the original PDF circuit.
Base = original AI image (best text baseline). All fixes applied programmatically."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

SRC = '/home/user/Bargh/file_00000000a51c82439f363061a6e7ef58.png'
OUT = '/home/user/Bargh/render/panel_final_fixed.png'

im = Image.open(SRC).convert('RGB')
W, H = im.size
px = im.load()
arr = np.array(im).astype(int)

FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def font(sz, bold=True): return ImageFont.truetype(FB if bold else FR, sz)

def ring_bg(x0, y0, x1, y1, margin=14, light=True):
    """sample background color from a ring around rect (excluding dark text pixels)"""
    X0, Y0, X1, Y1 = max(0,x0-margin), max(0,y0-margin), min(W,x1+margin), min(H,y1+margin)
    mask = np.zeros((Y1-Y0, X1-X0), bool)
    mask[:margin,:] = True; mask[-margin:,:] = True
    mask[:,:margin] = True; mask[:,-margin:] = True
    reg = arr[Y0:Y1, X0:X1]
    lum = reg.mean(axis=2)
    if light:
        sel = mask & (lum > 120)
    else:
        sel = mask & (lum < 120)
    if sel.sum() < 20: sel = mask
    med = np.median(reg[sel], axis=0)
    return tuple(int(v) for v in med)

def cover(x0, y0, x1, y1, color=None, noise=6, feather=True):
    """cover rect with sampled bg color + subtle noise"""
    if color is None: color = ring_bg(x0,y0,x1,y1)
    rng = np.random.default_rng(42)
    patch = np.clip(np.array(color) + rng.normal(0, noise, (y1-y0, x1-x0, 3)), 0, 255).astype(np.uint8)
    pimg = Image.fromarray(patch)
    if feather:
        m = Image.new('L', pimg.size, 0)
        ImageDraw.Draw(m).rectangle([4,4,pimg.size[0]-4,pimg.size[1]-4], fill=255)
        m = m.filter(ImageFilter.GaussianBlur(3))
        im.paste(pimg, (x0,y0), m)
    else:
        im.paste(pimg, (x0,y0))

def write(x, y, txt, sz=16, bold=True, col=None, anchor='mm'):
    if col is None: col = (28, 34, 42)
    d = ImageDraw.Draw(im)
    d.text((x, y), txt, font=font(sz, bold), fill=col, anchor=anchor)

def sample_text_color(x, y, r=6):
    reg = arr[max(0,y-r):y+r, max(0,x-r):x+r].reshape(-1,3)
    lum = reg.mean(axis=1)
    dark = reg[lum < lum.mean()]
    if len(dark)==0: dark = reg
    return tuple(int(v) for v in np.median(dark, axis=0))

# ============ 1) remove meters #3 & #4 (top row, x 940..1320) ============
cover(935, 112, 1330, 305)

# ============ 2) remove 4th 125A breaker (body x 1002..1082) ============
cover(1000, 462, 1085, 605)

# ============ 3) fix CT ratio labels: 400/5A (six on incomer) ============
for cx in (434, 490, 547):
    for cy in (103, 236):
        cover(cx-42, cy-11, cx+42, cy+11)
        write(cx, cy, '400/5A', 15)
# CT7-9 ratios
for cx in (1273, 1322, 1372):
    cover(cx-42, 560, cx+42, 584)
    write(cx, 572, '400/5A', 15)

# ============ 4) meter terminal rows -> I1 I1 I2 I2 I3 I3 ============
cover(575, 132, 745, 152)
write(660, 142, 'I1 I1  I2 I2  I3 I3', 13)
cover(800, 132, 960, 152)
write(880, 142, 'I1 I1  I2 I2  I3 I3', 13)
# aux supply label of meter1
cover(706, 127, 812, 147)
write(759, 137, 'POWER SUPPLY', 12)
# voltage terminal rows of the two kept meters
cover(640, 258, 780, 292)
write(710, 268, 'N  L1  L2  L3', 13)
cover(800, 258, 940, 292)
write(870, 268, 'N  L1  L2  L3', 13)
# clean stray symbol under meter2 terminals
cover(824, 276, 850, 292)

# ============ 5) clear invented display values (kept meters) ============
disp1 = ring_bg(640, 180, 780, 250, light=False)
cover(640, 182, 780, 248, color=disp1, noise=3, feather=False)
disp2 = ring_bg(830, 180, 930, 250, light=False)
cover(830, 182, 930, 248, color=disp2, noise=3, feather=False)
# write neutral meter text on displays
dk = sample_text_color(654, 167)
write(710, 215, '400/5A', 20, col=(90, 220, 120))
write(880, 215, '400/5A', 20, col=(90, 220, 120))

# ============ 6) Q0: WITH MOTOR ============
cover(268, 244, 380, 262)
write(324, 253, 'WITH MOTOR', 15)

# ============ 7) Q5: WITH MOTOR ============
cover(1060, 550, 1200, 568)
write(1130, 559, 'WITH MOTOR', 15)

# ============ 8) TRB-900 fixes ============
# MAX 5A
cover(852, 814, 922, 830)
write(887, 822, 'MAX 5A', 14)
# relay terminals spaced
cover(940, 792, 1012, 808)
write(976, 800, '18  15  16', 14)
# remove invented PV/SV values (059, 80.0) on display
trb_disp = ring_bg(805, 752, 955, 776, light=False)
cover(806, 750, 866, 772, color=trb_disp, noise=2, feather=False)
cover(900, 750, 958, 774, color=trb_disp, noise=2, feather=False)
cover(830, 772, 852, 782, color=trb_disp, noise=2, feather=False)
# add REL label next to SV (small LED label)
pv_col = sample_text_color(790, 762)
write(984, 762, 'REL', 13, col=pv_col)

# ============ 9) busbar labels L1 L2 L3 N PE (copper rows y 326..397) ============
bars = [('L1', 326), ('L2', 356), ('L3', 369), ('N', 386), ('PE', 397)]
for name, by in bars:
    # white bold with dark outline for contrast on copper
    d = ImageDraw.Draw(im)
    d.text((232, by), name, font=font(17), fill=(15,15,15), anchor='mm',
           stroke_width=2, stroke_fill=(255,255,255))

# ============ 10) M box on Q5 + dashed green command wire ============
d = ImageDraw.Draw(im)
# M box
bx0, by0, bx1, by1 = 1188, 500, 1232, 538
d.rounded_rectangle([bx0, by0, bx1, by1], radius=6, fill=(154,162,171), outline=(38,43,49), width=2)
d.text(((bx0+bx1)//2, (by0+by1)//2), 'M', font=font(20), fill=(20,24,30), anchor='mm')
d.line([(1170,519),(bx0,519)], fill=(38,43,49), width=2)
# dashed green wire: TRB terminals -> M box
def dashed_line(pt0, pt1, dash=12, gap=7, col=(26,122,26), wd=4):
    import math
    x0,y0 = pt0; x1,y1 = pt1
    L = math.hypot(x1-x0, y1-y0)
    n = int(L // (dash+gap)) + 1
    for i in range(n):
        t0 = (i*(dash+gap))/L; t1 = min(((i*(dash+gap))+dash)/L, 1)
        d.line([(x0+(x1-x0)*t0, y0+(y1-y0)*t0), (x0+(x1-x0)*t1, y0+(y1-y0)*t1)], fill=col, width=wd)
dashed_line((1000, 798), (1210, 798))
dashed_line((1210, 798), (1210, 560))
# arrowhead into M box
d.polygon([(1210,548),(1202,562),(1218,562)], fill=(26,122,26))

# ============ 11) SVA #3: copy clean meter1 module -> near CT7-9 ============
mod = im.crop((622, 116, 806, 296))   # meter1 module (already cleaned above)
# paste near Q5 CTs, below CT labels
im.paste(mod, (1252, 600))
# dashed measurement lead from CTs down to module
d2 = ImageDraw.Draw(im)
def dashed_gray(p0,p1):
    import math
    x0,y0=p0; x1,y1=p1; L=math.hypot(x1-x0,y1-y0)
    for i in range(int(L//9)+1):
        t0=min(i*9/L,1); t1=min((i*9+5)/L,1)
        d2.line([(x0+(x1-x0)*t0,y0+(y1-y0)*t0),(x0+(x1-x0)*t1,y0+(y1-y0)*t1)], fill=(110,110,110), width=2)
dashed_gray((1300, 586), (1300, 600))
# small caption for SVA3
write(1348, 700, '', 1)  # no-op keep

# ============ save ============
im.save(OUT)
print('saved', OUT, im.size)
