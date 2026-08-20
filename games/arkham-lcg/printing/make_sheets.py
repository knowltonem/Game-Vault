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
from PIL import Image, ImageDraw

# === CONFIG ===
REPO_ROOT = Path(r"C:\Users\edwar\Documents\games\board-game-vault")
INVESTIGATORS_DIR = REPO_ROOT / "games/arkham-lcg/investigators/custom-1"

# A4 at 300 DPI
DPI = 300
A4_W_MM = 210
A4_H_MM = 297

# Actual Strange Eons export dimensions (bleed already included in PNG)
# Measured from exports: 1126x826px at 300dpi = 95.3x69.9mm (landscape)
# After auto-rotate to portrait: 69.9mm wide x 95.3mm tall
CARD_W_MM = 70   # after rotation (was height)
CARD_H_MM = 95   # after rotation (was width)
BLEED_MM = 0     # bleed already baked into PNG by Strange Eons
CELL_W_MM = CARD_W_MM  # 70mm
CELL_H_MM = CARD_H_MM  # 95mm

# Grid: 3x3 per sheet (9 cards) — fits perfectly on A4 with margins
# 3 x 70mm = 210mm = exact A4 width (no side margins needed)
# 3 x 95mm = 285mm, leaving 12mm top/bottom margin
COLS = 3
ROWS = 3
MARGIN_X_MM = (A4_W_MM - COLS * CELL_W_MM) / 2  # ~0mm
MARGIN_Y_MM = (A4_H_MM - ROWS * CELL_H_MM) / 2  # ~6mm

def mm_to_px(mm):
    return int(round(mm * DPI / 25.4))

A4_W = mm_to_px(A4_W_MM)
A4_H = mm_to_px(A4_H_MM)
CELL_W = mm_to_px(CELL_W_MM)
CELL_H = mm_to_px(CELL_H_MM)
MARGIN_X = mm_to_px(MARGIN_X_MM)
MARGIN_Y = mm_to_px(MARGIN_Y_MM)
BLEED = mm_to_px(BLEED_MM)

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
    """Place a back card — mirrored horizontally for duplex long-edge."""
    mirrored_col = (COLS - 1) - col
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

        draw_cut_lines(front_sheet)
        draw_cut_lines(back_sheet)

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
    parser.add_argument("--test", action="store_true", help="Generate a sampler sheet with 9 different investigator 001 cards")
    parser.add_argument("--output", default="./print_output", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output)

    if args.test:
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
