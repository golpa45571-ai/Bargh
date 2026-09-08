# Bargh

## نقشهٔ جامع برق — Master Power & Control Drawing

خروجی اصلی این مخزن، یک نقشهٔ یکپارچه و خوانا از کل مدار برق است که بر اساس
`totall.pdf` (نقشهٔ master) و شیت‌های `001.pdf` تا `006.pdf` دوباره ترسیم شده؛
تمام تگ‌ها، ریتینگ‌ها، شماره‌سیم‌ها (۱ تا ۱ و ۱۸)، ترمینال‌ها و سایز هادی‌ها
مطابق فایل‌های اصلی حفظ شده‌اند.

| فایل | توضیح |
|---|---|
| `bargh_master_diagram.png` | نقشهٔ نهایی، ۷۰۲×۳۱۲۲ پیکسل (۲۴۰ DPI، مناسب چاپ ~A2 افقی) |
| `bargh_master_diagram.svg` | همان نقشه به‌صورت برداری، بدون افت کیفیت در بزرگ‌نمایی/چاپ |
| `make_master_drawing.py` | اسکریپت matplotlib که نقشه را تولید می‌کند (قابل ویرایش و بازتولید) |
| `totall.pdf` | نقشهٔ master اصلی (مرجع) |
| `001.pdf` … `006.pdf` | شیت‌های جزئیات (مرجع) |
| `power_circuit.md` | پیاده‌سازی متن کامل و راستی‌آزمایی‌شدهٔ تمام شیت‌ها |

## بازتولید نقشه

```bash
pip install matplotlib
python3 make_master_drawing.py
```

## نحوهٔ دانلود

- هر فایل را در همین صفحه باز کنید و با دکمهٔ **Download raw file** (آیکون ⬇) بگیرید.
- برای دانلود یک‌جای کل پروژه: دکمهٔ **Code → Download ZIP** در بالای همین صفحه.
- لینک مستقیم ZIP این برنچ:
  https://github.com/golpa45571-ai/Bargh/archive/refs/heads/arena/01a06e4b-bargh.zip

---

## Master Power & Control Drawing (EN)

A single readable composite of the entire power/control circuit, re-typeset from
`totall.pdf` + sheets `001–006.pdf`. All device tags, ratings, wire numbers,
terminal markings and conductor sizes are exactly as printed on the source PDFs;
junction dots appear only where the source draws a connection.
