#!/usr/bin/env python3
"""
make_sheets.py — Arkham LCG Card Print Sheet Generator
Epson ET-8550 + A4 Double-Sided Matte 250gsm

Usage:
  python make_sheets.py --pack "Nix the Puritan" --output ./print_output
  python make_sheets.py --all --output ./print_output
"""

import argparse
import os
import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# === CONFIG ===
REPO_ROOT = Path(r"C:\Users\edwar\Documents\games\board-game-vault")
INVESTIGATORS_DIR = REPO_ROOT / "games/arkham-lcg/investigators/custom-1"

# A4 at 300 DPI
DPI = 300
A4_W_MM = 210
A4_H_MM = 297

# Strange Eons exports with bleed baked in
# Full export: 1126x826px at 300dpi = 95.3x69.9mm (landscape)
# After auto-rotate to portrait: 69.9mm wide x 95.3mm tall
# Cut the bleed (~3.5mm each side) to get official 63x88mm card
# Print at FULL export size — cut line sits inside the bleed
CARD_W_MM = 70   # full export width after rotation (portrait)
CARD_H_MM = 96   # full export height after rotation (portrait)
GAP_MM = 1       # 1mm gap between cards
CELL_W_MM = CARD_W_MM + GAP_MM   # 71mm
CELL_H_MM = CARD_H_MM + GAP_MM   # 97mm

# Grid on A4 (210 x 297mm)
# 3 x 71mm = 213mm — slightly over, reduce gap to 0
# 3 x 70mm = 210mm = exact A4 width
# 3 x 96mm = 288mm, leaving 9mm (4.5mm each side top/bottom)
COLS = 3
ROWS = 3
CELL_W_MM = CARD_W_MM        # 70mm — no gap, bleed acts as gap
CELL_H_MM = CARD_H_MM        # 96mm
MARGIN_X_MM = (A4_W_MM - COLS * CELL_W_MM) / 2  # 0mm — edge to edge
MARGIN_Y_MM = (A4_H_MM - ROWS * CELL_H_MM) / 2  # 4.5mm

def mm_to_px(mm):
    return int(round(mm * DPI / 25.4))

A4_W = mm_to_px(A4_W_MM)
A4_H = mm_to_px(A4_H_MM)
CELL_W = mm_to_px(CELL_W_MM)
CELL_H = mm_to_px(CELL_H_MM)
MARGIN_X = mm_to_px(MARGIN_X_MM)
MARGIN_Y = mm_to_px(MARGIN_Y_MM)

def get_card_pairs(pack_dir: Path):
    """Find all Front/Back PNG pairs in a pack directory."""
    pairs = []
    folders = sorted([f for f in pack_dir.iterdir() if f.is_dir() and f.name != "art"])
    for folder in folders:
        fronts = sorted(folder.glob("*-Front.png"))
        backs = sorted(folder.glob("*-Back.png"))
        for front in fronts:
            back_name = front.name.replace("-Front.png", "-Back.png")
            back = folder / back_name
            if back.exists():
                pairs.append((front, back))
            else:
                pairs.append((front, None))
    return pairs

def make_blank(width, height, color=(255, 255, 255)):
    return Image.new("RGB", (width, height), color)

def place_card(sheet, card_img, col, row):
    """Place a card image at grid position (col, row) — auto-rotate if landscape, preserve aspect ratio."""
    x = MARGIN_X + col * CELL_W
    y = MARGIN_Y + row * CELL_H

    # Auto-rotate landscape cards to portrait
    img_w, img_h = card_img.size
    if img_w > img_h:
        card_img = card_img.rotate(90, expand=True)
        img_w, img_h = card_img.size

    # Resize preserving aspect ratio, fit within cell
    scale = min(CELL_W / img_w, CELL_H / img_h)
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    card_resized = card_img.resize((new_w, new_h), Image.LANCZOS)

    # Centre within cell
    offset_x = x + (CELL_W - new_w) // 2
    offset_y = y + (CELL_H - new_h) // 2
    sheet.paste(card_resized, (offset_x, offset_y))

def place_card_back(sheet, card_img, col, row):
    """Place a back card for duplex long-edge flip.
    ET-8550 rear feeder, art-side-up loading.
    Mirror columns AND rotate 180 to compensate for flip inversion.
    """
    mirrored_col = (COLS - 1) - col
    card_img = card_img.rotate(180)
    place_card(sheet, card_img, mirrored_col, row)

def draw_cut_lines(sheet):
    """Draw faint grey cut lines between cells."""
    draw = ImageDraw.Draw(sheet)
    color = (200, 200, 200)
    lw = 1
    for c in range(1, COLS):
        x = MARGIN_X + c * CELL_W
        draw.line([(x, 0), (x, A4_H)], fill=color, width=lw)
    for r in range(1, ROWS):
        y = MARGIN_Y + r * CELL_H
        draw.line([(0, y), (A4_W, y)], fill=color, width=lw)

def draw_instructions(sheet, sheet_num, total_sheets, side, pack_name):
    """Draw print instructions in the bottom margin."""
    draw = ImageDraw.Draw(sheet)

    # Try system fonts at large size — fall back to default
    font_large = None
    font_small = None
    for font_name in ["arialbd.ttf", "arial.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans.ttf"]:
        try:
            font_large = ImageFont.truetype(font_name, 52)
            font_small = ImageFont.truetype(font_name, 38)
            break
        except:
            continue
    if font_large is None:
        font_large = ImageFont.load_default()
        font_small = font_large

    color = (60, 60, 60)
    margin_left = mm_to_px(4)

    # Bottom margin area — cards end at MARGIN_Y + ROWS*CELL_H
    cards_bottom = MARGIN_Y + ROWS * CELL_H
    available = A4_H - cards_bottom  # space below cards

    # Place text centred in the bottom margin
    y1 = cards_bottom + int(available * 0.15)
    y2 = cards_bottom + int(available * 0.55)

    if side == "front":
        line1 = f"FRONT  |  {pack_name}  |  Sheet {sheet_num} of {total_sheets}"
        line2 = "Step 1: Print this sheet.  Step 2: Flip paper on LONG edge.  Step 3: Print BACK sheet."
    else:
        line1 = f"BACK   |  {pack_name}  |  Sheet {sheet_num} of {total_sheets}"
        line2 = "Flip on LONG edge (left side goes up). Reload face-down into rear tray."

    draw.text((margin_left, y1), line1, fill=color, font=font_large)
    draw.text((margin_left, y2), line2, fill=color, font=font_small)

    # Top-right corner label
    draw.text((A4_W - mm_to_px(28), mm_to_px(2)),
              f"S{sheet_num}/{total_sheets} {side.upper()}", fill=color, font=font_small)


def make_template_sheet(output_dir: Path, total_cards=9):
    """Generate a minimal ink test template -- white cards with number and outline only."""
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        font = ImageFont.truetype("arialbd.ttf", 120)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except:
            font = ImageFont.load_default()

    for side in ["front", "back"]:
        sheet = make_blank(A4_W, A4_H, (255, 255, 255))
        draw = ImageDraw.Draw(sheet)

        per_sheet = COLS * ROWS
        for idx in range(min(total_cards, per_sheet)):
            col = idx % COLS
            row = idx // COLS

            if side == "back":
                col = (COLS - 1) - col

            x = MARGIN_X + col * CELL_W
            y = MARGIN_Y + row * CELL_H

            # Draw card outline
            draw.rectangle([x+2, y+2, x+CELL_W-2, y+CELL_H-2], outline=(0,0,0), width=3)

            # Draw card number in centre
            num = str(idx + 1)
            bbox = draw.textbbox((0,0), num, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            tx = x + (CELL_W - tw) // 2
            ty = y + (CELL_H - th) // 2
            draw.text((tx, ty), num, fill=(0,0,0), font=font)

        # Cut lines
        draw_cut_lines(sheet)

        # Instructions
        draw_instructions(sheet, 1, 1, side, "TEMPLATE TEST")

        out = output_dir / f"TEMPLATE_{side}.png"
        sheet.save(out, dpi=(DPI, DPI))
        print(f"Template {side}: {out.name}")

    print(f"\nDone: template sheets saved to {output_dir}")


def make_sheets(pairs, output_dir: Path, prefix: str):
    """Generate front and back sheet PNGs from card pairs."""
    output_dir.mkdir(parents=True, exist_ok=True)
    per_sheet = COLS * ROWS
    sheet_num = 0

    for start in range(0, len(pairs), per_sheet):
        batch = pairs[start:start + per_sheet]
        sheet_num += 1

        front_sheet = make_blank(A4_W, A4_H)
        back_sheet = make_blank(A4_W, A4_H)

        for idx, (front_path, back_path) in enumerate(batch):
            col = idx % COLS
            row = idx // COLS

            # Front
            if front_path and front_path.exists():
                img = Image.open(front_path).convert("RGB")
                place_card(front_sheet, img, col, row)

            # Back
            if back_path and back_path.exists():
                img = Image.open(back_path).convert("RGB")
                place_card_back(back_sheet, img, col, row)
            elif front_path and front_path.exists():
                # Use generic back if no back exists
                img = make_blank(CELL_W, CELL_H, (30, 30, 80))
                place_card_back(back_sheet, img, col, row)

        total_sheets = (len(pairs) + per_sheet - 1) // per_sheet

        draw_cut_lines(front_sheet)
        draw_cut_lines(back_sheet)
        draw_instructions(front_sheet, sheet_num, total_sheets, "front", prefix)
        draw_instructions(back_sheet, sheet_num, total_sheets, "back", prefix)

        front_out = output_dir / f"{prefix}_sheet{sheet_num:02d}_front.png"
        back_out = output_dir / f"{prefix}_sheet{sheet_num:02d}_back.png"
        front_sheet.save(front_out, dpi=(DPI, DPI))
        back_sheet.save(back_out, dpi=(DPI, DPI))
        print(f"Sheet {sheet_num}: {front_out.name} + {back_out.name} ({len(batch)} cards)")

    print(f"\nDone: {sheet_num} sheet(s) generated in {output_dir}")
    print(f"Print front sheets first, then reload paper and print back sheets.")
    print(f"Duplex setting: Long-edge flip.")

def main():
    parser = argparse.ArgumentParser(description="Arkham LCG Print Sheet Generator")
    parser.add_argument("--pack", help="Pack folder name (e.g. 'Nix the Puritan')")
    parser.add_argument("--all", action="store_true", help="Process all investigator packs")
    parser.add_argument("--template", action="store_true", help="Generate minimal ink test template with card outlines and numbers only")
    parser.add_argument("--output", default="./print_output", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output)

    if args.template:
        print("Generating minimal ink template sheet...")
        make_template_sheet(output_dir / "template")

    elif args.test:
        # Find one 001 Front card from each pack — up to 9 different investigators
        packs = sorted([p for p in INVESTIGATORS_DIR.iterdir() 
                       if p.is_dir() and "Quick Look" not in p.name])
        pairs = []
        for pack in packs:
            # Only look in the 001 folder directly — not subfolders like mini
            folder_001 = sorted([f for f in pack.iterdir() if f.is_dir() and f.name.startswith("001")])
            if folder_001:
                front_path = sorted(folder_001[0].glob("*001*-Front.png"))
                if front_path:
                    front = front_path[0]
                    back = Path(str(front).replace("-Front.png", "-Back.png"))
                    pairs.append((front, back if back.exists() else None))
                    print(f"  + {pack.name}: {front.name}")
            if len(pairs) == 9:
                break
        print(f"\nTest sheet: {len(pairs)} investigators")
        make_sheets(pairs, output_dir, "SAMPLER_TEST")

    elif args.all:
        packs = [p for p in INVESTIGATORS_DIR.iterdir() if p.is_dir() and p.name != "Quick Look - Investigators"]
        for pack in sorted(packs):
            pairs = get_card_pairs(pack)
            if pairs:
                prefix = re.sub(r'[^\w]', '_', pack.name)
                print(f"\nProcessing: {pack.name} ({len(pairs)} cards)")
                make_sheets(pairs, output_dir / pack.name, prefix)
    elif args.pack:
        pack_dir = INVESTIGATORS_DIR / args.pack
        if not pack_dir.exists():
            print(f"Pack not found: {pack_dir}")
            return
        pairs = get_card_pairs(pack_dir)
        prefix = re.sub(r'[^\w]', '_', args.pack)
        print(f"\nProcessing: {args.pack} ({len(pairs)} cards)")
        make_sheets(pairs, output_dir, prefix)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
