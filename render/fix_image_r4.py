"""Round 4: seamless background rebuild for removed-element areas.
Patch 1 (removed SVA meters 3&4): per-column vertical interpolation between
  robust, horizontally smoothed reference bands above/below.
Patch 2 (removed 4th 125A breaker): per-row left anchor from the real gap
  strip (x986-997) + horizontal bg slope fitted from a clean band above.
"""
from PIL import Image
import numpy as np

P = '/home/user/Bargh/render/panel_final_fixed.png'
img = np.array(Image.open(P).convert('RGB')).astype(float)
rng = np.random.default_rng(11)


def bad(px):
    """mask green wire, very dark pixels"""
    m = px.mean(axis=-1)
    g = (px[..., 1] > px[..., 0] + 18) & (px[..., 1] > px[..., 2] + 18)
    return g | (m < 65)


def colref_robust(y0, y1, x0, x1):
    """per-column clean background color from a row band, outlier-trimmed and
    horizontally smoothed (running median) so cables/shadows don't leak in"""
    band = img[y0:y1, x0:x1]
    m = ~bad(band)
    w = x1 - x0
    out = np.full((w, 3), np.nan)
    for j in range(w):
        v = band[m[:, j], j]
        if len(v) >= 3:
            med = np.median(v, axis=0)
            close = v[np.abs(v - med).mean(axis=1) < 28]
            out[j] = np.median(close if len(close) >= 3 else v, axis=0)
    idx = np.arange(w)
    good = ~np.isnan(out[:, 0])
    for c in range(3):
        out[:, c] = np.interp(idx, idx[good], out[good, c])
    win = 25
    sm = out.copy()
    for c in range(3):
        pad = np.pad(out[:, c], win // 2, mode='edge')
        sm[:, c] = np.array([np.median(pad[i:i + win]) for i in range(w)])
    return sm


# ---------- PATCH 1 : removed meters, x935..1330 y112..305 ----------
x0, y0, x1, y1 = 935, 112, 1330, 305
top = colref_robust(88, 108, x0, x1)
bot = colref_robust(307, 318, x0, x1)
h, w = y1 - y0, x1 - x0
t = np.linspace(0, 1, h)[:, None, None]
field = top[None] * (1 - t) + bot[None] * t
img[y0:y1, x0:x1] = np.clip(field + rng.normal(0, 3.2, (h, w, 3)), 0, 255)

# ---------- PATCH 2 : removed 4th 125A, x1000..1085 y462..605 ----------
x0, y0, x1, y1 = 1000, 462, 1085, 605
h, w = y1 - y0, x1 - x0
L = np.full((h, 3), np.nan)
for i, y in enumerate(range(y0, y1)):
    v = img[y, 986:998]
    m = ~bad(v[None, :])[0]
    if m.sum() >= 4:
        L[i] = np.median(v[m], axis=0)
ok = ~np.isnan(L[:, 0])
yy = np.arange(h)
for c in range(3):
    L[:, c] = np.interp(yy, yy[ok], L[ok, c])
# horizontal bg slope from clean band above feeder row
band = img[438:452, 950:1250]
m = ~bad(band)
ys, xs = np.where(m)
vals = band[m]
A = np.stack([xs.astype(float), np.ones_like(xs, dtype=float)], 1)
slope = np.linalg.lstsq(A, vals, rcond=None)[0][0]
print('bg slope per 100px:', (slope * 100).round(1))
xr = (np.arange(x0, x1) - 992)[None, :, None].astype(float)
field = L[:, None, :] + slope[None, None, :] * xr
img[y0:y1, x0:x1] = np.clip(field + rng.normal(0, 3.2, (h, w, 3)), 0, 255)

Image.fromarray(img.astype(np.uint8)).save(P)

# ---------- verify ----------
b = np.array(Image.open(P).convert('L')).astype(float)
print('P1 row200:', {c: int(b[200, c]) for c in [933, 936, 1050, 1200, 1290, 1329, 1331, 1335]})
print('P1 row290:', {c: int(b[290, c]) for c in [936, 1050, 1200, 1329]})
print('P2 row means:', {y: int(b[y, 1005:1086].mean()) for y in [462, 470, 500, 540, 570, 595, 604]})
print('P2 gap / fill-left / fill-right @row500:',
      int(b[500, 986:998].mean()), int(b[500, 1000:1012].mean()), int(b[500, 1073:1085].mean()))
print('P2 bottom edge 604/605:', int(b[604, 1005:1086].mean()), int(b[605, 1005:1086].mean()))
print('P1 interior max col-jump:', int(np.abs(np.diff(b[150:290, 940:1325], axis=1)).max()))
print('P2 interior max col-jump:', int(np.abs(np.diff(b[465:600, 1005:1082], axis=1)).max()))
g2 = np.array(Image.open(P).convert('RGB')).astype(float)[462:605, 1000:1085]
grn = (g2[:, :, 1] > g2[:, :, 0] + 20) & (g2[:, :, 1] > g2[:, :, 2] + 20)
print('green inside P2:', int(grn.sum()))
