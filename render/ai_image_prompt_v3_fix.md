# 🔧 پرامپت اصلاح تصویر تولیدشده — نسخه‌ی ۳
> **روش استفاده:** تصویری که هوش مصنوعی ساخته + این پرامپت را با هم به همان مدل بدهید (مدل‌های Gemini / Nano Banana / GPT-4o قابلیت ویرایش تصویر ورودی را دارند).

---

## 🎯 PROMPT (English) — attach your generated image + this text

```
I am attaching a generated image of an electrical panel. The overall style is good —
KEEP the same style, composition, colors and layout. But the CONTENT has deviations from
the real engineering drawing. Apply ONLY the corrections below; change nothing else.

CORRECTION LIST — verify and fix each item in the attached image:

1. BREAKER COUNT (bottom feeder row): there must be EXACTLY 8 feeder breakers under the
   busbar, left to right: "Lighting", "Q1 100A", "Q2 100A", "Q3 100A", then THREE separate
   "125A" breakers, then "Q5 100A". Plus ONE large incomer breaker "Q0 250A" on the left
   between the incoming cable and the busbar. Nothing more, nothing less.
   → If any breaker is missing or extra, add/remove it.

2. The three "125A" breakers are SINGLE-POLE (narrow, one pole each), NOT 3-pole wide.
   Each connects to a different phase: first = L1, second = L2, third = L3.

3. The "Lighting" breaker has ONLY the label "Lighting" — no amperage number on it.
   → Remove any "100A" or other rating printed on the Lighting breaker.

4. CURRENT TRANSFORMERS: exactly 9 donut CTs total:
   – 6 CTs on the three incoming phase conductors between Q0 and the busbar
     (labels: CT1 400/5A, CT2 400/5A, CT3 400/5A, CT4 400/5A, CT5 400/5A, CT6 400/5A)
   – 3 CTs on the three load-side conductors of breaker Q5
     (labels: CT7 400/5A, CT8 400/5A, CT9 400/5A)
   → Every CT must show "400/5A". Remove any extra CTs elsewhere.

5. METERS: exactly 3 identical digital meters labeled "SVA":
   – SVA #1 and SVA #2 both next to the incomer CT groups (both wired to the incoming
     feeder — the duplication is intentional)
   – SVA #3 next to the Q5 feeder CTs
   → Remove any 4th meter; do not delete the duplicated incomer meter.

6. MOTOR OPERATORS: exactly two breaker actuators — a small box "M" attached to the Q0
   breaker and another "M" attached to the Q5 breaker. Other breakers have none.

7. CONTROL COMPARTMENT (bottom): exactly two power supplies labeled
   "POWER SUPPLY AC 230V" and one temperature controller with texts:
   "SHIVA AMVAJ" · "TRB-900" · "CODE: 15B2" · "TEMPERATURE CONTROLLER" ·
   "180-250 VAC" · "MAX 5A" · display fields "PV" "SV" "REL" · relay terminals "18 15 16".
   → Fix any misspelled text exactly as written here.

8. CONTROL WIRE: one dashed line from the TRB-900 controller to the "M" box of breaker Q5.

9. POWER DIRECTION: incoming cable enters from the BOTTOM of the panel, goes up through
   Q0, then the 6 CTs, into the busbar at the TOP; feeders drop downward with arrows.

10. BUSBAR: three copper phase bars "L1" "L2" "L3" + neutral "N" + earth "PE".

11. REMOVE any component that is not in this list: contactors, fuses, signal lamps,
    selector switches, UPS, generator, fans, extra meters, extra breakers.

12. All labels must be spelled EXACTLY (case-sensitive):
    Q0 Q1 Q2 Q3 Q5 · MCCB · 250A 100A 125A · 3PHASE · WITH MOTOR · CT1…CT9 · 400/5A ·
    SVA · Lighting · POWER SUPPLY AC 230V · SHIVA AMVAJ · TRB-900 · CODE: 15B2 ·
    TEMPERATURE CONTROLLER · 180-250 VAC · MAX 5A · PV SV REL · PH N · L1 L2 L3 PE · 18 15 16

Keep everything else in the attached image unchanged. Output landscape 16:9, high
resolution, crisp text.
```

---

## 🟢 نسخه‌ی فارسی (برای مدل‌های چندزبانه)

```
تصویر پیوست‌شده یک تابلوی برق است که قبلاً تولید شده. سبک، ترکیب‌بندی و رنگ‌ها خوب‌اند — همان‌ها را نگه دار. فقط محتوا باید طبق نقشه‌ی مهندسی واقعی اصلاح شود. فقط موارد زیر را درست کن و هیچ چیز دیگری را تغییر نده:

۱. تعداد کلیدهای فیدر در ردیف زیر باسبار دقیقاً ۸ عدد باشد، از چپ به راست: «Lighting»، «Q1 100A»، «Q2 100A»، «Q3 100A»، سه کلید «125A» جداگانه، و در آخر «Q5 100A». به‌علاوه یک کلید بزرگ ورودی «Q0 250A» در سمت چپ بین کابل ورودی و باسبار. نه کمتر نه بیشتر — کم و اضافه را اصلاح کن.

۲. سه کلید 125A تک‌پل و باریک‌اند، نه سه‌پل پهن. هرکدام به یک فاز جداگانه: اولی L1، دومی L2، سومی L3.

۳. روی کلید Lighting فقط کلمه‌ی «Lighting» نوشته شود — هیچ آمپراژی روی آن نباشد (اگر 100A یا عدد دیگری چاپ شده، حذفش کن).

۴. ترانس‌های جریان: دقیقاً ۹ عدد CT دوناتی — ۶ عدد روی سه هادی ورودی بین Q0 و باسبار (برچسب‌ها: CT1 400/5A تا CT6 400/5A) و ۳ عدد روی سه هادی سمت بار کلید Q5 (CT7 400/5A تا CT9 400/5A). همه باید 400/5A داشته باشند. CT اضافه‌ی هرجای تصویر را حذف کن.

۵. مترها: دقیقاً ۳ متر دیجیتال یکسان با برچسب «SVA» — دو عدد کنار گروه‌های CT ورودی (تکرار عمدی است، حذف نکن) و یک عدد کنار CTهای فیدر Q5. متر چهارم نباشد.

۶. آپراتور موتوری (جعبه‌ی کوچک M): فقط دو عدد — یکی متصل به کلید Q0 و یکی متصل به کلید Q5. بقیه‌ی کلیدها M نداشته باشند.

۷. محفظه‌ی فرمان (پایین): دقیقاً دو منبع تغذیه با برچسب «POWER SUPPLY AC 230V» و یک کنترلر دما با متن‌های: «SHIVA AMVAJ» · «TRB-900» · «CODE: 15B2» · «TEMPERATURE CONTROLLER» · «180-250 VAC» · «MAX 5A» · فیلدهای «PV» «SV» «REL» · ترمینال‌های «18 15 16». هر غلط املایی را عیناً با همین املای‌ها اصلاح کن.

۸. سیم فرمان: یک خط خط‌چین از کنترلر TRB-900 تا جعبه‌ی M کلید Q5.

۹. جهت تغذیه: کابل ورودی از پایین تابلو وارد می‌شود، بالا می‌رود از Q0 و ۶ CT عبور می‌کند و به باسبارِ بالایی می‌رسد؛ فیدرها با فلش رو به پایین خارج می‌شوند.

۱۰. باسبار: سه شینه‌ی مسی «L1» «L2» «L3» + نول «N» + ارت «PE».

۱۱. هر قطعه‌ای که در این فهرست نیست حذف شود: کنتاکتور، فیوز، چراغ سیگنال، سوییچ انتخابگر، UPS، ژنراتور، فن، متر اضافه، کلید اضافه.

۱۲. همه‌ی برچسب‌ها دقیقاً با همین املاء (به بزرگی و کوچکی حروف): Q0 Q1 Q2 Q3 Q5 · MCCB · 250A 100A 125A · 3PHASE · WITH MOTOR · CT1…CT9 · 400/5A · SVA · Lighting · POWER SUPPLY AC 230V · SHIVA AMVAJ · TRB-900 · CODE: 15B2 · TEMPERATURE CONTROLLER · 180-250 VAC · MAX 5A · PV SV REL · PH N · L1 L2 L3 PE · 18 15 16

بقیه‌ی تصویر دست‌نخورده بماند. خروجی افقی ۱۶:۹، رزولوشن بالا، متن واضح.
```

---

## 👁 چک‌لیست بصری ۳۰ ثانیه‌ای (خودتان سریع نگاه بیندازید)

| نگاه به… | باید ببینید | خطای رایج مدل‌ها |
|---|---|---|
| ردیف کلیدهای فیدر | ۸ کلید: Lighting + ۳تا 100A + ۳تا 125A + Q5 | کم/زیاد کردن تعداد |
| سه کلید 125A | باریک و تک‌پل | کشیدن سه‌پل پهن |
| کلید Lighting | فقط «Lighting» | چسباندن آمپراژ ساختگی |
| حلقه‌های CT روی ورودی | ۶ حلقه با 400/5A | جا انداختن یا اضافه‌کردن |
| مترهای SVA | ۳ عدد (۲ روی ورودی + ۱ روی Q5) | حذف متر تکراری ورودی! |
| جعبه‌های M | فقط روی Q0 و Q5 | M روی همه‌ی کلیدها |
| پایین تابلو | ۲ منبع تغذیه + ۱ کنترلر TRB-900 | اضافه‌کردن کنتاکتور/چراغ |
| متن‌ها | TRB-900، SHIVA AMVAJ، CODE: 15B2، 400/5A | غلط املایی شدید |
| مسیر خط‌چین | از TRB-900 تا Mکیو۵ | جا افتادن |
| ورودی کابل | از پایین تابلو | معکوس کردن |

**نکته:** هر سطر چک‌لیست که خراب بود، همان شماره در پرامپت اصلاحی معادلش است — می‌توانید پرامپت را کامل بدهید یا فقط شماره‌های معیوب را.
