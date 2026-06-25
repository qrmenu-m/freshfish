# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding='utf-8')
"""
Smart crop: auto-detect the white menu area (trim phone black borders),
then crop individual dish photos with corrected coordinates.
"""
from PIL import Image
import numpy as np
import os

BASE = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\WhatsApp"
OUT  = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos"
os.makedirs(OUT, exist_ok=True)

def auto_trim(img):
    """Remove black phone-frame borders by finding the bright content area."""
    arr = np.array(img.convert("RGB"))
    # Find rows/cols where mean brightness > 40
    bright_rows = np.where(arr.mean(axis=(1,2)) > 40)[0]
    bright_cols = np.where(arr.mean(axis=(0,2)) > 40)[0]
    if len(bright_rows) == 0 or len(bright_cols) == 0:
        return img
    r0, r1 = int(bright_rows[0]), int(bright_rows[-1])
    c0, c1 = int(bright_cols[0]), int(bright_cols[-1])
    return img.crop((c0, r0, c1+1, r1+1))

def crop_rel(src_file, label, fl, ft, fr, fb, quality=88):
    path = os.path.join(BASE, src_file)
    img  = Image.open(path)
    img  = auto_trim(img)   # <-- strip black phone border
    W, H = img.size
    box  = (int(fl*W), int(ft*H), int(fr*W), int(fb*H))
    crop = img.crop(box).convert("RGB")
    out  = os.path.join(OUT, f"{label}.jpg")
    crop.save(out, "JPEG", quality=quality)
    print(f"  OK {label}.jpg  trimmed={W}x{H}  crop={crop.size}")

# ════════════════════════════════════════════════════════
# FILE 1 — Горячие блюда
# After trim, the image is the white menu card.
# Layout: blue header ~0-17%, then 5 dish rows
# Each dish photo is on the LEFT (0..52%)
# ════════════════════════════════════════════════════════
src1 = "WhatsApp Image 2026-06-23 at 14.54.23.jpeg"
print("\n[File1] Hot dishes")
crop_rel(src1, "sazan",  0.00, 0.17, 0.52, 0.30)
crop_rel(src1, "sudak",  0.00, 0.30, 0.52, 0.43)
crop_rel(src1, "som",    0.00, 0.44, 0.52, 0.57)
crop_rel(src1, "karas",  0.00, 0.57, 0.52, 0.71)
crop_rel(src1, "bersh",  0.00, 0.71, 0.52, 0.84)

# ════════════════════════════════════════════════════════
# FILE 2 — Гарниры/снэки (луковые, овощи, креветки, крылышки x2)
# ════════════════════════════════════════════════════════
src2 = "WhatsApp Image 2026-06-23 at 14.54.23 (1).jpeg"
print("\n[File2] Snacks")
crop_rel(src2, "lukovye_kolca",  0.00, 0.10, 0.46, 0.24)
crop_rel(src2, "ovoshi_gril",    0.00, 0.24, 0.46, 0.38)
crop_rel(src2, "krevetki",       0.00, 0.38, 0.46, 0.53)
crop_rel(src2, "krilishki",      0.00, 0.53, 0.46, 0.67)
crop_rel(src2, "krilishki_teri", 0.00, 0.67, 0.46, 0.81)

# ════════════════════════════════════════════════════════
# FILE 3 — Салаты
# ════════════════════════════════════════════════════════
src3 = "WhatsApp Image 2026-06-23 at 14.54.23 (2).jpeg"
print("\n[File3] Salads")
crop_rel(src3, "acuchuk",      0.00, 0.10, 0.46, 0.26)
crop_rel(src3, "svej_salat",   0.00, 0.26, 0.46, 0.43)
crop_rel(src3, "grecheskiy",   0.00, 0.43, 0.46, 0.60)
crop_rel(src3, "hrust_baklaj", 0.00, 0.60, 0.46, 0.76)

# ════════════════════════════════════════════════════════
# FILE 4 — Горячие блюда 2 (морской окунь, форель, дорадо, сёмга)
# ════════════════════════════════════════════════════════
src4 = "WhatsApp Image 2026-06-23 at 14.54.23 (3).jpeg"
print("\n[File4] Hot2")
crop_rel(src4, "morskoy_okun",  0.00, 0.09, 0.50, 0.23)
crop_rel(src4, "forel_gril",    0.00, 0.23, 0.50, 0.37)
crop_rel(src4, "forel_dorad",   0.00, 0.37, 0.50, 0.51)
crop_rel(src4, "dorado",        0.00, 0.51, 0.50, 0.65)
crop_rel(src4, "semga_ris",     0.00, 0.63, 0.50, 0.77)
crop_rel(src4, "steyk_semga",   0.00, 0.77, 0.50, 0.91)

# ════════════════════════════════════════════════════════
# FILE 5 — Комбо (908x1600 with phone frame)
# After trim: just the menu card.
# Photo blocks: klassika ~6-22%, lyuks ~38-53%, shedevr ~65-80%
# ════════════════════════════════════════════════════════
src5 = "WhatsApp Image 2026-06-23 at 14.54.23 (4).jpeg"
print("\n[File5] Combos")
crop_rel(src5, "combo_klassika", 0.00, 0.06, 0.75, 0.22)
crop_rel(src5, "combo_lyuks",    0.00, 0.37, 0.75, 0.52)
crop_rel(src5, "combo_shedevr",  0.00, 0.64, 0.75, 0.79)

# ════════════════════════════════════════════════════════
# FILE 6 — Сеты (мини, деликатес, дары океана)
# ════════════════════════════════════════════════════════
src6 = "WhatsApp Image 2026-06-23 at 14.54.24.jpeg"
print("\n[File6] Sets")
crop_rel(src6, "set_mini",       0.00, 0.05, 0.78, 0.20)
crop_rel(src6, "set_delikates",  0.00, 0.29, 0.78, 0.45)
crop_rel(src6, "set_daryi",      0.00, 0.54, 0.78, 0.69)

# ════════════════════════════════════════════════════════
# FILE 7 — Сеты 2 (морская симфония, Fresh Fish сет)
# ════════════════════════════════════════════════════════
src7 = "WhatsApp Image 2026-06-23 at 14.54.24 (1).jpeg"
print("\n[File7] Sets 2")
crop_rel(src7, "set_simfoniya",  0.00, 0.05, 0.78, 0.21)
crop_rel(src7, "set_freshfish",  0.00, 0.39, 0.78, 0.55)

# ════════════════════════════════════════════════════════
# FILE 8 — Гарниры 2 (фри, деревенский, шарики, наггетсы, сырные)
# ════════════════════════════════════════════════════════
src8 = "WhatsApp Image 2026-06-23 at 14.54.24 (2).jpeg"
print("\n[File8] Garniry")
crop_rel(src8, "fri",           0.00, 0.08, 0.46, 0.22)
crop_rel(src8, "derevenskiy",   0.00, 0.22, 0.46, 0.37)
crop_rel(src8, "shar_kartof",   0.00, 0.37, 0.46, 0.52)
crop_rel(src8, "naggetsyi",     0.00, 0.52, 0.46, 0.67)
crop_rel(src8, "syrn_palochki", 0.00, 0.67, 0.46, 0.81)

print("\nAll done!")
