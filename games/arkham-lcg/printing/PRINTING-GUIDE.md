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

## Printing from Epson Photo+ (Windows 11) — Step by Step

### Every print job — front sheet first:

1. Open **Epson Photo+**
2. Confirm **ET-8550 Series (Network)** selected at top
3. Click **Photo**
4. **Paper Settings** dialog:
   - Select **A4** → OK
5. Add your sheet PNG file
6. In print settings:
   - **Fit:** Shrink to Fit ← CRITICAL — NOT Fill Page
   - **Orientation:** Portrait
   - **Copies:** 1
7. Click **Print Settings** or **Printer Properties** (Epson driver):
   - **Main tab → Media Type:** Ultra Premium Photo Paper Matte
   - **Main tab → Quality:** High
   - **Main tab → Color:** Color
   - **Main tab → Paper Source:** Rear Paper Feeder
   - **Maintenance → Extended Settings → Thick Paper and Envelopes:** ON
8. Print the FRONT sheet
9. Let sit 2 minutes before handling

### Flipping for the back sheet:

1. Take the printed front sheet
2. Flip it on the **LONG edge** (left side comes up and over to the right)
3. Reload into the rear paper feeder — **art side facing UP** (blank side down)
4. ET-8550 rear feeder prints on the bottom surface — blank side gets printed
5. Open the BACK sheet PNG in Epson Photo+
6. Same settings as above
7. Print the BACK sheet

### DO NOT use:
- **Fill Page** — stretches and crops cards
- **Fit to Page** (if different from Shrink to Fit) — may resize
- **Landscape** orientation
- Any rotation option in Epson Photo+

---

## Print Sheet Specification — Locked Settings

These are the confirmed settings used by `make_sheets.py`.
Do not change unless Strange Eons export format changes.

| Setting | Value | Reason |
|---|---|---|
| **Card cell size** | 70mm × 95mm | Actual Strange Eons export size after rotation |
| **Bleed** | 0mm added | Bleed already baked into PNG by Strange Eons |
| **Card orientation** | Auto-rotate landscape → portrait | Strange Eons exports landscape (1126×826px) |
| **Grid** | 3×3 = 9 cards per A4 sheet | 3×70mm = 210mm = exact A4 width |
| **Back sheet — columns** | Mirrored left-right | Long-edge flip swaps left/right |
| **Back sheet — rows** | Same as front | Long-edge flip does not invert rows |
| **Back card rotation** | 180° | Corrects orientation after long-edge flip |
| **DPI** | 300 | Strange Eons exports at 300 DPI |
| **Sheet format** | PNG at 300 DPI | Direct print from Epson Photo+ |

---

## Script Commands

```
# Sampler test sheet — 9 different investigator 001 cards
python make_sheets.py --test --output ./print_output/test

# Full pack
python make_sheets.py --pack "Nix the Puritan" --output ./print_output

# All packs
python make_sheets.py --all --output ./print_output
```

---

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
