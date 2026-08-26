# 🎯 پرامپت نهایی — نسخه‌ی ۲ (دقیق‌تر، مبتنی بر جزئیات ۶ فایل 001–006)
> **روش استفاده:** این پرامپت را کپی کنید + عکس نمونه‌ی خودتان را پیوست کنید → به مدل تصویرساز (ترجیحاً Gemini / Nano Banana یا GPT-4o image) بدهید.

---

## 🔵 PROMPT — copy this whole block (English, recommended)

```
The attached image is my STYLE REFERENCE. Copy its exact visual style: same illustration
technique, same colors, same panel rendering, same callout/labeling style, same legend
layout. But the CONTENT must come 100% from the engineering specification below — this is
a real single-line diagram redrawn as a panel graphic. Do not add, remove, merge, rename
or alter ANY component, wire, tag, number or rating. Render every label text EXACTLY as
written, letter-for-letter.

Build ONE industrial 3-phase low-voltage distribution panel (open enclosure, power section
on top, control compartment at the bottom) with EXACTLY this structure:

—— A) INCOMING & MAIN BREAKER (left side) —— [per sheet 001]
• A 3-phase + neutral (+ earth) cable enters the enclosure from the BOTTOM and rises up.
• Main breaker: 3-pole molded-case circuit breaker, 250 A, with motor-operator mechanism:
  a small actuator box marked "M" mechanically linked to the breaker.
• Exact label texts:  "Q0"   |   "MCCB 3 PHASE 250A WITH MOTOR"

—— B) INCOMER METERING —— [per sheet 001, drawn at terminal level]
• On the three phase conductors between Q0 and the busbar sit TWO independent groups of
  donut current transformers — 3 CTs per group, 6 CTs total, ALL rated 400/5A:
    Group 1:  "CT1 400/5A"   "CT2 400/5A"   "CT3 400/5A"
    Group 2:  "CT4 400/5A"   "CT5 400/5A"   "CT6 400/5A"
• TWO identical digital multifunction meters, each a dark module with a green numeric
  display, labeled "SVA". Each meter has:
    – 6 current terminals marked:  I1 I1 · I2 I2 · I3 I3   (CT secondary loop in/out)
    – 4 voltage terminals marked:  N · L1 · L2 · L3        (thin sense wires from busbar)
    – the first meter additionally shows aux terminals labeled "POWER SUPPLY"
• Meter #1 (SVA) is wired to CT1–CT3, meter #2 (SVA) to CT4–CT6. Both measure the SAME
  incoming feeder — duplication is intentional. Keep both.

—— C) MAIN BUSBAR (horizontal, top area) ——
• Three copper phase bars labeled "L1" "L2" "L3", a neutral bar "N" and an earth bar "PE",
  mounted on insulators.

—— D) OUTGOING FEEDERS — exactly NINE breakers hanging from the busbar, left to right ——
 1. "Lighting" — 3-pole MCCB. Label text is ONLY the word "Lighting" (no amperage text).
 2. "Q1" — 3-pole MCCB, "100A", feeding a 3-phase + N + PE circuit.   [sheet 003]
 3. "Q2" — 3-pole MCCB, "100A", 3-phase + N + PE.                      [sheet 003]
 4. "Q3" — 3-pole MCCB, "100A", 3-phase + N + PE.                      [sheet 003]
 5–7. THREE separate SINGLE-POLE MCCBs, each "125A".                    [sheet 006]
     CRITICAL: each is tapped from a DIFFERENT phase — #1 from L1, #2 from L2, #3 from L3 —
     each with its own neutral and PE conductor (single-phase 3-wire circuits).
 8. "Q5" — 3-pole MCCB, "100A", "3PHASE", "WITH MOTOR" (motor-operator box "M"),
     per sheet 004:
     – on its three load-side phase conductors: three donut CTs
       "CT7 400/5A"  "CT8 400/5A"  "CT9 400/5A"
     – a third identical digital meter "SVA" (SVA #3), current inputs I1 I1 / I2 I2 / I3 I3,
       voltage taps N · L1 · L2 · L3 taken directly from the busbar.
• Every feeder ends with a short downward load arrow.

—— E) CONTROL COMPARTMENT (bottom strip behind a divider line) —— [sheets 002 & 005]
• TWO identical switched-mode power supplies, each labeled exactly "POWER SUPPLY AC 230V".
  Each PSU is fed from the busbar through its own small protective breaker mounted directly
  above it — one breaker tagged "Q0", the other tagged "Q5". (These tag repetitions exist
  in the original drawing — reproduce them EXACTLY.)
• The two PSUs power a 2-wire 230 VAC control bus (L and N rails).
• ONE panel-mount digital temperature controller on those rails, dark faceplate:
    brand "SHIVA AMVAJ"   model "TRB-900"   "CODE: 15B2"
    title "TEMPERATURE CONTROLLER"
    display fields "PV" "SV" "REL" · supply terminals "PH" "N"
    specs "180-250 VAC" and "MAX 5A" · relay terminals "18" "15" "16"
• CONTROL LOGIC (must be visible): a dashed control wire leaves the TRB-900 relay terminals
  (18/15/16), passes through the divider, and reaches the motor-operator box "M" of breaker
  Q5 — the temperature controller automatically closes/trips feeder Q5.
• No other control devices exist. Nothing else in this compartment.

—— EXACT TEXT INVENTORY (render verbatim, case-sensitive) ——
Q0 · Q1 · Q2 · Q3 · Q5 · MCCB · 250A · 100A · 125A · 3 PHASE · 3PHASE · WITH MOTOR · M ·
CT1 CT2 CT3 CT4 CT5 CT6 CT7 CT8 CT9 · 400/5A · SVA · I1 I2 I3 · N L1 L2 L3 · Lighting ·
POWER SUPPLY · POWER SUPPLY AC 230V · SHIVA AMVAJ · TRB-900 · CODE: 15B2 ·
TEMPERATURE CONTROLLER · PV · SV · REL · PH · 180-250 VAC · MAX 5A · 18 15 16 · PE

—— ABSOLUTE RULES (violations = rejected image) ——
✗ No extra components: no contactors, no fuses, no signal lamps, no selector switches,
  no UPS, no generator, no fans, no extra meters or breakers.
✗ Counts are fixed: 9 feeders · 9 CTs (all 400/5A) · 3 SVA meters · 2 PSUs ·
  1 TRB-900 · 2 motorized breakers (Q0 250A, Q5 100A).
✗ Never draw the three 125A breakers as 3-pole — they are SINGLE-pole, one per phase.
✗ Never invent an amperage for the "Lighting" breaker — its only label is "Lighting".
✗ Power direction is fixed: cable enters at the BOTTOM → Q0 → CTs → busbar at the TOP →
  feeders drop downward.
✗ All device labels stay in ENGLISH exactly as listed. Legend/callouts may be in Farsi,
  matching the style of the attached reference image.

Output: landscape 16:9, high resolution, crisp readable text.
```

---

## 🟢 پرامپت فارسی (برای مدل‌های چندزبانه — همان محتوا)

```
تصویر پیوست‌شده مرجع سبک من است: دقیقاً همان تکنیک تصویرسازی، همان رنگ‌ها، همان سبک شماره‌گذاری و راهنما را کپی کن. اما محتوا باید ۱۰۰٪ از مشخصات مهندسی زیر بیاید — این بازطراحی گرافیکی یک نقشه‌ی تک‌خطی واقعی است. هیچ قطعه، سیم، تگ، عدد یا آمپراژی را اضافه، حذف، ادغام یا تغییر نده. همه‌ی برچسب‌ها را عیناً و حرف‌به‌حرف بنویس.

یک تابلوی توزیع برق صنعتی سه‌فاز (بدنه‌ی باز؛ قدرت در بالا، فرمان در پایین) با دقیقاً این ساختار:

الف) ورودی (چپ) [برگه 001]:
• کابل سه‌فاز + نول (+ ارت) از پایین تابلو وارد و بالا می‌رود.
• کلید اصلی: MCCB سه‌پل 250A با آپراتور موتوری (جعبه‌ی کوچک «M» متصل به کلید).
• برچسب‌ها: «Q0» و «MCCB 3 PHASE 250A WITH MOTOR»

ب) اندازه‌گیری ورودی [برگه 001، با جزئیات ترمینال]:
• روی سه هادی فاز بین Q0 و باسبار، دو گروه مستقل CT دوناتی — هر گروه ۳ عدد، مجموعاً ۶ CT، همگی 400/5A:
  گروه ۱: «CT1 400/5A» «CT2 400/5A» «CT3 400/5A» — گروه ۲: «CT4 400/5A» «CT5 400/5A» «CT6 400/5A»
• دو متر دیجیتال یکسان با نمایشگر سبز و برچسب «SVA»؛ هر متر دارای:
  ترمینال‌های جریان I1 I1 · I2 I2 · I3 I3 (حلقه‌ی ثانویه‌ی CT) و ترمینال‌های ولتاژ N · L1 · L2 · L3
  (سیم‌نازک تپ از باسبار)؛ متر اول علاوه بر آن ترمینال کمکی «POWER SUPPLY» دارد.
• متر اول به CT1–CT3 و متر دوم به CT4–CT6 متصل است؛ هر دو همین ورودی را می‌سنجند — تکرار عمدی است.

ج) باسبار (افقی، بالا): سه شینه‌ی مسی «L1» «L2» «L3» + نول «N» + ارت «PE» روی مقره.

د) فیدرهای خروجی — دقیقاً ۹ کلید آویزان از باسبار، از چپ به راست:
۱. «Lighting» — MCCB سه‌پل؛ برچسب فقط کلمه‌ی «Lighting» (بدون آمپراژ).
۲. «Q1» — سه‌پل 100A — مدار سه‌فاز + N + PE [برگه 003]
۳. «Q2» — سه‌پل 100A — سه‌فاز + N + PE [برگه 003]
۴. «Q3» — سه‌پل 100A — سه‌فاز + N + PE [برگه 003]
۵تا۷. سه کلید MCCB تک‌پل 125A [برگه 006] — حیاتی: هرکدام از یک فاز جداگانه: اولی از L1، دومی از L2، سومی از L3؛ هرکدام با N و PE خودش.
۸. «Q5» — سه‌پل 100A «3PHASE» «WITH MOTOR» با جعبه‌ی «M» [برگه 004]:
   روی سه هادی فازِ سمت بارِ کلید، سه CT دوناتی: «CT7 400/5A» «CT8 400/5A» «CT9 400/5A»
   + متر دیجیتال سوم «SVA» با ورودی‌های I1 I1 / I2 I2 / I3 I3 و تپ ولتاژ N·L1·L2·L3 از باسبار.
• زیر هر فیدر یک فلش کوتاه رو به پایین (بار).

هـ) محفظه‌ی فرمان (نوار پایین، پشت خط جداکننده) [برگه‌های 002 و 005]:
• دو منبع تغذیه‌ی یکسان با برچسب دقیق «POWER SUPPLY AC 230V»؛ هرکدام از باسبار از طریق
  کلید محافظ کوچکِ بالای خودش تغذیه می‌شود — یکی با تگ «Q0» و دیگری با تگ «Q5» (تکرار تگ‌ها
  در نقشه‌ی اصلی هست؛ عیناً بازسازی کن).
• دو PSU یک ریل فرمان دوسیمه 230VAC (L و N) را تغذیه می‌کنند.
• یک کنترلر دمای تابلویی روی همین ریل‌ها، پنل تیره:
  برند «SHIVA AMVAJ» مدل «TRB-900» «CODE: 15B2» عنوان «TEMPERATURE CONTROLLER»
  نمایشگر «PV» «SV» «REL» · ترمینال تغذیه «PH» «N» · مشخصات «180-250 VAC» و «MAX 5A» · ترمینال رله «18» «15» «16»
• منطق فرمان (باید دیده شود): یک سیم فرمان خط‌چین از ترمینال‌های رله‌ی TRB-900 (18/15/16)
  از خط جداکننده عبور کرده و به جعبه‌ی موتوری «M» کلید Q5 می‌رسد — کنترلر دما فیدر Q5 را
  خودکار وصل/قطع می‌کند. هیچ دستگاه فرمان دیگری وجود ندارد.

متن‌هایی که عیناً باید بیایند:
Q0 Q1 Q2 Q3 Q5 MCCB 250A 100A 125A 3 PHASE 3PHASE WITH MOTOR M CT1…CT9 400/5A SVA
I1 I2 I3 N L1 L2 L3 Lighting POWER SUPPLY POWER SUPPLY AC 230V SHIVA AMVAJ TRB-900
CODE: 15B2 TEMPERATURE CONTROLLER PV SV REL PH 180-250 VAC MAX 5A 18 15 16 PE

قوانین مطلق (نقض = تصویر رد):
✗ هیچ قطعه‌ی اضافه‌ای نه: کنتاکتور، فیوز، چراغ سیگنال، سوییچ انتخابگر، UPS، ژنراتور، فن، متر یا کلید اضافه.
✗ تعددها ثابت‌اند: ۹ فیدر · ۹ CT (همه 400/5A) · ۳ متر SVA · ۲ PSU · ۱ TRB-900 · ۲ کلید موتوری (Q0 250A و Q5 100A).
✗ سه کلید 125A هرگز سه‌پل کشیده نشوند — تک‌پل‌اند، هرکدام از یک فاز.
✗ برای کلید Lighting آمپراژ ساختگی نساز — تنها برچسبش «Lighting» است.
✗ جهت تغذیه ثابت است: کابل از پایین → Q0 → CTها → باسبار در بالا → فیدرها به پایین.
✗ برچسب تجهیزات انگلیسی بماند؛ فقط راهنما/شماره‌گذاری می‌تواند فارسی باشد (مطابق سبک عکس مرجع).

خروجی: کادر افقی ۱۶:۹، رزولوشن بالا، متن واضح و خوانا.
```

---

## ✅ چک‌لیست سریع پس از تولید
- [ ] ۹ فیدر؟ (Lighting، Q1، Q2، Q3، سه×125A، Q5)
- [ ] ۹ عدد CT با 400/5A؟ (CT1–CT6 روی ورودی، CT7–CT9 روی Q5)
- [ ] ۳ متر SVA؟ (دو روی ورودی، یکی روی Q5)
- [ ] سه کلید 125A تک‌پل و هرکدام از یک فاز؟
- [ ] Lighting بدون آمپراژ؟
- [ ] دو PSU با برچسب POWER SUPPLY AC 230V و تگ‌های Q0/Q5 روی کلید محافظشان؟
- [ ] TRB-900 با PV/SV/REL و ترمینال‌های 18-15-16؟
- [ ] سیم فرمان خط‌چین از TRB-900 تا M کیو۵؟
- [ ] کابل ورودی از پایین و باسبار در بالا؟
