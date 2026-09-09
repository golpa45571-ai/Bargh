# -*- coding: utf-8 -*-
"""
inject_master_views.py — تزریق تصاویر master_views.json داخل BarghMaster.html

پایپ‌لاین:
    /tmp/mpl/bin/python render_master_views.py     # ساخت PNGها از make_master_drawing.py
    python3 inject_master_views.py                 # تزریق در تک‌فایل HTML

اسکریپت idempotent است: بلوک‌ها با مارکر <!--<<< … >>>--> / /*<<< … >>>*/ جابه‌جا می‌شوند.
"""
import io, os, re, json, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "BarghMaster.html")
DATA = os.path.join(HERE, "master_views.json")

imgs = json.load(io.open(DATA, encoding="utf-8"))

# ----------------------------------------------------------------  متا/شرح هر تصویر
META = {
    "panel":    ("تابلوی گرافیکی مدار — نمای جلو", "چیدمان فیزیکی تجهیزها در بays زونی، با همان مختصات و پالت کد نقشه", "render_master_views.py → بلوک‌های ZONE"),
    "bus":      ("شینهٔ پنج‌هادی اصلی", "R · S · T · N · PE با سطح مقطع 25*5Mm² CU و رایزرهای DI", "ناحیهٔ x=10…200 ، y=166…208"),
    "q0":       ("کلید اصلی Q0 و CT1…CT6", "شش CT روی رایزرهای ورودی: سه‌تا به DATA LOGGER و سه‌تا به KWH1", "ناحیهٔ x=38…124 ، y=90…178"),
    "mtr1":     ("DATA LOGGER و KWH1", "جعبه‌های اندازه‌گیری با ترمینال‌های 11₁…13₂", "ناحیهٔ x=114…268 ، y=96…182"),
    "sig":      ("F.KWH1&SIG و جعبه سیگنال", "کلید 6A سه‌فاز و KWH1 H1/H2/H3 با سیم‌های 35…44", "ناحیهٔ x=192…262 ، y=92…192"),
    "feeders":  ("فیدرهای Q1 · Q2 · Q3", "سه MCCB سه‌فاز 100A با شنت و خروجی R·S·T·N·E", "ناحیهٔ x=278…372 ، y=84…200"),
    "q5in":     ("Q5 · CT7…CT9 · KWH2 · MCB16", "خروجی 50·51·52 به سه کلید 125A می‌رود، نه از شینه", "ناحیهٔ x=330…470 ، y=84…200"),
    "ctrl":     ("ZONE 005 — رشته فرمان و تایمر", "X.KWH2 → S1 → بوبین R2 → N0 و شاخهٔ NO + TRB-900 → NC → شنت Q5", "ناحیهٔ x=280…402 ، y=6…88"),
    "aux":      ("مدارهای کمکی", "کنترل · پریز · روشنایی با فیوزها و کلیدهای S0/S1/S2", "ناحیهٔ x=88…282 ، y=36…84"),
    "zone001":  ("ZONE 001 — اندازه‌گیری و کلید اصلی", "همان چیزی که کد در این بلوک رسم می‌کند", "کادر خودکار بلوک ZONE 001"),
    "zone002":  ("ZONE 002 — مدارهای کمکی", "پریز، روشنایی و فیوزهای مرتبط", "کادر خودکار بلوک ZONE 002"),
    "zone003":  ("ZONE 003 — فیدرهای Q1 Q2 Q3", "سه کلید 100A و خروجی‌های زون 004", "کادر خودکار بلوک ZONE 003"),
    "zone004":  ("ZONE 004 — Q5 · CT7…9 · KWH2 · MCB", "تغذیهٔ گروه 125A از خروجی Q5", "کادر خودکار بلوک ZONE 004"),
    "zone005":  ("ZONE 005 — کنتاکت‌های کمکی، R2، تایمر، N0", "رشتهٔ فرمان و کنترل دما", "کادر خودکار بلوک ZONE 005"),
    "zone006":  ("ZONE 006 — سه کلید 1PHASE 125A", "تغذیه از نوارهای 50·51·52 و ریل‌های N/E زون", "کادر خودکار بلوک ZONE 006"),
}
ZKEYS = [k for k in sorted(imgs) if re.match(r"^zone\d{3}$", k)]

# ----------------------------------------------------------------  CSS
CSS = r"""
/*<<<SHOT_CSS>>>*/
.shot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:10px}
.shot-grid.wide{grid-template-columns:1fr}
.shot{margin:0;background:linear-gradient(180deg,#0f1a2b,#0a1220);border:1px solid var(--border);border-radius:11px;overflow:hidden;
      box-shadow:0 1px 0 rgba(255,255,255,.03) inset,0 10px 24px -18px #000}
.shot-bar{display:flex;align-items:center;gap:8px;padding:7px 9px;border-bottom:1px solid var(--border);flex-wrap:wrap}
.shot-bar .tag{font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;color:#0b1424;background:var(--accent);
               padding:1.5px 6px;border-radius:999px;font-weight:800}
.shot-bar b{font-size:12px;color:var(--ink)}
.shot-body{background:#fff;cursor:zoom-in;position:relative}
.shot-body img{display:block;width:100%;height:auto}
.shot-body::after{content:"⤢";position:absolute;right:8px;bottom:8px;font-size:14px;color:#33415a;
                  background:rgba(255,255,255,.82);border:1px solid #cbd5e1;border-radius:7px;padding:1px 7px;opacity:0;transition:.15s}
.shot:hover .shot-body::after{opacity:1}
.shot-foot{padding:6px 9px;font-size:10.5px;color:var(--dim);border-top:1px dashed var(--border);line-height:1.5}
.shot-zoom{position:fixed;inset:0;background:rgba(4,8,16,.93);z-index:9999;display:flex;flex-direction:column;
           padding:10px;backdrop-filter:blur(3px)}
.shot-zoom .zz-bar{display:flex;gap:8px;align-items:center;color:#dbe6f5;font-size:12.5px;padding:2px 4px 8px}
.shot-zoom .zz-body{flex:1;overflow:auto;background:#fff;border-radius:10px;padding:8px}
.shot-zoom .zz-body img{display:block;width:100%;image-rendering:auto}
.shot-zoom .zz-body.zoom1x img{width:auto;max-width:none}
/*<<</SHOT_CSS>>>*/"""

# ----------------------------------------------------------------  JS
JS = r"""
/*<<<MASTER_SHOTS>>>*/
/* ═══════════════════════════════════════════════════════════════════════
   تصاویر گرافیکی بخش‌ها — رندرشده از make_master_drawing.py
   (render_master_views.py → master_views.json → این بلوک)
   هیچ داده‌ای در این تصاویر نیست جز همان آنچه کد نقشه مادر رسم می‌کند.
   ═══════════════════════════════════════════════════════════════════════ */
const MASTER_IMG = %IMGJSON%;
const MASTER_META = %METAJSON%;

Object.assign(Views, {
  shotKeys(){ return Object.keys(MASTER_IMG); },
  shot(key, o){
    o = o || {};
    const src = MASTER_IMG[key]; if(!src) return '';
    const m = MASTER_META[key] || {};
    const t = o.t || m[0] || key, d = o.sub || m[1] || '', s = m[2] || '';
    return `<figure class="shot" id="shot-${key}">
      <figcaption class="shot-bar">
        <span class="tag">${U.esc(key)}</span><b>${U.esc(t)}</b>
        <span class="xs dim">${U.esc(d)}</span>
        <span style="flex:1"></span>
        <button class="btn xs" onclick="event.stopPropagation();Views.shotOpen('${key}')">⤢ تمام‌صفحه</button>
        <button class="btn xs" onclick="event.stopPropagation();Views.shotDl('${key}')">⬇ PNG</button>
      </figcaption>
      <div class="shot-body" onclick="Views.shotOpen('${key}')"><img src="${src}" alt="${U.esc(t)}" loading="lazy"></div>
      <div class="shot-foot xs dim">مبدأ: make_master_drawing.py · ${U.esc(s)} · رندر PNG بدون بازنویسی نقشه</div>
    </figure>`;
  },
  shotStrip(keys, title, sub, wide){
    const list = (keys || []).filter(k => MASTER_IMG[k]);
    if(!list.length) return '';
    return this.panel(title || 'تصاویر گرافیکی این بخش از نقشه مادر',
      sub || ('برش‌های برداری‌شده از همان بوم 486×216 — ' + list.length + ' تصویر'),
      `<div class="shot-grid${wide ? ' wide' : ''}">${list.map(k => this.shot(k)).join('')}</div>`);
  },
  _zz(){ let el = document.getElementById('shotZoom');
    if(!el){ el = document.createElement('div'); el.id = 'shotZoom'; el.className = 'shot-zoom';
      el.innerHTML = `<div class="zz-bar"><b id="zzT"></b><span class="xs dim" id="zzS"></span>
        <span style="flex:1"></span>
        <button class="btn xs" onclick="Views.zzZoom()">۱:۱ / جا‌کردن</button>
        <button class="btn xs" id="zzDl">⬇ PNG</button>
        <button class="btn xs bad" onclick="Views.shotClose()">✕ بستن</button></div>
        <div class="zz-body" id="zzB" onclick="Views.shotClose()"></div>`;
      document.body.appendChild(el);
      document.addEventListener('keydown', e => { if(e.key === 'Escape') Views.shotClose(); });
    }
    return el; },
  shotOpen(key){ const el = this._zz(), body = el.querySelector('#zzB');
    body.classList.remove('zoom1x');
    body.innerHTML = `<img src="${MASTER_IMG[key]}" alt="${U.esc(key)}">`;
    el.querySelector('#zzT').textContent = (MASTER_META[key] || [key])[0];
    el.querySelector('#zzS').textContent = (MASTER_META[key] || ['', ''])[1] + '  ·  ' + key;
    el.querySelector('#zzDl').onclick = (e) => { e.stopPropagation(); Views.shotDl(key); };
    el.style.display = 'flex'; this._zzKey = key; },
  zzZoom(){ const el = document.getElementById('shotZoom'); if(el) el.querySelector('#zzB').classList.toggle('zoom1x'); },
  shotClose(){ const el = document.getElementById('shotZoom'); if(el) el.style.display = 'none'; },
  shotDl(key){ const a = document.createElement('a'); a.href = MASTER_IMG[key];
    a.download = 'bargh_' + key + '.png'; document.body.appendChild(a); a.click(); a.remove(); },
  shotsFor(view){
    const map = {
      graphicpanel:['panel'],
      power:['bus','q0','feeders'],
      metering:['mtr1','sig'],
      aux:['aux','zone002'],
      control:['ctrl','zone005'],
      group125:['q5in','zone006'],
      zones: ['zone001','zone002','zone003','zone004','zone005','zone006'],
      protection:['q0','feeders','q5in'],
      equipment:['panel','q0'],
      terminals:['mtr1','zone006'],
      wires:['ctrl','aux'],
      bom:['panel','q0','mtr1'],
      faults:['bus','q0'],
      test:['zone006','q5in'],
      temperature:['ctrl'],
      powerflow:['bus','feeders','q5in'],
      overview:['panel'],
      fullmap:['panel','bus','q0','mtr1','feeders','q5in','ctrl','aux'],
      schematic:['bus','q0','mtr1','sig','feeders','q5in','ctrl','aux'],
      sheets: ['bus','q0','mtr1','sig','feeders','q5in','ctrl','aux'].concat(ZKEYS),
      dashboard:['panel','bus'],
      reports:['panel'],
      education:['panel','q0','mtr1','aux','ctrl','z006'],
      ai:['panel'],
      settings:[],
      validation:['panel'],
      audit:['panel']
    };
    return map[view] || [];
  }
});

/* تصاویر را بالای نمای مربوطه می‌چسباند (همان الگوی فایل نمونه: <img> + توضیح) */
(function(){
  const CAP = {
    graphicpanel: 'تابلوی گرافیکی مدار — پرتره از نمای جلوی تابلو',
    power:   'تصویر برداری‌شده از نقشه مادر — قدرت',
    metering:'تصویر برداری‌شده از نقشه مادر — اندازه‌گیری و سیگنال',
    aux:     'تصویر برداری‌شده از نقشه مادر — مدارهای کمکی',
    control: 'تصویر برداری‌شده از نقشه مادر — رشتهٔ فرمان',
    group125:'تصویر برداری‌شده از نقشه مادر — گروه 125A',
    zones:   'تصویر هر زون از همان بلوک کد (ZONE 001…006)',
    sheets:  'گالری کامل تصاویر بخش‌ها'
  };
  Object.keys(VIEWS_SHOT_WRAP || {}).length;
  const views = ['graphicpanel','power','metering','aux','control','group125','zones','protection',
                 'equipment','terminals','wires','bom','faults','test','temperature','powerflow',
                 'overview','fullmap','sheets','dashboard','reports','education','ai','validation','audit'];
  views.forEach(v => {
    const orig = Views[v]; if(!orig) return;
    Views[v] = function(){
      let head = '';
      try{
        const keys = Views.shotsFor(v);
        if(keys.length) head = Views.shotStrip(keys, CAP[v], null, v === 'graphicpanel' || v === 'fullmap');
      }catch(e){ console.warn('shots:' + v, e); }
      return head + orig.call(this);
    };
  });
})();
/*<<</MASTER_SHOTS>>>*/
"""

# ----------------------------------------------------------------  تزریق
html = io.open(HTML, encoding="utf-8").read()


def replace_block(text, start_marker, end_marker, block):
    if start_marker in text:
        a = text.index(start_marker)
        b = text.index(end_marker, a) + len(end_marker)
        return text[:a] + block + text[b:]
    return None


# 1) CSS → داخل بلوک <style> اول
sc = '</style>'
css_block = CSS
i = html.index(sc)
html = html[:i] + css_block + "\n" + html[i:]

# 2) JS → درست پیش از `const Nav = {`
js = JS.replace("%IMGJSON%", json.dumps(imgs, separators=(",", ":")))
js = js.replace("%METAJSON%", json.dumps({k: list(v) for k, v in META.items()}, ensure_ascii=False, separators=(",", ":")))
js = js.replace("ZKEYS", json.dumps(ZKEYS))
js = js.replace("  Object.keys(VIEWS_SHOT_WRAP || {}).length;\n", "")
anchor = "const Nav = {"
if "/*<<<MASTER_SHOTS>>>*/" in html:
    a = html.index("/*<<<MASTER_SHOTS>>>*/")
    b = html.index("/*<<</MASTER_SHOTS>>>*/") + len("/*<<</MASTER_SHOTS>>>*/")
    html = html[:a] + js + html[b:]
else:
    j = html.rindex(anchor)
    html = html[:j] + js + "\n\n" + html[j:]

# 3) نام بخش را عین فایل نمونه می‌کنیم
html = html.replace("{id:'graphicpanel',ic:'🖥', fa:'تابلو گرافیکی چیدمان', en:'Graphic Panel Layout'}",
                    "{id:'graphicpanel',ic:'🖼', fa:'تابلو گرافیکی مدار', en:'Graphical Panel Board'}")

io.open(HTML, "w", encoding="utf-8").write(html)
print("injected %d images (%.2f MB base64) → %s" % (len(imgs), sum(len(v) for v in imgs.values()) / 1048576.0, HTML))
