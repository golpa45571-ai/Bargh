# پرامپت رسم گرافیکی مدار برای هوش مصنوعی تصویرساز
### Circuit-to-Graphic AI Prompt — built from the definitive audit of all 7 PDFs (totall + 001–006)

> **نحوه‌ی استفاده:** عکس نمونه (سبک مورد نظرتان) را همراه این پرامپت به مدل تصویرساز بدهید.
> پرامپت انگلیسی را ترجیحاً استفاده کنید (دقت مدل‌ها در انگلیسی بالاتر است). پرامپت فارسی برای مدل‌های چندزبانه ضمیمه شده.

---

## 📋 PROMPT (English) — copy everything inside the box

```
Using the attached image as a STYLE REFERENCE ONLY (match its visual style, illustration
technique and numbered-callout layout), create a clean, high-resolution educational
infographic of an industrial 3-phase electrical distribution panel.

⚠ FIDELITY RULE — this reproduces a real engineering drawing: do NOT add, remove, merge,
split or rename any component, tag, rating or wire. Every number and letter below is exact.

PANEL LAYOUT — one enclosure: power section on top, control compartment at the bottom.

A) INCOMING & MAIN BREAKER (left side):
- A 3-phase + neutral power cable enters the enclosure from the BOTTOM and runs upward.
- Main incomer: large 3-pole molded-case circuit breaker with a motor-operator mechanism
  (small actuator box marked "M") mounted on its side.
- Exact labels: "Q0" and "MCCB 3 PHASE 250A WITH MOTOR"

B) INCOMER METERING (on the 3 phase conductors between Q0 and the busbar):
- Two separate groups of three donut current transformers = 6 CTs total:
  Group 1: "CT1 400/5A", "CT2 400/5A", "CT3 400/5A"
  Group 2: "CT4 400/5A", "CT5 400/5A", "CT6 400/5A"
- Two identical digital multifunction meters, dark modules with green numeric displays,
  labeled "SVA" (SVA #1 wired to CT1–CT3, SVA #2 wired to CT4–CT6), each with thin
  voltage-sense wires tapped from the busbar (terminals marked N, L1, L2, L3).
  Both meters measure the same incoming feeder — this duplication is intentional. Keep both.

C) MAIN BUSBAR (horizontal, near the top):
- Three copper phase bars "L1", "L2", "L3" + neutral bar "N" + earth bar "PE",
  mounted on small insulators.

D) OUTGOING FEEDERS — breaker row hanging from the busbar, left to right,
   EXACTLY these 9 feeders:
  1. "Lighting" — 3-pole MCCB, label exactly "Lighting" (NO amperage text on this one)
  2. "Q1 — MCCB 100A" (3-pole)
  3. "Q2 — MCCB 100A" (3-pole)
  4. "Q3 — MCCB 100A" (3-pole)
  5–7. Three separate SINGLE-POLE MCCBs, each labeled "MCCB 125A". CRITICAL: each is fed
      from a DIFFERENT phase — first from L1, second from L2, third from L3 — each with
      its own neutral (N) and earth (PE) connection.
  8. "Q5 — MCCB 3PHASE 100A WITH MOTOR" — 3-pole breaker with motor-operator box "M",
      plus its own three CTs: "CT7 400/5A", "CT8 400/5A", "CT9 400/5A", and a third
      digital meter labeled "SVA" (SVA #3) with voltage taps from the busbar.
- Each feeder has a short downward arrow indicating its load.

E) CONTROL COMPARTMENT (bottom strip, separated by a horizontal divider):
- Two identical switched-mode power-supply modules, each labeled exactly
  "POWER SUPPLY AC 230V", each fed through its own small protective breaker mounted
  above it — one tagged "Q0", the other tagged "Q5" (these repeated tags exist in the
  original drawing; keep them EXACTLY as they are).
- One panel-mount digital TEMPERATURE CONTROLLER, dark faceplate:
  brand "SHIVA AMVAJ", model "TRB-900", "CODE: 15B2", title "TEMPERATURE CONTROLLER",
  display fields "PV", "SV", "REL", spec texts "180-250 VAC" and "MAX 5A",
  relay terminals "15", "16", "18", supply terminals "PH" and "N".
- One dashed green CONTROL WIRE from the TRB-900 relay terminals (15/16/18) running up
  to the motor-operator "M" of breaker Q5 — the temperature controller automatically
  switches feeder Q5 ON/OFF.

STYLE (from the attached reference): open-panel semi-realistic technical illustration,
red numbered callout dots on components, clean light background, copper busbars, dark
breaker bodies with light toggle levers, digital meter faces; optional Farsi side legend
exactly like the reference image. Landscape 16:9.

IF A SIDEBAR LEGEND IS INCLUDED, use exactly these Farsi items:
۱ کابل ورودی سه‌فاز + نول | ۲ کلید اصلی Q0 — ۲۵۰ آمپر موتوری | ۳ ترانس جریان CT1 تا CT6 — 400/5
۴ مترهای SVA (دو عدد) | ۵ باسبار L1 L2 L3 N PE | ۶ فیدر روشنایی | ۷ فیدرهای Q1 تا Q3 — ۱۰۰ آمپر
۸ سه فیدر تک‌فاز ۱۲۵ آمپر (L1/L2/L3) | ۹ فیدر Q5 موتوری + CT7 تا CT9 + SVA | ۱۰ کنترلر دما TRB-900
۱۱ منابع تغذیه ۲۳۰ ولت فرمان

TEXTS THAT MUST APPEAR VERBATIM (case-sensitive):
Q0, Q1, Q2, Q3, Q5, MCCB, 250A, 100A, 125A, 3PHASE, 3 PHASE, WITH MOTOR,
CT1, CT2, CT3, CT4, CT5, CT6, CT7, CT8, CT9, 400/5A, SVA, Lighting,
POWER SUPPLY AC 230V, SHIVA AMVAJ, TRB-900, CODE: 15B2, TEMPERATURE CONTROLLER,
180-250 VAC, MAX 5A, PV, SV, REL, PH, N, L1, L2, L3, PE, 15, 16, 18.

STRICT DO-NOT LIST:
- Do NOT add any component that is not listed (no contactors, fuses, indicator lamps,
  selector switches, UPS, generator, or fan graphics).
- Do NOT change any amperage (250A / 100A / 125A), CT ratio (400/5A), or tag (Q0…Q5).
- Do NOT merge the two SVA meters or the two CT groups; all 9 CTs must be present.
- Do NOT draw the three 125A breakers as 3-pole — they are SINGLE-pole, one per phase.
- Do NOT reverse the power direction: cable enters at the BOTTOM, busbar at the TOP.
- Device labels stay in ENGLISH exactly as given; only the legend/callouts may be Farsi.
```

---

## 📋 پرامپت (فارسی) — برای مدل‌های چندزبانه

```
تصویر پیوست‌شده فقط مرجع سبک است (همان سبک Illustrator، مرتب و تمیز). یک اینفوگرافیک آموزشی باکیفیت و رزولوشن بالا از یک تابلوی توزیع برق صنعتی سه‌فاز بساز.

⚠ قانون وفاداری: این بازسازی یک نقشه‌ی مهندسی واقعی است. هیچ قطعه، تگ، آمپراژ یا سیمی را اضافه، حذف، ادغام یا تغییر نام نده. همه‌ی اعداد و حروف دقیق‌اند.

چیدمان تابلو: بخش قدرت در بالا، محفظه‌ی فرمان در پایین.

الف) ورودی (سمت چپ):
- کابل سه‌فاز + نول از پایین تابلو وارد و به سمت بالا می‌رود.
- کلید اصلی: MCCB سه‌پل بزرگ با آپراتور موتوری (جعبه‌ی کوچک با حرف «M» کنار کلید).
- برچسب‌های دقیق: «Q0» و «MCCB 3 PHASE 250A WITH MOTOR»

ب) اندازه‌گیری ورودی (روی سه هادی فاز بین Q0 و باسبار):
- دو گروه جداگانه‌ی ترانس جریان دوناتی، هر گروه ۳ عدد = ۶ CT:
  گروه ۱: «CT1 400/5A»، «CT2 400/5A»، «CT3 400/5A»
  گروه ۲: «CT4 400/5A»، «CT5 400/5A»، «CT6 400/5A»
- دو متر دیجیتال چندعملکردی یکسان (ماژول تیره با نمایشگر عددی سبز) با برچسب «SVA»
  (SVA اول به CT1 تا CT3 و SVA دوم به CT4 تا CT6 متصل است) + سیم‌های نازک تپ ولتاژ از
  باسبار به هر متر (ترمینال‌های N، L1، L2، L3). هر دو متر ورودیِ واحد را می‌سنجند؛ این
  تکرار عمدی است — هر دو را نگه دار.

ج) باسبار اصلی (افقی، نزدیک بالای تابلو):
- سه شینه‌ی مسی «L1»، «L2»، «L3» + شینه‌ی نول «N» + شینه‌ی ارت «PE» روی مقره.

د) فیدرهای خروجی — ردیف کلیدها آویزان از باسبار، از چپ به راست، دقیقاً این ۹ فیدر:
  ۱. «Lighting» — MCCB سه‌پل، برچسب فقط «Lighting» (بدون متن آمپراژ!)
  ۲. «Q1 — MCCB 100A» (سه‌پل)
  ۳. «Q2 — MCCB 100A» (سه‌پل)
  ۴. «Q3 — MCCB 100A» (سه‌پل)
  ۵ تا ۷. سه کلید MCCB تک‌پل با برچسب «MCCB 125A». حیاتی: هر کلید از یک فاز جداگانه
      تغذیه می‌شود — اولی از L1، دومی از L2، سومی از L3 — هر کدام با N و PE خودش.
  ۸. «Q5 — MCCB 3PHASE 100A WITH MOTOR» — سه‌پل با آپراتور موتوری «M» + سه CT خودش:
      «CT7 400/5A»، «CT8 400/5A»، «CT9 400/5A» + متر دیجیتال سوم «SVA» با تپ ولتاژ از باسبار.
- زیر هر فیدر یک فلش کوچک رو به پایین (نشان بار).

هـ) محفظه‌ی فرمان (نوار پایین، با خط جداکننده):
- دو ماژول منبع تغذیه‌ی یکسان با برچسب دقیق «POWER SUPPLY AC 230V»، هرکدام با کلید
  محافظ کوچک بالای خودش (یکی با تگ «Q0» و دیگری با تگ «Q5» — این تگ‌های تکراری در نقشه‌ی
  اصلی وجود دارند؛ دقیقاً همین‌طور نگهش دار).
- یک کنترلر دما تابلویی با پنل تیره: برند «SHIVA AMVAJ»، مدل «TRB-900»، «CODE: 15B2»،
  عنوان «TEMPERATURE CONTROLLER»، فیلدهای نمایشگر «PV»، «SV»، «REL»، متن مشخصات
  «180-250 VAC» و «MAX 5A»، ترمینال‌های رله «15»، «16»، «18»، ترمینال تغذیه «PH» و «N».
- یک سیم فرمان خط‌چین سبز از ترمینال‌های رله‌ی TRB-900 (15/16/18) به آپراتور موتوری «M»
  کلید Q5 — کنترلر دما، فیدر Q5 را خودکار وصل/قطع می‌کند.

سبک (مطابق عکس مرجع): تصویرسازی فنی نیمه‌واقعی از تابلو با درب باز، نقاط شماره‌گذاری قرمز
روی اجزا، پس‌زمینه‌ی روشن و تمیز، شینه‌های مسی، بدنه‌ی تیره‌ی کلیدها با اهرم روشن، نمایشگر
دیجیتال مترها؛ کنار تصویر راهنمای فارسی مثل عکس مرجع. کادر افقی ۱۶:۹.

متن‌هایی که باید عیناً (حرف‌به‌حرف) در تصویر بیایند:
Q0, Q1, Q2, Q3, Q5, MCCB, 250A, 100A, 125A, 3PHASE, 3 PHASE, WITH MOTOR, CT1 … CT9,
400/5A, SVA, Lighting, POWER SUPPLY AC 230V, SHIVA AMVAJ, TRB-900, CODE: 15B2,
TEMPERATURE CONTROLLER, 180-250 VAC, MAX 5A, PV, SV, REL, PH, N, L1, L2, L3, PE, 15, 16, 18.

ممنوع مطلق:
- افزودن هر قطعه‌ی فهرست‌نشده (کنتاکتور، فیوز، چراغ سیگنال، سوییچ انتخابگر، UPS، ژنراتور، فن).
- تغییر آمپراژ (250A / 100A / 125A)، نسبت CT (400/5A) یا تگ‌ها (Q0 تا Q5).
- ادغام دو متر SVA یا دو گروه CT؛ هر ۹ CT باید باشند.
- کشیدن سه کلید 125A به‌صورت سه‌پل — تک‌پل‌اند، هرکدام از یک فاز.
- برعکس‌کردن جهت تغذیه: کابل از پایین وارد می‌شود، باسبار بالاست.
- برچسب تجهیزات انگلیسی بماند؛ فقط راهنمای کنار تصویر فارسی باشد.
```

---

## ✅ چک‌لیست تأیید خروجی (بعد از تولید تصویر، با این فهرست مقایسه کنید)

| # | مورد صحت‌سنجی | مقدار صحیح |
|---|---|---|
| 1 | تعداد فیدرهای خروجی | دقیقاً ۹ (Lighting، Q1، Q2، Q3، سه×125A، Q5) |
| 2 | تعداد CT | دقیقاً ۹ (CT1 تا CT9، همگی 400/5A) |
| 3 | تعداد متر SVA | دقیقاً ۳ |
| 4 | تعداد منبع تغذیه | دقیقاً ۲ (POWER SUPPLY AC 230V) |
| 5 | کلیدهای موتوری | ۲ عدد: Q0 (250A) و Q5 (100A) با جعبه M |
| 6 | سه کلید 125A | تک‌پل؛ اولی L1، دومی L2، سومی L3 |
| 7 | فیدر Lighting | فقط برچسب Lighting — بدون آمپراژ |
| 8 | ورودی کابل | از پایین تابلو |
| 9 | کنترلر دما | فقط یک TRB-900 با PV/SV/REL و 15/16/18 |
| 10 | مسیر فرمان | رله‌ی TRB-900 ← آپراتور موتوری Q5 |

## 💡 نکات کاربردی
1. **عکس نمونه را حتماً همراه پرامپت پیوست کنید** — جمله‌ی اول پرامپت به آن ارجاع می‌دهد.
2. بهترین مدل‌ها برای متن دقیق داخل تصویر: **Gemini (Imagen/Nano Banana)**، **GPT-4o image** و **Flux**؛ مدل‌های دیگر معمولاً متن‌ها را خراب می‌کنند.
3. اگر متن‌ها غلط املایی داشتند، در پیام دوم فقط بگویید: «فقط متن‌های روی اجزا را اصلاح کن، بقیه‌ی تصویر دست‌نخورده بماند» و لیست verbatim را دوباره بدهید.
4. اگر تعداد اجزا کم/زیاد شد، همان چک‌لیست بالا را به‌عنوان پیام اصلاحی بفرستید.
5. خروجی را Landscape 16:9 و بزرگ بخواهید تا متن‌ها خوانا باشند.
