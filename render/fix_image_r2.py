# -*- coding: utf-8 -*-
"""Round-2 pixel fixes: label spacing, busbar labels placement, REL visibility."""
from PIL import Image, ImageDraw, ImageFont
import numpy as np

im = Image.open('/home/user/Bargh/render/panel_final_fixed.png').convert('RGB')
W, H = im.size
arr = np.array(im).astype(int)

FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FR = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def font(sz, bold=True): return ImageFont.truetype(FB if bold else FR, sz)

def ring_bg(x0, y0, x1, y1, margin=10, light=True):
    X0, Y0, X1, Y1 = max(0,x0-margin), max(0,y0-margin), min(W,x1+margin), min(H,y1+margin)
    m = np.zeros((Y1-Y0, X1-X0), bool)
    m[:margin,:] = True; m[-margin:,:] = True; m[:,:margin] = True; m[:,-margin:] = True
    reg = arr[Y0:Y1, X0:X1]
    lum = reg.mean(axis=2)
    sel = m & (lum > 120) if light else m & (lum < 120)
    if sel.sum() < 20: sel = m
    return tuple(int(v) for v in np.median(reg[sel], axis=0))

def cover(x0, y0, x1, y1, color=None, noise=5):
    if color is None: color = ring_bg(x0,y0,x1,y1)
    rng = np.random.default_rng(7)
    patch = np.clip(np.array(color) + rng.normal(0, noise, (y1-y0, x1-x0, 3)), 0, 255).astype(np.uint8)
    im.paste(Image.fromarray(patch), (x0, y0))

def write(x, y, txt, sz=14, col=(28,34,42), anchor='mm'):
    ImageDraw.Draw(im).text((x,y), txt, font=font(sz), fill=col, anchor=anchor)

# A) incomer CT ratio rows — one clean strip, three compact labels
cover(388, 96, 596, 112)
for cx in (432, 490, 546): write(cx, 104, '400/5A', 11)
cover(388, 228, 596, 244)
for cx in (432, 490, 546): write(cx, 236, '400/5A', 11)

# B) CT7-9 ratios (lower band, do not touch CT names at y≈559)
cover(1245, 566, 1400, 586)
for cx in (1273, 1322, 1372): write(cx, 576, '400/5A', 10)

# C) meter1 terminal row + POWER SUPPLY (no overlap)
cover(545, 131, 748, 153)
write(640, 142, 'I1 I1  I2 I2  I3 I3', 11)
cover(735, 129, 818, 149)
write(776, 138, 'POWER SUPPLY', 10)

# D) Q0 WITH MOTOR — clean wide patch
cover(260, 245, 388, 263)
write(324, 254, 'WITH MOTOR', 14)

# E) relay terminals — wide patch
cover(928, 791, 1026, 809)
write(977, 800, '18   15   16', 13)

# F) REL in bright white (was invisible dark-on-dark)
write(986, 762, 'REL', 12, col=(250, 250, 250))

# G) busbar labels — remove old, place per detected copper extents, alternate sides
# cover old L1 & N labels drawn at x≈225
for cy in (326, 386):
    col = ring_bg(215, cy-10, 250, cy+10, light=False)   # copper-ish
    cover(215, cy-10, 250, cy+10, color=col, noise=8)
r,g,b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
copper = (r>150)&(r<230)&(g>80)&(g<150)&(b<95)
d = ImageDraw.Draw(im)
bars = [('L1',326),('L2',356),('L3',369),('N',386),('PE',397)]
for i,(name,by) in enumerate(bars):
    row = copper[by-2:by+3].any(axis=0)
    xs = np.where(row)[0]
    if len(xs)==0: continue
    xL, xR = int(xs.min()), int(xs.max())
    if i % 2 == 0:
        tx = max(60, xL - 28)
    else:
        tx = min(W-40, xR + 30)
    d.text((tx, by), name, font=font(15), fill=(15,15,15), anchor='mm',
           stroke_width=2, stroke_fill=(255,255,255))

# H) PSU texts with proper spacing
for cx in (330, 560):
    cover(cx-46, 797, cx+46, 815);  write(cx, 806, 'POWER SUPPLY', 12)
    cover(cx-36, 813, cx+36, 831);  write(cx, 822, 'AC 230V', 12)

# I) Q5 WITH MOTOR — wider spacing
cover(1058, 550, 1202, 568)
write(1130, 559, 'WITH MOTOR', 14)

im.save('/home/user/Bargh/render/panel_final_fixed.png')
print('round-2 saved')
