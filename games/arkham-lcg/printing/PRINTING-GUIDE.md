# Arkham LCG Card Printing Guide
## Epson ET-8550 + U-DM250-480 Double-Sided Matte 250gsm

---

## ICC Colour Profile — Do You Need One?

No dedicated ICC profile exists for U-DM250-480 + ET-8550. This is normal
for lesser-known paper brands. The good news: the ET-8550's pigment ink on
matte paper handles saturated game card art very well without one.

**Recommended approach — start simple:**
1. Use driver setting: **Ultra Premium Photo Paper Matte**
2. Let **Epson manage colour** (turn off colour management in the app)
3. Print one test sheet and assess
4. If colours look off, try one of the free profiles below

**Free ICC profiles if needed:**

| Source | Profile | Driver Setting |
|---|---|---|
| Qimage Ultimate | Non-Epson matte profiles for ET-8550 | ddisoftware.com/qimage-u/dl-8550.htm |
| Red River Paper | Premium Matte — closest match | redrivercatalog.com |
| Jimmy Nordström | Scandinavian Photo Matte Pro | Velvet Fine Art Paper / Standard |

**How to install a profile on Windows:**
1. Download the `.icm` file
2. Right-click it → Install Profile
3. In your print app: select **Application Manages Colour** → choose the profile
4. In Epson driver: set colour management to **Off (No Color Adjustment)**

---

## Paper Settings — Epson ET-8550 (Windows 11)

| Setting | Tab | Value |
|---|---|---|
| **Media Type** | Main | Ultra Premium Photo Paper Matte |
| **Print Quality** | Main | Best |
| **Color** | Main | Color |
| **Black Ink** | Main | Matte Black Ink |
| **Paper Source** | Main | Rear Paper Feed |
| **Paper Size** | Main | A4 |
| **Duplex** | Page Layout | Long-edge binding |
| **Borderless** | Main | Off |
| **Thick Paper** | Maintenance → Extended Settings | Check this box for 250gsm |

**Where to find these settings on Windows 11:**
1. Open any image → File → Print
2. Select **Epson ET-8550** as printer
3. Click **Printer Properties** or **Preferences**
4. You will see the **Main tab** — set Media Type, Quality, Black Ink here
5. Click **Page Layout tab** for duplex settings

**Important — Matte Black Ink:**
For matte paper the driver must switch to Matte Black Ink.
Selecting "Ultra Premium Photo Paper Matte" as Media Type does this automatically.
If you see "Photo Black Ink" selected — change Media Type first, it will switch.

**Important — Thick Paper setting:**
250gsm is thick. In the driver go to:
Maintenance tab → Extended Settings → check **Thick Paper and Envelopes**
This slows the feed slightly and prevents smearing on heavy stock.

**Always print at Actual Size:**
In the print dialog set fit to **Actual Size** — never "Fit to Page".
Fit to Page resizes the cards and throws off the cut lines.

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
