# -*- coding: utf-8 -*-
"""
render_master_views.py — تصویرساز بخش‌های BarghMaster.html

فقط سه فایل منبع نقشه مادر مصرف می‌شوند؛ هیچ داده‌ای از جای دیگر نمی‌آید:

  • make_master_drawing.py اجرا می‌شود (بدون ذخیرهٔ فایل اصلی).
  • متن کد به بلوک‌های «# ==== ZONE 00x » تقسیم می‌شود؛ هر بلوک جدا اجرا می‌شود و
    کادر هنرهای افزوده‌شده در همان بلوک جمع می‌شود ⇒ پنجرهٔ دقیق همان زون.
  • برای هر بخش، همان شکل با viewport جدید ذخیره می‌شود ⇒ تصویر، خودِ نقشه است.
  • «تابلوی گرافیکی مدار»: تجهیزها (متن‌های بولدِ Q0/M1/CT1/F.CONTROL/…) از همان
    بلوک‌ها برداشته می‌شوند و نمای جلوی تابلو با همان پالت C رسم می‌شود.

خروجی: master_views.json → {"key": "data:image/png;base64,…", …}
"""
import io, os, re, json, base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from PIL import Image as PILImage

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "make_master_drawing.py")
OUT = os.path.join(HERE, "master_views.json")

code = io.open(SRC, encoding="utf-8").read()
code = "\n".join(l for l in code.split("\n")
                 if "fig.savefig(" not in l and l.strip() != "print('saved')")

# ------------------------------------------------------------------ بلوک‌بندی کد
SEP = re.compile(r"^# =+\s*$")
lines = code.split("\n")
blocks, cur, curtitle = [], [], ""
for i, ln in enumerate(lines):
    if SEP.match(ln):
        nxt = next((lines[j] for j in range(i + 1, min(i + 4, len(lines))) if lines[j].strip() and not SEP.match(lines[j])), "")
        if nxt.strip().startswith("# ZONE") or nxt.strip().startswith("# TITLE") or \
           nxt.strip().startswith("# MAIN BUS") or nxt.strip().startswith("# FOOTER"):
            if curtitle or cur:
                blocks.append((curtitle, "\n".join(cur)))
            curtitle, cur = (nxt.strip().lstrip("# ").strip(), [])
            continue
    cur.append(ln)
if cur:
    blocks.append((curtitle, "\n".join(cur)))
if not any(b[0].startswith("ZONE") for b in blocks):        # ساختار غیرمنتظره → تک‌بلوک
    blocks, (curtitle, cur) = [("", code)], ("", [])

def _zkey(tag):
    m = re.search(r"(\d{3})", tag)
    return "zone" + (m.group(1) if m else re.sub(r"\W", "", tag)[:6].lower())


def _zshort(tag):
    t = re.sub(r"\s*[-\u2014]+\s*", " · ", tag.strip())
    return t if len(t) <= 30 else t[:28] + "…"


def dev_kind(tag):
    return ("mccb" if re.match(r"^(Q\d|MCCB|M\d$)", tag) else
            "ct" if tag.startswith("CT") else
            "fuse" if tag.startswith("F.") else
            "meter" if (tag.startswith("KWH") or "LOGGER" in tag or tag in ("NC", "N0")) else
            "switch" if (re.match(r"^S\d", tag) or tag == "LAMP") else "box")


TAG_RE = re.compile(r"^(Q\d+|M\d|CT\d+|KWH\d+|F\.[A-Z0-9]+|S\d|LAMP|MCB\d*|TIMER|NC|N0|R\d|MCCB|TERM\w*)$")


def parse_label(t):
    t = (t or "").strip()
    if not t:
        return None, None
    if "LOGGER" in t.upper():
        return "DATA LOGGER", "three-phase logger · I1…I3 + U"
    parts = [x.strip() for x in re.split(r"\s*[·—\-]\s*", t) if x.strip()]
    t0 = parts[0].replace(" ", "")
    if TAG_RE.match(t0):
        return t0, " · ".join(parts[1:])
    return None, None


ns = {"__name__": "master_views"}
ZONES, DEVICES = [], []
DEVICE_PAT = re.compile(r"^(Q\d|M\d|CT\d|KWH\d|F\.[A-Z0-9]+|S\d|LAMP|MCB\d+|TIMER|NC|N0|R\d)$")


def bbox_of(art):
    try:
        if isinstance(art, Rectangle):
            x, y = art.get_xy(); return (x, y, x + art.get_width(), y + art.get_height())
        if isinstance(art, Circle):
            cx, cy = art.center; r = art.radius; return (cx - r, cy - r, cx + r, cy + r)
        if hasattr(art, "get_xydata") and art.get_xydata() is not None and len(art.get_xydata()):
            a = art.get_xydata(); return (a[:, 0].min(), a[:, 1].min(), a[:, 0].max(), a[:, 1].max())
        if hasattr(art, "get_position"):
            x, y = art.get_position(); return (x, y, x, y)
    except Exception:
        return None
    return None


for title, body in blocks:
    ax0 = ns.get("ax")
    before = (len(ax0.patches), len(ax0.lines), len(ax0.texts)) if ax0 is not None else (0, 0, 0)
    exec(compile(body or "pass", SRC, "exec"), ns)
    ax = ns.get("ax")
    if ax is None or not title.startswith("ZONE"):
        continue
    arts_p, arts_l = list(ax.patches)[before[0]:], list(ax.lines)[before[1]:]
    bb = [bbox_of(a) for a in arts_p + arts_l]
    bb = [q for q in bb if q]
    if not bb:
        continue
    texts = [(t.get_position()[0], t.get_position()[1], (t.get_text() or "").strip(),
              float(t.get_fontsize() or 0), str(t.get_fontweight()), str(t.get_style()))
             for t in list(ax.texts)[before[2]:]]
    x0 = min(q[0] for q in bb); y0 = min(q[1] for q in bb)
    x1 = max(q[2] for q in bb); y1 = max(q[3] for q in bb)

    dev = []
    for (tx, ty, txt, size, wt, st) in texts:
        if wt != "bold" or size < 5.2:
            continue
        tag, desc = parse_label(txt)
        if not tag:
            continue
        best, bd = None, 1e9
        for q in bb:
            cx, cy = (q[0] + q[2]) / 2.0, (q[1] + q[3]) / 2.0
            d = max(abs(cx - tx), abs(cy - ty))
            if d < bd and 3.0 < (q[2] - q[0]) < 62 and 1.2 < (q[3] - q[1]) < 46:
                best, bd = q, d
        w = (best[2] - best[0]) if best else 12.0
        h = (best[3] - best[1]) if best else 8.0
        if not desc:
            cand = [t for t in texts if t[5] == "italic" and max(abs(t[0] - tx), abs(t[1] - ty)) < 17 and t[2]]
            if cand:
                desc = max(cand, key=lambda t: t[3])[2]
        dev.append(dict(tag=tag, desc=desc or "", x=tx, y=ty, w=w, h=h, zone=title,
                        kind=dev_kind(tag)))

    uniq, used = [], set()
    n_by_tag = {}
    for d in sorted(dev, key=lambda z: z["x"]):
        n_by_tag[d["tag"]] = n_by_tag.get(d["tag"], 0) + 1
        if n_by_tag[d["tag"]] > 1:
            if not re.match(r"^MCCB", d["tag"]):
                continue
            d["tag"] = "%s·%d" % (d["tag"], n_by_tag[d["tag"]])
        uniq.append(d)
    for d in uniq:
        DEVICES.append(d)
    ZONES.append(dict(tag=title, box=(x0, y0, x1, y1), devs=uniq, texts=texts))

W, H, C, DPI = ns["W"], ns["H"], ns["C"], ns["DPI"]
fig, ax = ns["fig"], ns["ax"]
for z in ZONES:
    z["key"], z["short"] = _zkey(z["tag"]), _zshort(z["tag"])

# ------------------------------------------------------------------ خروجی PNG
#   نقشه یک‌بار در اندازهٔ کامل رندر می‌شود، بعد هر ناحیه با برش دقیق پیکسلی
#   (نگاشت یکان→پیکسل = DPI/16.6 که از خودِ figsize در کد اصلی می‌آید) جدا می‌شود.
IMAGES = {}
RENDER_DPI = 232                      # ≈ یک‌سوم PNG اصلی؛ برای برش‌های تیز
_ppu = RENDER_DPI / 16.6               # pixel per drawing unit

fig.set_size_inches(W / 16.6, H / 16.6)
_buf = io.BytesIO()
fig.savefig(_buf, format="png", facecolor="white", dpi=RENDER_DPI)
_buf.seek(0)
FULL = PILImage.open(_buf).convert("RGB")
print("full raster:", FULL.size, "· %.0f px/unit" % _ppu)


def _save(key, im):
    q = im.quantize(colors=160, method=PILImage.MEDIANCUT, dither=PILImage.NONE)
    out = io.BytesIO()
    q.save(out, format="PNG", optimize=True)
    IMAGES[key] = "data:image/png;base64," + base64.b64encode(out.getvalue()).decode()
    print("  %-11s %5dx%-5d → %6.0f KB" % (key, im.size[0], im.size[1], len(out.getvalue()) / 1024.0))
    return len(out.getvalue())


def crop(key, x0, y0, x1, y1, maxw=1500):
    x0, y0 = max(0.0, x0), max(0.0, y0)
    x1, y1 = min(W, x1), min(H, y1)
    box = (int(round(x0 * _ppu)), int(round((H - y1) * _ppu)),
           int(round(x1 * _ppu)), int(round((H - y0) * _ppu)))
    box = (max(0, box[0]), max(0, box[1]), min(FULL.size[0], box[2]), min(FULL.size[1], box[3]))
    im = FULL.crop(box)
    if maxw and im.width > maxw:
        im = im.resize((maxw, max(1, int(im.height * maxw / im.width))), PILImage.LANCZOS)
    return _save(key, im)


def _zkey(tag):
    m = re.search(r"(\d{3})", tag)
    return "zone" + (m.group(1) if m else re.sub(r"\W", "", tag)[:6].lower())


def _zshort(tag):
    t = re.sub(r"\s*[-—]+\s*", " · ", tag.strip())
    return t if len(t) <= 30 else t[:28] + "…"


# 1) پنجرهٔ هر زون — کادر همان بلوک‌های کد
print("zone windows (از بلوک‌های make_master_drawing.py):")
for z in ZONES:
    x0, y0, x1, y1 = z["box"]
    z["key"], z["short"] = _zkey(z["tag"]), _zshort(z["tag"])
    crop(z["key"], x0 - 5, y0 - 5, x1 + 5, y1 + 7)

# 2) پنجرهٔ کارکردیِ مدارها (ناحیهٔ همان مدار روی بوم 486×216)
SECTIONS = {
    "bus":     (10, 166, 200, 208),   # شینهٔ پنج‌هادی + رایزرهای DI
    "q0":      (38,  90, 124, 178),   # Q0 و CT1…CT6
    "mtr1":    (114, 96, 268, 182),   # DATA LOGGER و KWH1
    "sig":     (192, 92, 262, 192),   # F.KWH1&SIG و SIGBOX
    "feeders": (278, 84, 372, 200),   # Q1 · Q2 · Q3
    "q5in":    (330, 84, 470, 200),   # Q5 و جریان‌های آن
    "ctrl":    (280,  6, 402,  88),   # رشته فرمان + تایمر
    "aux":     (88,  36, 282,  84),   # روشنایی · پریز · کنترل
}
print("circuit windows:")
for k, (x0, y0, x1, y1) in SECTIONS.items():
    crop(k, x0, y0, x1, y1)

# ------------------------------------------------------------------ 3) تابلوی گرافیکی مدار
BW2, BH2 = 300.0, 156.0
bfig = plt.figure(figsize=(BW2 / 16.6, BH2 / 16.6), dpi=DPI)
bax = bfig.add_axes([0, 0, 1, 1]); bax.set_xlim(0, BW2); bax.set_ylim(0, BH2); bax.axis("off")


def bt(x, y, s, size=5.6, color="#111", ha="left", weight="normal", style="normal", va="center"):
    bax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, weight=weight,
             style=style, zorder=9)


def bl(x1, y1, x2, y2, c="#111", lw=1.0):
    bax.plot([x1, x2], [y1, y2], color=c, lw=lw, solid_capstyle="round", zorder=7)


bax.add_patch(Rectangle((0, 0), BW2, BH2, fc="white", ec="none", zorder=0))
bax.add_patch(Rectangle((3.5, 3.5), BW2 - 7, BH2 - 7, fc="#f4f7fa", ec="#7d8fa3", lw=1.7, zorder=1))
bax.add_patch(Rectangle((6.5, 6.5), BW2 - 13, BH2 - 13, fc="white", ec="#c3cdd7", lw=0.9, zorder=2))
bax.add_patch(Rectangle((6.5, BH2 - 16.5), BW2 - 13, 10.0, fc="#0d2b45", ec="none", zorder=3))
bt(9, BH2 - 11.5, "GRAPHICAL PANEL BOARD  ·  front view", size=7.0, weight="bold", color="white")
bt(BW2 - 9, BH2 - 11.5, "layout: device coordinates of make_master_drawing.py  ·  ZONE bays in source order",
   size=4.9, ha="right", color="#bcd6ee", style="italic")

nrows = max(1, len(ZONES))
top, bot = BH2 - 19.0, 20.5
RH = (top - bot) / nrows
UNIT = {"mccb": 3.3, "ct": 1.25, "fuse": 1.35, "meter": 2.5, "switch": 1.05, "box": 1.8}
placed = 0
for ri, z in enumerate(ZONES):
    ry = top - ri * RH
    bax.add_patch(Rectangle((9.5, ry - RH + 2.6), BW2 - 19, RH - 3.4,
                            fc="#fbfdff", ec="#c3cdd7", lw=0.9, ls=(0, (6, 3)), zorder=3))
    bax.add_patch(Rectangle((12.5, ry - RH + 5.0), BW2 - 24, 1.5, fc="#dde4ec", ec="#9aa8b8", lw=0.4, zorder=3))
    bt(13.5, ry - RH + 6.9, "DIN RAIL 35 mm", size=3.7, color="#7d8fa3", weight="bold")
    lab = z.get("short") or z["tag"]
    bax.add_patch(Rectangle((BW2 - 9.5 - 34, ry - 3.0), 34, 3.2, fc="#0d2b45", ec="none", zorder=4))
    bt(BW2 - 9.5 - 17, ry - 1.4, lab, size=5.2, ha="center", weight="bold", color="white")
    items = sorted(z["devs"], key=lambda d: d["x"])
    if not items:
        continue
    total = sum(UNIT[d["kind"]] for d in items)
    step = (BW2 - 26) / max(total * 1.28, 1.0)
    cx = 14.0
    for d in items:
        w = max(4.4, UNIT[d["kind"]] * step * 0.9)
        hgt = min(RH - 15.5, 24.0) if d["kind"] == "mccb" else min(RH - 16.5, 18.5)
        by = ry - RH + 6.4
        fc = {"mccb": "#ffffff", "ct": "#fdeef0", "fuse": "#fff4f2",
              "meter": "#f4fdff", "switch": "#ffffff", "box": "#f7f7f7"}[d["kind"]]
        ec = {"mccb": "#111111", "ct": C["ct"], "fuse": C["red2"],
              "meter": C["cyanec"], "switch": "#111111", "box": "#111111"}[d["kind"]]
        bax.add_patch(Rectangle((cx, by), w, hgt, fc=fc, ec=ec, lw=1.15, zorder=5))
        if d["kind"] == "mccb":
            poles = 3 if d["tag"].startswith("Q") else 1
            for i in range(poles):
                px = cx + w * (i + 0.5) / poles
                bl(px, by + hgt - 2.6, px, by + hgt * 0.48, C[["R", "S", "T"][i % 3]], 1.3)
                bax.plot([px, px + 1.05], [by + hgt * 0.48, by + hgt * 0.48 + 1.4], color="#111", lw=0.9, zorder=8)
            bax.add_patch(Rectangle((cx + 0.9, by + 1.4), w - 1.8, 2.7, fc="white", ec="#111", lw=0.8, zorder=6))
            bt(cx + w / 2, by + 2.7, "I>", size=3.9, ha="center", weight="bold")
            if d["tag"] in ("Q0", "Q5"):
                bax.add_patch(Circle((cx + w + 2.2, by + 2.8), 1.35, fc="white", ec="#111", lw=0.9, zorder=6))
                bt(cx + w + 2.2, by + 2.8, "M", size=4.2, ha="center", weight="bold")
        elif d["kind"] == "ct":
            bax.add_patch(Rectangle((cx + w * 0.2, by + 2.2), w * 0.22, hgt - 4.4, color=C["ct"], zorder=6))
            bax.add_patch(Rectangle((cx + w * 0.58, by + 2.2), w * 0.22, hgt - 4.4, color=C["ct"], zorder=6))
            bt(cx + w / 2, by + hgt - 1.9, "400/5A", size=3.4, ha="center", color=C["ct"])
        elif d["kind"] == "fuse":
            bax.add_patch(Rectangle((cx + w * 0.24, by + hgt * 0.32), w * 0.52, hgt * 0.36,
                                    fc="white", ec=C["red2"], lw=1.0, zorder=6))
            bl(cx + w * 0.18, by + hgt * 0.22, cx + w * 0.82, by + hgt * 0.78, C["red2"], 0.9)
        elif d["kind"] == "meter":
            for i in range(6):
                yy = by + hgt - 2.0 - i * (hgt - 3.6) / 5.0
                bax.add_patch(Circle((cx + 1.4, yy), 0.5, fc="white", ec="#333", lw=0.7, zorder=7))
            bax.add_patch(Rectangle((cx + w * 0.42, by + hgt * 0.4), w * 0.44, hgt * 0.28,
                                    fc="#0f1d2b", ec="#333", lw=0.7, zorder=6))
            bt(cx + w * 0.64, by + hgt * 0.54, "kWh", size=3.5, ha="center", color="#8fd6ff")
        else:
            bl(cx + 1.3, by + hgt * 0.46, cx + w - 2.8, by + hgt * 0.46, "#111", 1.0)
            bax.plot([cx + w - 2.8, cx + w - 1.2], [by + hgt * 0.46, by + hgt * 0.74], color="#111", lw=0.95, zorder=8)
        bt(cx + w / 2, by - 2.0, d["tag"], size=4.9, ha="center", weight="bold")
        if d.get("desc"):
            ds = d["desc"] if len(d["desc"]) <= 28 else d["desc"][:26] + "…"
            bt(cx + w / 2, by - 4.6, ds, size=3.4, ha="center", color="#4a5a6a", style="italic")
        cx += w + max(2.0, step * 0.3)
        placed += 1
    bt(BW2 - 12.5, ry - RH + 6.9, "%d devices" % len(items), size=4.0, ha="right", color="#4a5a6a", style="italic")

by = ns.get("by") or dict(R=196, S=191.5, T=187, N=182.5, E=178)
bt(12, BH2 - 20.2, "BUS 25*5Mm² CU  ·  R/S/T/N/PE", size=4.8, weight="bold", color="#0d2b45")
for i, (k, col) in enumerate([("R", C["R"]), ("S", C["S"]), ("T", C["T"]), ("N", C["N"]), ("PE", C["E"])]):
    yy = 15.0 - i * 2.0
    bl(12, yy, BW2 - 12, yy, col, 1.35)
    bt(BW2 - 11, yy, k, size=4.0, ha="right", color=col, weight="bold")
bt(12, 4.6, "device set & positions read from the same drawing script · %d devices in %d zone bays"
   % (placed, len(ZONES)), size=4.5, color="#4a5a6a", style="italic")
_bb = io.BytesIO()
bfig.savefig(_bb, format="png", facecolor="white", dpi=210)
plt.close(bfig); _bb.seek(0)
_p = PILImage.open(_bb).convert("RGB")
if _p.width > 1900:
    _p = _p.resize((1900, int(_p.height * 1900 / _p.width)), PILImage.LANCZOS)
_save("panel", _p)

# ------------------------------------------------------------------ 4) ذخیره
io.open(OUT, "w", encoding="utf-8").write(json.dumps(IMAGES))
tot = sum(len(v) for v in IMAGES.values())
print("zones=%d · devices=%d · %d images · %.2f MB base64 → %s"
      % (len(ZONES), placed, len(IMAGES), tot / 1048576.0, OUT))
