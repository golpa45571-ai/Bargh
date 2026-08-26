# 🔍 گزارش تطبیق تصویر تولیدشده با نقشه‌ی اصلی + پرامپت اصلاح (نسخه‌ی ۴)

**روش بررسی:** OCR کامل تصویر (۱۰۵ بلوک متنی با مختصات) + آنالیز پیکسلی (باسبار مسی، بدنه‌ها، نمایشگرها) — مقایسه با `MASTER_CIRCUIT_MEMORY.md`

---

## ✅ موارد صحیح (مطابق نقشه‌ی اصلی — دست نزنید)

| مورد | وضعیت در تصویر |
|---|---|
| کلید ورودی Q0 | «Q0 · MCCB · 3PHASE · 250A · WITH MOTOR» کامل و درست ✓ |
| CTهای ورودی | CT1، CT2، CT3 + CT4، CT5، CT6 (دو گروه ۳تایی) با نسبت ✓ |
| فیدرهای Q1، Q2، Q3 | هر سه: «Qx · 100A · MCCB» درست ✓ |
| فیدر روشنایی | فقط «Lighting» بدون آمپراژ — دقیقاً مثل نقشه ✓ |
| CTهای فیدر Q5 | CT7، CT8، CT9 با نسبت — جمع CTها = ۹ ✓ |
| دو منبع تغذیه | «POWER SUPPLY AC 230V» ×۲ با تگ‌های Q0 و Q5 روی کلید محافظ ✓ |
| کنترلر دما | SHIVA AMVAJ · TRB-900 · CODE:15B2 · TEMPERATURE CONTROLLER · PV · SV · PH · N · 180-250VAC ✓ |
| باسبار مسی | موجود (نوار مسی افقی بالای ردیف فیدرها) ✓ |
| سبک کلی | ۱۶:۹، تابلو باز، مرتب ✓ |

## ❌ مغایرت‌ها — ۸ خطای قطعی + ۳ مورد مشکوک

| # | خطا | در تصویر | صحیح (نقشه‌ی اصلی) | شدت |
|---|---|---|---|---|
| ۱ | **۴ متر SVA در ردیف بالا** (چهار جعبه: SVA ×۴) | SVA#1، #2، #3، #4 همه بالا | فقط **۳ متر**: دو تا کنار CTهای ورودی، سومی **پایین کنار CT7–CT9 فیدر Q5** | 🔴 زیاد |
| ۲ | **۴ کلید 125A** (چهار برچسب 125A MCCR پشت‌سرهم) | ×۴ | فقط **۳ عدد** تک‌پل: L1، L2، L3 | 🔴 زیاد |
| ۳ | متن خراب «WITKNOTOR» روی Q5 | garbled | «WITH MOTOR» | 🟠 متوسط |
| ۴ | «MAXSA» | garbled | «MAX 5A» | 🟠 متوسط |
| ۵ | «181516» چسبیده | بدون فاصله | «18 15 16» | 🟡 جزئی |
| ۶ | ترمینال مترها «111112121313» | بی‌معنا | «I1 I1 · I2 I2 · I3 I3» + «N L1 L2 L3» | 🟠 متوسط |
| ۷ | مقادیر ساختگی نمایشگرها «415.0V، 415.2V، 059، 80.0، 8hi h 87» | جعل محتوا | نقشه هیچ مقدار نمایشی ندارد — فقط SVA و 400/5A | 🟠 متوسط |
| ۸ | برچسب «REL» روی کنترلر پیدا نشد | جاافتاده | باید باشد (LED وضعیت رله) | 🟡 جزئی |
| ۹ | برچسب شینه‌ها روی باسبار نیست؛ «PE» هیچ‌جا یافت نشد | ناقص | ۵ شینه با برچسب «L1 L2 L3 N PE» | 🟠 متوسط |
| ۱۰ | «400/SA» (در ۹ مورد) | احتمالاً عکس/رندر | «400/5A» — دقت شود عدد 5 باشد | 🟡 جزئی |
| ۱۱ | جعبه‌ی M روی Q5 به‌وضوح دیده نشد (فقط یک M کنار Q0) | نامشخص | M باید روی Q0 **و** Q5 باشد + خط‌چین سبز از TRB-900 تا Mِ Q5 | 🟠 متوسط |

---

## 🔧 پرامپت اصلاحی — تصویر فعلی + این متن را به مدل بدهید

### English (recommended)

```
The attached panel image is ALMOST correct — keep its style, layout and every correctly
drawn part EXACTLY as is. Apply ONLY these targeted fixes:

FIX 1 — SVA METERS: currently FOUR meters are drawn in the top row. Delete the extra one:
there must be EXACTLY THREE SVA meters. Keep SVA #1 and SVA #2 in the top area next to
the incomer CT groups (CT1–CT3 and CT4–CT6), and MOVE the third SVA meter down, next to
the Q5 feeder's CTs (CT7/CT8/CT9). No fourth meter anywhere.

FIX 2 — 125A BREAKERS: currently FOUR breakers are labeled "125A". Delete one: there must
be EXACTLY THREE single-pole 125A MCCBs, fed from three different phases L1, L2, L3.

FIX 3 — On breaker Q5, correct the garbled text "WITKNOTOR" to exactly "WITH MOTOR".

FIX 4 — On the TRB-900 controller, correct "MAXSA" to exactly "MAX 5A", and space the
relay terminals as "18  15  16" (three separate terminals).

FIX 5 — On the SVA meter terminals, replace the garbled "111112121313" with the real
terminal marks: current inputs "I1 I1 · I2 I2 · I3 I3" and voltage inputs "N L1 L2 L3".

FIX 6 — Remove all invented display values ("415.0 V", "415.2 V", "059", "80.0", current
readings). Meter faces must show only the label "SVA" and "400/5A" — no numbers.

FIX 7 — Add the missing "REL" indicator label on the TRB-900 display row (next to PV, SV).

FIX 8 — Label the five busbar bars directly on them: "L1", "L2", "L3", "N", "PE".
The PE bar currently has no label — add it.

FIX 9 — Every CT label must read exactly "400/5A" (verify the digit 5, not letter S/A).

FIX 10 — Breaker Q0 AND breaker Q5 must each have a small motor-operator box marked "M"
mechanically attached, and ONE dashed green control wire must run from the TRB-900 relay
terminals (18/15/16) up to the "M" box of breaker Q5.

DO NOT change anything else: keep Q0 (MCCB 3PHASE 250A WITH MOTOR), Q1/Q2/Q3 (100A),
Lighting (no amperage), the two "POWER SUPPLY AC 230V" units with their "Q0"/"Q5" tagged
feed breakers, all TRB-900 texts, and the overall style exactly as they are.
Output landscape 16:9, high resolution, crisp text.
```

### فارسی (برای مدل‌های چندزبانه)

```
تصویر پیوست‌شده تقریباً درست است — سبک و چیدمان و همه‌ی بخش‌های درست را دقیقاً نگه دار. فقط این اصلاحات را اعمال کن:

۱. مترهای SVA: الان چهار متر در ردیف بالا رسم شده. اضافی را حذف کن — دقیقاً سه متر: SVA اول و دوم بالای تابلو کنار گروه‌های CT ورودی (CT1–CT3 و CT4–CT6)، و متر سوم را پایین ببر کنار CTهای فیدر Q5 (CT7/CT8/CT9). متر چهارم هیچ‌جا نباشد.

۲. کلیدهای 125A: الان چهار کلید 125A رسم شده. یکی را حذف کن — دقیقاً سه کلید تک‌پل 125A از سه فاز جداگانه L1 و L2 و L3.

۳. روی کلید Q5 متن خراب «WITKNOTOR» را به «WITH MOTOR» اصلاح کن.

۴. روی کنترلر TRB-900 عبارت «MAXSA» را به «MAX 5A» اصلاح کن و ترمینال‌های رله را با فاصله جدا: «18 15 16».

۵. روی ترمینال‌های مترهای SVA به‌جای متن بی‌معنای «111112121313»، نشانه‌های واقعی را بنویس: ورودی جریان «I1 I1 · I2 I2 · I3 I3» و ورودی ولتاژ «N L1 L2 L3».

۶. همه‌ی اعداد ساختگی نمایشگرها (415.0V، 415.2V، 059، 80.0، جریان‌ها) را حذف کن. صفحه‌ی متر فقط برچسب «SVA» و «400/5A» داشته باشد — بدون عدد.

۷. برچسب جاافتاده‌ی «REL» را روی نمایشگر TRB-900 کنار PV و SV اضافه کن.

۸. روی پنج شینه‌ی باسبار برچسب بگذار: «L1»، «L2»، «L3»، «N»، «PE». شینه‌ی PE الان بدون برچسب است.

۹. برچسب همه‌ی CTها دقیقاً «400/5A» باشد (عدد ۵، نه حرف).

۱۰. هر دو کلید Q0 و Q5 باید جعبه‌ی کوچک «M» (آپراتور موتوری) متصل به خودشان داشته باشند و یک سیم فرمان خط‌چین سبز از ترمینال‌های رله‌ی TRB-900 (18/15/16) تا جعبه‌ی M کلید Q5 کشیده شود.

هیچ چیز دیگری را تغییر نده: Q0 (MCCB 3PHASE 250A WITH MOTOR)، Q1/Q2/Q3 (100A)، Lighting (بدون آمپراژ)، دو منبع «POWER SUPPLY AC 230V» با تگ‌های Q0 و Q5 روی کلید محافظشان، همه‌ی متن‌های TRB-900 و سبک کلی دقیقاً همان بماند.
خروجی افقی ۱۶:۹، رزولوشن بالا، متن واضح.
```

---

## 📌 خلاصه‌ی وضعیت نهایی برای چک بعدی

| شاخص | هدف | وضعیت فعلی تصویر |
|---|---|---|
| فیدرها | ۸ کلید (Lighting + Q1-Q3 + 3×125A + Q5) | ۹ (یک 125A اضافه) ❌ |
| CT | ۹ × 400/5A | ۹ ✓ (متن 400/5A چک شود) |
| متر SVA | ۳ (۲ بالا + ۱ کنار Q5) | ۴، همگی بالا ❌ |
| PSU | ۲ با تگ Q0/Q5 | ۲ ✓ |
| TRB-900 | متن‌های کامل + REL | تقریباً ✓ (REL و MAX 5A و فاصله‌ی ترمینال‌ها) |
| M-box | روی Q0 و Q5 | Q0 ✓ / Q5 نامشخص ❓ |
| باسبار | L1 L2 L3 N PE | بدون برچسب / PE غایب ❌ |
