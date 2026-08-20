# Arkham LCG Card Printing Guide
## Epson ET-8550 + U-DM250-480 Double-Sided Matte 250gsm

---

## Paper Settings — Epson ET-8550

| Setting | Value |
|---|---|
| **Paper Type** | Ultra Premium Photo Paper Matte |
| **Paper Size** | A4 (210mm × 297mm) |
| **Print Quality** | Best Photo |
| **Colour** | Colour |
| **Duplex** | Long-edge binding (flip on long edge) |
| **Borderless** | Off |

---

## Card Dimensions

| | Metric | Imperial |
|---|---|---|
| **Card width** | 63mm | 2.48" |
| **Card height** | 88mm | 3.46" |
| **Bleed (each edge)** | 2mm | 0.08" |
| **Card with bleed** | 67mm × 92mm | 2.64" × 3.62" |

---

## Sheet Layout — 9 Cards per A4 Sheet (3×3)

```
A4 = 210mm × 297mm
Margins: Left/Right = 4.5mm, Top/Bottom = 4.5mm
Col 1: x=4.5mm  Col 2: x=71.5mm  Col 3: x=138.5mm
Row 1: y=4.5mm  Row 2: y=96.5mm  Row 3: y=188.5mm
```

---

## Printing Process

1. Run `make_sheets.py` to generate print PDFs
2. Open PDF → Print → Actual Size → A4 → Matte → Best → Long-edge duplex
3. Let dry 5 minutes after printing
4. Cut with guillotine: rows first, then columns
5. Optional: round corners with 3mm corner punch

---

## Quick Reference

| Cards per sheet | 9 |
|---|---|
| Sheets per full pack (35 cards) | 4 sheets (36 slots — 1 blank) |
| Strange Eons export DPI | 300 minimum |
| Colour space | sRGB |
