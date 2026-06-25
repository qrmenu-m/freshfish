# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding='utf-8')
"""
Step 1: Better crops with precise coordinates.
Step 2: Remove background with rembg -> transparent PNG.
"""
from PIL import Image
import numpy as np
import os
from rembg import remove

BASE      = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\WhatsApp"
OUT_CROP  = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos\raw"
OUT_PNG   = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos\nobg"

os.makedirs(OUT_CROP, exist_ok=True)
os.makedirs(OUT_PNG,  exist_ok=True)

def auto_trim(img):
    """Strip black phone-frame border."""
    arr = np.array(img.convert("RGB"))
    bright_rows = np.where(arr.mean(axis=(1,2)) > 40)[0]
    bright_cols = np.where(arr.mean(axis=(0,2)) > 40)[0]
    if len(bright_rows)==0 or len(bright_cols)==0:
        return img
    return img.crop((int(bright_cols[0]), int(bright_rows[0]),
                     int(bright_cols[-1])+1, int(bright_rows[-1])+1))

def crop_and_remove(src_file, label, fl, ft, fr, fb):
    """Crop dish from menu image, then remove background."""
    path = os.path.join(BASE, src_file)
    img  = auto_trim(Image.open(path))
    W, H = img.size
    box  = (int(fl*W), int(ft*H), int(fr*W), int(fb*H))
    crop = img.crop(box).convert("RGBA")

    # Save raw crop for debug
    raw_path = os.path.join(OUT_CROP, f"{label}.jpg")
    crop.convert("RGB").save(raw_path, "JPEG", quality=88)

    # Remove background
    print(f"  Removing bg: {label}...", end=" ", flush=True)
    result = remove(crop)           # returns RGBA with transparent bg
    out_path = os.path.join(OUT_PNG, f"{label}.png")
    result.save(out_path, "PNG")
    print(f"done ({result.size})")
    return out_path

# ══════════════════════════════════════════════════════
# FILE 1 — Горячие блюда (499x931 after trim)
# Dish photos are on the LEFT side.
# Row height ~15%, starts at ~18%
# ══════════════════════════════════════════════════════
src1 = "WhatsApp Image 2026-06-23 at 14.54.23.jpeg"
print("\n[File1] Hot dishes")
crop_and_remove(src1, "sazan",  0.00, 0.185, 0.52, 0.310)
crop_and_remove(src1, "sudak",  0.00, 0.315, 0.52, 0.440)
crop_and_remove(src1, "som",    0.00, 0.445, 0.52, 0.570)
crop_and_remove(src1, "karas",  0.00, 0.575, 0.52, 0.700)
crop_and_remove(src1, "bersh",  0.00, 0.705, 0.52, 0.830)

# ══════════════════════════════════════════════════════
# FILE 2 — Снэки/крылышки (591x950 after trim)
# ══════════════════════════════════════════════════════
src2 = "WhatsApp Image 2026-06-23 at 14.54.23 (1).jpeg"
print("\n[File2] Snacks")
crop_and_remove(src2, "lukovye_kolca",  0.00, 0.115, 0.46, 0.240)
crop_and_remove(src2, "ovoshi_gril",    0.00, 0.245, 0.46, 0.380)
crop_and_remove(src2, "krevetki",       0.00, 0.385, 0.46, 0.520)
crop_and_remove(src2, "krilishki",      0.00, 0.525, 0.46, 0.660)
crop_and_remove(src2, "krilishki_teri", 0.00, 0.665, 0.46, 0.800)

# ══════════════════════════════════════════════════════
# FILE 3 — Салаты (591x950 after trim)
# ══════════════════════════════════════════════════════
src3 = "WhatsApp Image 2026-06-23 at 14.54.23 (2).jpeg"
print("\n[File3] Salads")
crop_and_remove(src3, "acuchuk",      0.00, 0.115, 0.46, 0.265)
crop_and_remove(src3, "svej_salat",   0.00, 0.270, 0.46, 0.430)
crop_and_remove(src3, "grecheskiy",   0.00, 0.435, 0.46, 0.600)
crop_and_remove(src3, "hrust_baklaj", 0.00, 0.605, 0.46, 0.760)

# ══════════════════════════════════════════════════════
# FILE 4 — Горячие блюда 2 (591x950 after trim)
# ══════════════════════════════════════════════════════
src4 = "WhatsApp Image 2026-06-23 at 14.54.23 (3).jpeg"
print("\n[File4] Hot dishes 2")
crop_and_remove(src4, "morskoy_okun",  0.00, 0.095, 0.50, 0.235)
crop_and_remove(src4, "forel_gril",    0.00, 0.240, 0.50, 0.375)
crop_and_remove(src4, "forel_dorad",   0.00, 0.380, 0.50, 0.515)
crop_and_remove(src4, "dorado",        0.00, 0.520, 0.50, 0.655)
crop_and_remove(src4, "semga_ris",     0.00, 0.635, 0.50, 0.775)
crop_and_remove(src4, "steyk_semga",   0.00, 0.780, 0.50, 0.915)

# ══════════════════════════════════════════════════════
# FILE 5 — Комбо (908x1600)
# Photos are wide landscape trays
# ══════════════════════════════════════════════════════
src5 = "WhatsApp Image 2026-06-23 at 14.54.23 (4).jpeg"
print("\n[File5] Combos")
crop_and_remove(src5, "combo_klassika", 0.00, 0.085, 0.75, 0.235)
crop_and_remove(src5, "combo_lyuks",    0.00, 0.400, 0.75, 0.545)
crop_and_remove(src5, "combo_shedevr",  0.00, 0.665, 0.75, 0.805)

# ══════════════════════════════════════════════════════
# FILE 6 — Сеты (591x1103 after trim)
# ══════════════════════════════════════════════════════
src6 = "WhatsApp Image 2026-06-23 at 14.54.24.jpeg"
print("\n[File6] Sets")
crop_and_remove(src6, "set_mini",       0.00, 0.075, 0.78, 0.225)
crop_and_remove(src6, "set_delikates",  0.00, 0.430, 0.78, 0.580)
crop_and_remove(src6, "set_daryi",      0.00, 0.762, 0.78, 0.908)

# ══════════════════════════════════════════════════════
# FILE 7 — Сеты 2 (591x950 after trim)
# ══════════════════════════════════════════════════════
src7 = "WhatsApp Image 2026-06-23 at 14.54.24 (1).jpeg"
print("\n[File7] Sets 2")
crop_and_remove(src7, "set_simfoniya",  0.00, 0.085, 0.78, 0.240)
crop_and_remove(src7, "set_freshfish",  0.00, 0.415, 0.78, 0.565)

# ══════════════════════════════════════════════════════
# FILE 8 — Гарниры (591x1102 after trim)
# ══════════════════════════════════════════════════════
src8 = "WhatsApp Image 2026-06-23 at 14.54.24 (2).jpeg"
print("\n[File8] Garniry")
crop_and_remove(src8, "fri",           0.00, 0.080, 0.46, 0.215)
crop_and_remove(src8, "derevenskiy",   0.00, 0.225, 0.46, 0.360)
crop_and_remove(src8, "shar_kartof",   0.00, 0.365, 0.46, 0.505)
crop_and_remove(src8, "naggetsyi",     0.00, 0.515, 0.46, 0.655)
crop_and_remove(src8, "syrn_palochki", 0.00, 0.665, 0.46, 0.800)

print("\nAll done! Check dish_photos/nobg/")
