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

## Epson ET-8550 — Driver Settings (Windows 11)

### How to get to the driver

**Every time you print:**
1. Open your sheet PNG → Ctrl+P
2. Select Epson ET-8550
3. Click **Printer Properties** or **Preferences**
4. The Epson driver window opens with 3 tabs: **Main / More Options / Maintenance**

**To set as default (once):**
Windows Settings → Bluetooth & devices → Printers & scanners
→ Epson ET-8550 → Printing preferences → same tabs appear

---

### MAIN TAB — set these every print

**Paper Source**
- Select: **Rear Paper Feeder**
- The rear top tray handles photo and heavy stock like your 250gsm
- Do NOT leave on Auto — it defaults to the front cassette and the job will fail

**Document Size**
- Select: **A4**
- This is what Epson calls the paper size selector (confusingly named)

**Paper Type**
- Select: **Ultra Premium Photo Paper Matte**
- If not listed, use: **Premium Photo Paper Matte** or **Matte Paper — Heavyweight**
- This setting controls ink amount AND automatically switches to Matte Black Ink
- You do not need to set black ink separately — Paper Type handles it

**Color**
- Select: **Color**

**Quality**
- Select: **High**
- Best quality is available but is slower and uses more ink with minimal visible difference
- High is the recommended setting for card printing

**Borderless**
- Leave: **Off** (unchecked)

---

### MORE OPTIONS TAB

**Color Correction**
- Select: **Color Controls** (let Epson manage colour)
- Do NOT select ICM or No Color Adjustment unless you have installed a custom ICC profile
- Leave all sliders at default

---

### MAINTENANCE TAB → Extended Settings

**Thick Paper and Envelopes**
- Check this box: **ON**
- Your U-DM250-480 at 250gsm is thick — this slows the feed slightly to prevent smearing
- Must be set once — it stays checked until you uncheck it

---

### When printing the PNG sheets

1. Open `SAMPLER_TEST_sheet01_front.png` in **Windows Photos**
2. Ctrl+P → select Epson ET-8550
3. Click **More Settings**
4. Set paper size: **A4**
5. Set fit: **Actual Size** — NEVER Fit to Page (resizes cards)
6. Click **Printer Properties** → verify Main tab settings above
7. Print front sheet
8. Reload paper flipped on long edge
9. Print back sheet

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
