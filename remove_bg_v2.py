# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding='utf-8')
"""
V2: Precise crops from NEW upscaled PNG images + rembg background removal.
"""
from PIL import Image
import os
from rembg import remove

BASE     = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\WhatsApp"
OUT_RAW  = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos\raw_v2"
OUT_NOBG = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos\nobg_v2"

os.makedirs(OUT_RAW,  exist_ok=True)
os.makedirs(OUT_NOBG, exist_ok=True)

def crop_and_remove(img, label, left, top, right, bottom):
    """Crop region (absolute pixels), then remove background."""
    crop = img.crop((left, top, right, bottom)).convert("RGBA")
    
    # Save raw crop for debugging
    crop.convert("RGB").save(os.path.join(OUT_RAW, f"{label}.jpg"), "JPEG", quality=92)
    
    # Remove background with rembg
    print(f"  {label}... ", end="", flush=True)
    result = remove(crop)
    result.save(os.path.join(OUT_NOBG, f"{label}.png"), "PNG")
    print(f"done {result.size}")


# ═══════════════════════════════════════════════════════
# Image (4).png — Горячие блюда 1 (998 x 2160)
# Сазан, Судак, Белый амур, Сом, Карась, Берш
# ═══════════════════════════════════════════════════════
print("\n[1] Image (4).png — Горячие блюда 1")
img = Image.open(os.path.join(BASE, "Image (4).png"))
# W=998, H=2160

crop_and_remove(img, "sazan",      20,  380, 430,  630)   # Сазан — доска с рыбой
crop_and_remove(img, "sudak",      20,  640, 400,  870)   # Судак
crop_and_remove(img, "beliy_amur", 20,  880, 400, 1080)   # Белый амур
crop_and_remove(img, "som",        15, 1080, 420, 1340)   # Сом
crop_and_remove(img, "karas",      15, 1340, 420, 1620)   # Карась
crop_and_remove(img, "bersh",      15, 1620, 420, 1940)   # Берш


# ═══════════════════════════════════════════════════════
# Image (1).png — Горячие блюда 2 (1182 x 2560)
# Морской окунь, Форель гриль, Жареная форель, Дорадо, Сёмга, Стейк сёмги
# ═══════════════════════════════════════════════════════
print("\n[2] Image (1).png — Горячие блюда 2")
img = Image.open(os.path.join(BASE, "Image (1).png"))
# W=1182, H=2560

crop_and_remove(img, "morskoy_okun", 20,  420, 480,  680)   # Морской окунь
crop_and_remove(img, "forel_gril",   20,  700, 500,  970)   # Форель на гриле
crop_and_remove(img, "forel_dorad",  20,  990, 500, 1260)   # Жареная форель+дольки
crop_and_remove(img, "dorado",       20, 1280, 460, 1520)   # Дорадо
crop_and_remove(img, "semga_ris",    20, 1660, 480, 1960)   # Сёмга с рисом
crop_and_remove(img, "steyk_semga",  20, 1980, 480, 2320)   # Стейк из сёмги


# ═══════════════════════════════════════════════════════
# WhatsApp Image ... (1).jpeg — Снэки/крылышки (2364 x 5120)
# Луковые кольца, Овощи гриль, Креветки, Крылышки, Крылышки терияки
# (this old file is still the snacks page, doubled resolution)
# ═══════════════════════════════════════════════════════
print("\n[3] WhatsApp — Снэки/крылышки")
img = Image.open(os.path.join(BASE, "WhatsApp Image 2026-06-23 at 14.54.23 (1).jpeg"))
# W=2364, H=5120 (this is already high-res from WhatsApp)

crop_and_remove(img, "lukovye_kolca",   30,  640, 1050, 1250)
crop_and_remove(img, "ovoshi_gril",     30, 1280, 1050, 1920)
crop_and_remove(img, "krevetki",        30, 1960, 1050, 2620)
crop_and_remove(img, "krilishki",       30, 2660, 1050, 3340)
crop_and_remove(img, "krilishki_teri",  30, 3370, 1050, 4060)


# ═══════════════════════════════════════════════════════
# Image.png — Салаты (1182 x 2560)
# Ачучук, Свежий салат, Греческий, Хрустящие баклажаны
# ═══════════════════════════════════════════════════════
print("\n[4] Image.png — Салаты")
img = Image.open(os.path.join(BASE, "Image.png"))
# W=1182, H=2560

crop_and_remove(img, "acuchuk",       30,  470, 460,  780)
crop_and_remove(img, "svej_salat",    30,  800, 460, 1160)
crop_and_remove(img, "grecheskiy",    30, 1160, 460, 1520)
crop_and_remove(img, "hrust_baklaj",  30, 1530, 460, 1880)


# ═══════════════════════════════════════════════════════
# Image (3).png — Комбо (1816 x 3200)
# Классика, Люкс, Шедевр
# ═══════════════════════════════════════════════════════
print("\n[5] Image (3).png — Комбо")
img = Image.open(os.path.join(BASE, "Image (3).png"))
# W=1816, H=3200

crop_and_remove(img, "combo_klassika", 20,  200, 1100,  550)
crop_and_remove(img, "combo_lyuks",    20, 1040, 1000, 1440)
crop_and_remove(img, "combo_shedevr",  20, 1820, 1050, 2240)


# ═══════════════════════════════════════════════════════
# Image (6).png — Сеты 1 (1182 x 2560)
# Мини, Деликатес, Дары Океана
# ═══════════════════════════════════════════════════════
print("\n[6] Image (6).png — Сеты 1")
img = Image.open(os.path.join(BASE, "Image (6).png"))
# W=1182, H=2560

crop_and_remove(img, "set_mini",       20,  290, 580,  560)
crop_and_remove(img, "set_delikates",  20,  980, 580, 1280)
crop_and_remove(img, "set_daryi",      20, 1620, 580, 1930)


# ═══════════════════════════════════════════════════════
# Image (2).png — Сеты 2 (1182 x 2560)
# Морская симфония, Fresh Fish
# ═══════════════════════════════════════════════════════
print("\n[7] Image (2).png — Сеты 2")
img = Image.open(os.path.join(BASE, "Image (2).png"))
# W=1182, H=2560

crop_and_remove(img, "set_simfoniya",  20,  340, 600,  650)
crop_and_remove(img, "set_freshfish",  20, 1160, 600, 1490)


# ═══════════════════════════════════════════════════════
# Image (5).png — Гарниры (1182 x 2560)
# Фри, Деревенский, Шарики, Наггетсы, Сырные палочки
# ═══════════════════════════════════════════════════════
print("\n[8] Image (5).png — Гарниры")
img = Image.open(os.path.join(BASE, "Image (5).png"))
# W=1182, H=2560

crop_and_remove(img, "fri",             20,  460, 400,  750)
crop_and_remove(img, "derevenskiy",     20,  760, 400, 1060)
crop_and_remove(img, "shar_kartof",     20, 1070, 400, 1360)
crop_and_remove(img, "naggetsyi",       20, 1370, 400, 1630)
crop_and_remove(img, "syrn_palochki",   20, 1640, 400, 1920)


print("\n\n✅ All done! Check dish_photos/nobg_v2/")
print(f"Total files: {len(os.listdir(OUT_NOBG))}")
