# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding='utf-8')
"""Build the deployable QR menu at public/index.html."""
import base64, os

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
PHOTO_DIR = os.path.join(BASE_DIR, "menu_screen")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
OUT        = os.path.join(PUBLIC_DIR, "index.html")
LOGO_FILE  = os.path.join(BASE_DIR, "freshfish_logo.png")

def b64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return f"data:{mime_for(path)};base64," + base64.b64encode(data).decode()
    print(f"  MISSING: {path}")
    return ""

def mime_for(path):
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }.get(ext, "application/octet-stream")

def b64png(filename):
    path = os.path.join(PHOTO_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        src = f"data:{mime_for(path)};base64," + base64.b64encode(data).decode()
        print(f"  {filename}: {len(src)//1024} KB")
        return src
    print(f"  MISSING: {filename}")
    return ""

def img_tag(src, alt=""):
    if src:
        return f'<img src="{src}" alt="{alt}" loading="lazy">'
    return '<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:36px;">🐟</div>'

def kz_line(text, extra_style=""):
    if not text:
        return ""
    style = f' style="{extra_style}"' if extra_style else ""
    return f'<div class="fish-kz"{style}>{text}</div>'

def price_tags(prices):
    tags = []
    for w, p in prices:
        weight = f'<span class="pw">{w}</span>' if w else ""
        tags.append(f'<div class="pt">{weight}<span class="pa">{p}</span><span class="pu">тг</span></div>')
    return "".join(tags)

print("Loading PNGs...")
names = [
    "sazan","sudak","beliy_amur","som","karas","bersh",
    "lukovye_kolca","ovoshi_gril","krevetki","krilishki","krilishki_teri",
    "acuchuk","svej_salat","grecheskiy","hrust_baklaj",
    "morskoy_okun","forel_gril","dorado","semga_ris","steyk_semga",
    "karas_red","sudak_red","dorado_salad",
    "pizza_margarita","pizza_pepperoni","pizza_mushrooms","pizza_chicken","pizza_salmon",
    "hachapuri","flatbread","tom_yam","uha",
    "lemonade_watermelon_pomegranate","lemonade_orange","lemonade_kiwi_lime",
    "lemonade_strawberry_lime","lemonade_mango_passion","lemonade_cherry",
    "lemonade_berry","lemonade_kiwi_apple","lemonade_strawberry_mojito",
    "lemonade_mojito","lemonade_pomegranate",
    "combo_klassika","combo_lyuks","combo_shedevr",
    "set_mini","set_delikates","set_daryi","set_simfoniya","set_freshfish",
    "fri","derevenskiy","shar_kartof","naggetsyi","syrn_palochki",
]
photo_files = {
    "sazan": "сазан.png",
    "sudak": "судак.png",
    "beliy_amur": "белый амур.png",
    "som": "сом.png",
    "karas": "карась.png",
    "bersh": "берш.png",
    "morskoy_okun": "морской окунь.png",
    "forel_gril": "форель на гриле.png",
    "dorado": "дорадо.png",
    "semga_ris": "семга с рисом и салатом.png",
    "steyk_semga": "стейк из семги с рисом.png",
    "karas_red": "new_items/crucian_red_sauce.webp",
    "sudak_red": "new_items/pike_perch_red_sauce.webp",
    "dorado_salad": "new_items/dorado_grill_salad.webp",
    "pizza_margarita": "new_items/pizza_margarita.webp",
    "pizza_pepperoni": "new_items/pizza_pepperoni.webp",
    "pizza_mushrooms": "new_items/pizza_mushrooms.webp",
    "pizza_chicken": "new_items/pizza_chicken.webp",
    "pizza_salmon": "new_items/pizza_salmon.webp",
    "hachapuri": "new_items/hachapuri.webp",
    "flatbread": "new_items/flatbread.webp",
    "tom_yam": "new_items/tom_yam.webp",
    "uha": "new_items/uha.webp",
    "lemonade_watermelon_pomegranate": "new_items/lemonade_watermelon_pomegranate.webp",
    "lemonade_orange": "new_items/lemonade_orange.webp",
    "lemonade_kiwi_lime": "new_items/lemonade_kiwi_lime.webp",
    "lemonade_strawberry_lime": "new_items/lemonade_strawberry_lime.webp",
    "lemonade_mango_passion": "new_items/lemonade_mango_passion.webp",
    "lemonade_cherry": "new_items/lemonade_cherry.webp",
    "lemonade_berry": "new_items/lemonade_berry.webp",
    "lemonade_kiwi_apple": "new_items/lemonade_kiwi_apple.webp",
    "lemonade_strawberry_mojito": "new_items/lemonade_strawberry_mojito.webp",
    "lemonade_mojito": "new_items/lemonade_mojito.webp",
    "lemonade_pomegranate": "new_items/lemonade_pomegranate.webp",
    "krilishki": "крылышки.png",
    "krilishki_teri": "крылышки в соусе терияки.png",
    "acuchuk": "ачучук.png",
    "svej_salat": "свежий салат.png",
    "grecheskiy": "греческий салат.png",
    "hrust_baklaj": "хрустящие баклажаны.png",
    "lukovye_kolca": "луковые кольца.png",
    "ovoshi_gril": "овощи на гриле.png",
    "krevetki": "креветки королевские.png",
    "combo_klassika": "комбо классика.png",
    "combo_lyuks": "комбо люкс.png",
    "combo_shedevr": "комбо шедевр.png",
    "set_mini": "сет мини.png",
    "set_delikates": "сет деликатес.png",
    "set_daryi": "сет дары океана.png",
    "set_simfoniya": "сет морская симфония.png",
    "set_freshfish": "fresh fish сет.png",
    "fri": "фри.png",
    "derevenskiy": "картофель по деревенски.png",
    "shar_kartof": "картофельные шарики.png",
    "naggetsyi": "наггетсы.png",
    "syrn_palochki": "сырные палочки.png",
}
P = {name: "" for name in names}
for key, filename in photo_files.items():
    P[key] = b64png(filename)

LOGO = b64_image(LOGO_FILE)

WA = "https://api.whatsapp.com/send/?phone=77075832489&text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%0A%D0%9F%D0%B8%D1%88%D1%83+%D0%B8%D0%B7+QR-%D0%BC%D0%B5%D0%BD%D1%8E+Fresh+Fish%21&type=phone_number&app_absent=0"

def fish_card(card_id, photo_key, name_ru, name_kz, prices):
    """Horizontal card for fish: photo left, info right."""
    img = img_tag(P[photo_key], name_ru)
    return f"""
  <div class="card card-fish" id="{card_id}">
    <div class="fish-photo">{img}</div>
    <div class="fish-body">
      <div class="fish-name">{name_ru}</div>
      {kz_line(name_kz)}
      <div class="price-row">{price_tags(prices)}</div>
    </div>
  </div>"""

def simple_card(card_id, photo_key, name_ru, name_kz, desc, price):
    img = img_tag(P[photo_key], name_ru)
    return f"""
  <div class="card" id="{card_id}">
    <div class="card-simple">
      <div class="simple-photo">{img}</div>
      <div class="simple-info">
        <div class="fish-name">{name_ru}</div>
        {kz_line(name_kz)}
        {f'<div class="desc">{desc}</div>' if desc else ''}
      </div>
      <div class="price-single">{price}<span style="font-size:12px;font-weight:600"> тг</span></div>
    </div>
  </div>"""

def price_card(card_id, name_ru, desc, prices):
    return f"""
  <div class="card card-price" id="{card_id}">
    <div class="price-card-body">
      <div class="price-card-info">
        <div class="fish-name">{name_ru}</div>
        {f'<div class="desc">{desc}</div>' if desc else ''}
      </div>
      <div class="price-row price-row-compact">{price_tags(prices)}</div>
    </div>
  </div>"""

def combo_card(card_id, photo_key, name_ru, name_kz, price, col1, col2):
    img = img_tag(P[photo_key], name_ru)
    return f"""
  <div class="card card-combo" id="{card_id}">
    <div class="combo-photo">{img}</div>
    <div class="combo-header">
      <div class="combo-name">{name_ru}</div>
      {kz_line(name_kz, "color:var(--foam)")}
      <div class="combo-price">{price} тг</div>
    </div>
    <div class="combo-body">
      <div class="combo-cols">
        <div class="combo-col">{col1}</div>
        <div class="combo-col">{col2}</div>
      </div>
    </div>
  </div>"""

def set_card(card_id, photo_key, name_ru, name_kz, persons, price, col1, col2):
    img = img_tag(P[photo_key], name_ru)
    return f"""
  <div class="card card-set" id="{card_id}">
    <div class="set-photo">{img}</div>
    <div class="set-header">
      <div class="combo-name">{name_ru}</div>
      {kz_line(name_kz, "color:var(--foam)")}
      <div class="set-persons">👥 {persons}</div>
      <div class="set-price">{price} тг</div>
    </div>
    <div class="combo-body">
      <div class="combo-cols">
        <div class="combo-col">{col1}</div>
        <div class="combo-col">{col2}</div>
      </div>
    </div>
  </div>"""

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"/>
  <meta name="description" content="Fresh Fish — рыбный ресторан Карагандa. QR-меню."/>
  <title>Fresh Fish | QR-меню — Рыбный ресторан Карагандa</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Playfair+Display:wght@700&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
    :root{{
      --deep:#0a2540;--mid:#0e4d8a;--bright:#1a6fc4;
      --cyan:#00b4d8;--foam:#90e0ef;--accent:#ff6b2c;
      --gold:#f5c842;--white:#fff;--card:#f0f8ff;
      --tdark:#0a2540;--tmid:#2c5f8a;--tlight:#7fb3d3;
      --r:14px;--sh:0 4px 20px rgba(10,37,64,.12);
    }}
    html{{scroll-behavior:smooth}}
    body{{font-family:'Nunito',sans-serif;background:linear-gradient(180deg,#e8f4ff 0%,#f0f8ff 100%);color:var(--tdark);overflow-x:hidden;min-height:100vh}}

    /* HERO */
    .hero{{background:linear-gradient(145deg,var(--deep) 0%,var(--mid) 55%,var(--bright) 100%);padding:36px 20px 28px;text-align:center;position:relative;overflow:hidden}}
    .hero::before{{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 320'%3E%3Cpath fill='rgba(255,255,255,0.04)' d='M0,160L48,138.7C96,117,192,75,288,80C384,85,480,139,576,149.3C672,160,768,128,864,122.7C960,117,1056,139,1152,144C1248,149,1344,139,1392,133.3L1440,128V320H0Z'/%3E%3C/svg%3E") center/cover no-repeat}}
    .logo-wrap{{display:flex;align-items:center;justify-content:center;margin-bottom:10px}}
    .brand-logo-frame{{width:138px;height:138px;border-radius:50%;overflow:hidden;background:#eaf6ff;border:3px solid rgba(255,255,255,.75);box-shadow:0 8px 28px rgba(0,0,0,.28),0 0 0 6px rgba(144,224,239,.14)}}
    .brand-logo{{width:100%;height:100%;object-fit:cover;object-position:center;display:block}}
    .brand-name{{font-family:'Playfair Display',serif;font-size:34px;font-weight:700;color:#fff;letter-spacing:1px;text-shadow:0 2px 12px rgba(0,0,0,.3)}}
    .brand-sub{{font-size:13px;font-weight:600;color:var(--foam);letter-spacing:3px;text-transform:uppercase;margin-bottom:14px}}
    .hero-badge{{display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.25);backdrop-filter:blur(8px);border-radius:30px;padding:6px 16px;font-size:12px;color:var(--foam);font-weight:600}}
    .social-strip{{display:flex;justify-content:center;gap:10px;margin-top:16px;flex-wrap:wrap}}
    .social-btn{{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:30px;font-size:12px;font-weight:700;text-decoration:none;transition:transform .2s,opacity .2s}}
    .social-btn:active{{transform:scale(.95);opacity:.85}}
    .btn-wa{{background:#25d366;color:#fff}}
    .btn-tt{{background:linear-gradient(135deg,#010101 60%,#69c9d0);color:#fff}}
    .btn-2g{{background:var(--bright);color:#fff}}

    /* NAV */
    .nav-wrap{{position:sticky;top:0;z-index:100;background:rgba(255,255,255,.93);backdrop-filter:blur(12px);border-bottom:2px solid var(--foam);padding:10px 0;box-shadow:0 2px 16px rgba(10,37,64,.10)}}
    .nav-scroll{{display:flex;gap:8px;overflow-x:auto;padding:0 16px;scrollbar-width:none}}
    .nav-scroll::-webkit-scrollbar{{display:none}}
    .nav-btn{{flex-shrink:0;background:var(--card);border:2px solid var(--foam);border-radius:30px;padding:7px 16px;font-family:'Nunito',sans-serif;font-size:13px;font-weight:700;color:var(--mid);cursor:pointer;transition:all .2s;white-space:nowrap}}
    .nav-btn.active,.nav-btn:hover{{background:linear-gradient(135deg,var(--bright),var(--cyan));border-color:transparent;color:#fff;box-shadow:0 4px 12px rgba(26,111,196,.35)}}

    /* MAIN */
    .main{{padding:0 16px 120px;max-width:480px;margin:0 auto}}
    .section{{margin-top:32px}}
    .section-header{{display:flex;align-items:center;gap:12px;margin-bottom:16px}}
    .section-icon{{width:44px;height:44px;background:linear-gradient(135deg,var(--bright),var(--cyan));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 4px 12px rgba(26,111,196,.3);flex-shrink:0}}
    .section-title{{font-size:20px;font-weight:900;color:var(--deep)}}
    .section-kz{{font-size:12px;font-weight:600;color:var(--tlight);letter-spacing:1px}}
    .price-notice{{background:linear-gradient(135deg,var(--mid),var(--bright));color:#fff;border-radius:12px;padding:10px 16px;margin-bottom:16px;font-size:12px;font-weight:600;display:flex;align-items:center;gap:8px}}

    /* CARD BASE */
    .card{{background:#fff;border-radius:var(--r);box-shadow:var(--sh);overflow:hidden;margin-bottom:14px;border:1px solid rgba(144,224,239,.3);opacity:0;transform:translateY(20px);transition:opacity .5s,transform .5s,box-shadow .2s}}
    .card.visible{{opacity:1;transform:translateY(0)}}
    .card:active{{box-shadow:0 2px 8px rgba(10,37,64,.08);transform:scale(.99)}}

    /* FISH CARD */
    .card-fish{{display:flex;align-items:stretch}}
    .fish-photo{{
      width:110px;flex-shrink:0;
      background:linear-gradient(135deg,#dff0fa,#b8e0f7);
      display:flex;align-items:center;justify-content:center;
      padding:8px;overflow:hidden;
    }}
    .fish-photo img{{width:100%;height:100%;object-fit:contain;display:block}}
    .fish-body{{flex:1;padding:14px}}
    .fish-name{{font-size:15px;font-weight:800;color:var(--deep);line-height:1.3}}
    .fish-kz{{font-size:11px;color:var(--tlight);font-weight:600;margin-bottom:8px}}
    .desc{{font-size:12px;color:var(--tmid);margin-top:3px}}
    .price-row{{display:flex;gap:8px;flex-wrap:wrap}}
    .pt{{display:flex;flex-direction:column;align-items:center;background:var(--card);border:2px solid var(--foam);border-radius:10px;padding:6px 12px;min-width:68px}}
    .pw{{font-size:10px;font-weight:700;color:var(--tlight);text-transform:uppercase}}
    .pa{{font-size:17px;font-weight:900;color:var(--bright);line-height:1.1}}
    .pu{{font-size:9px;color:var(--tlight)}}

    /* SIMPLE CARD */
    .card-simple{{display:flex;align-items:center;gap:14px;padding:14px}}
    .simple-photo{{
      width:76px;height:76px;flex-shrink:0;
      background:linear-gradient(135deg,#dff0fa,#b8e0f7);
      border-radius:12px;overflow:hidden;
      display:flex;align-items:center;justify-content:center;
      padding:4px;
    }}
    .simple-photo img{{width:100%;height:100%;object-fit:contain;display:block}}
    .simple-info{{flex:1}}
    .price-single{{font-size:19px;font-weight:900;color:var(--bright);white-space:nowrap;text-align:right}}

    /* PRICE-ONLY CARD */
    .card-price{{overflow:visible}}
    .price-card-body{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px}}
    .price-card-info{{flex:1;min-width:0}}
    .price-row-compact{{justify-content:flex-end;flex-shrink:0}}
    .price-row-compact .pt{{min-width:64px;padding:5px 10px}}
    .price-row-compact .pa{{font-size:16px}}

    /* COMBO CARD */
    .card-combo,.card-set{{padding:0}}
    .combo-photo,.set-photo{{
      width:100%;height:180px;overflow:hidden;
      background:linear-gradient(135deg,#dff0fa,#b8e0f7);
      display:flex;align-items:center;justify-content:center;
    }}
    .combo-photo img,.set-photo img{{width:100%;height:100%;object-fit:contain;display:block}}
    .combo-header{{background:linear-gradient(135deg,var(--deep),var(--mid));padding:14px 16px 10px}}
    .set-header{{background:linear-gradient(135deg,#0a3d6b,var(--bright));padding:14px 16px 10px}}
    .combo-name{{font-size:16px;font-weight:900;color:#fff}}
    .combo-price{{display:inline-block;background:var(--gold);color:var(--deep);font-size:22px;font-weight:900;padding:4px 16px;border-radius:8px;margin-top:8px}}
    .set-persons{{font-size:11px;color:var(--cyan);font-weight:700;margin-top:2px}}
    .set-price{{display:inline-block;background:linear-gradient(135deg,var(--accent),#ff8c4c);color:#fff;font-size:22px;font-weight:900;padding:4px 16px;border-radius:8px;margin-top:8px;box-shadow:0 4px 12px rgba(255,107,44,.3)}}
    .combo-body{{padding:14px 16px}}
    .combo-cols{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
    .combo-col{{font-size:11px;color:var(--tmid);line-height:1.6}}

    /* REVIEWS */
    .reviews-section{{margin-top:36px}}
    .reviews-intro{{text-align:center;background:linear-gradient(135deg,var(--deep),var(--mid));border-radius:var(--r);padding:20px 16px;margin-bottom:16px;color:#fff}}
    .reviews-intro h3{{font-size:18px;font-weight:900;margin-bottom:6px}}
    .reviews-intro p{{font-size:12px;color:var(--foam);line-height:1.5}}
    .review-cards{{display:flex;flex-direction:column;gap:12px}}
    .review-card{{background:#fff;border-radius:var(--r);box-shadow:var(--sh);border:1px solid rgba(144,224,239,.3);overflow:hidden;opacity:0;transform:translateY(20px);transition:opacity .5s,transform .5s}}
    .review-card.visible{{opacity:1;transform:translateY(0)}}
    .review-inner{{display:flex;align-items:center;gap:14px;padding:14px}}
    .review-thumb{{width:72px;height:72px;flex-shrink:0;background:linear-gradient(135deg,var(--mid),var(--cyan));border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:32px;position:relative;overflow:hidden}}
    .play-over{{position:absolute;inset:0;background:rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;font-size:20px}}
    .review-info{{flex:1}}
    .review-name{{font-size:14px;font-weight:800;color:var(--deep)}}
    .review-stars{{font-size:13px;color:var(--gold);margin:2px 0}}
    .review-text{{font-size:12px;color:var(--tmid);line-height:1.4}}
    .review-link{{display:block;text-align:center;background:linear-gradient(135deg,#010101,#69c9d0);color:#fff;font-size:12px;font-weight:700;padding:10px;text-decoration:none}}
    .reviews-cta{{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#010101,#333);color:#fff;text-decoration:none;border-radius:var(--r);padding:14px 20px;font-size:14px;font-weight:800;margin-top:12px;box-shadow:0 4px 16px rgba(0,0,0,.2);transition:transform .2s}}
    .reviews-cta:active{{transform:scale(.97)}}

    /* CONTACTS */
    .contacts{{margin-top:36px;background:linear-gradient(145deg,var(--deep),var(--mid));border-radius:var(--r);padding:24px 20px;color:#fff}}
    .contacts h2{{font-size:20px;font-weight:900;margin-bottom:18px;text-align:center}}
    .contact-item{{display:flex;align-items:flex-start;gap:14px;margin-bottom:16px}}
    .contact-icon{{width:42px;height:42px;flex-shrink:0;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px}}
    .contact-label{{font-size:11px;color:var(--foam);font-weight:600;margin-bottom:2px;text-transform:uppercase;letter-spacing:1px}}
    .contact-value{{font-size:14px;font-weight:700}}
    .contact-value a{{color:#fff;text-decoration:none}}
    .branch-divider{{border:none;border-top:1px solid rgba(255,255,255,.15);margin:16px 0}}
    .hours-row{{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}}
    .hours-day{{font-size:12px;color:var(--foam)}}
    .hours-time{{font-size:14px;font-weight:800}}
    .map-btns{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:18px}}
    .map-btn{{display:flex;align-items:center;justify-content:center;gap:6px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.25);border-radius:12px;padding:12px 8px;color:#fff;text-decoration:none;font-size:12px;font-weight:700}}

    /* FAB */
    .fab-wrap{{position:fixed;bottom:24px;right:16px;display:flex;flex-direction:column;gap:10px;z-index:200}}
    .fab{{width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;text-decoration:none;box-shadow:0 6px 20px rgba(0,0,0,.25);transition:transform .2s}}
    .fab:active{{transform:scale(.9)}}
    .fab-wa{{background:#25d366}}
    .fab-call{{background:linear-gradient(135deg,var(--bright),var(--cyan))}}

    /* BUBBLES */
    .bubble{{position:fixed;border-radius:50%;pointer-events:none;opacity:.05;animation:rise linear infinite}}
    @keyframes rise{{0%{{bottom:-60px;opacity:.05}}100%{{bottom:110%;opacity:0}}}}

    .footer{{text-align:center;padding:24px 16px;color:var(--tlight);font-size:11px;line-height:1.6}}
  </style>
</head>
<body>

<div class="bubble" style="width:40px;height:40px;left:10%;background:#1a6fc4;animation-duration:8s;animation-delay:0s"></div>
<div class="bubble" style="width:25px;height:25px;left:30%;background:#00b4d8;animation-duration:11s;animation-delay:2s"></div>
<div class="bubble" style="width:55px;height:55px;left:70%;background:#0e4d8a;animation-duration:9s;animation-delay:4s"></div>
<div class="bubble" style="width:20px;height:20px;left:85%;background:#90e0ef;animation-duration:7s;animation-delay:1s"></div>

<!-- HERO -->
<header class="hero">
  <div class="logo-wrap">
    <div class="brand-logo-frame">
      <img class="brand-logo" src="{LOGO}" alt="Fresh Fish" width="138" height="138">
    </div>
  </div>
  <div class="brand-name">Fresh Fish</div>
  <p class="brand-sub">Рыбный ресторан · Қарағанды</p>
  <div class="hero-badge"><span>🌊</span> Свежая рыба каждый день</div>
  <div class="social-strip">
    <a href="{WA}" class="social-btn btn-wa" id="hero-wa">💬 WhatsApp</a>
    <a href="https://www.tiktok.com/@fresh_fish.krg1" class="social-btn btn-tt" target="_blank" id="hero-tt">🎵 TikTok</a>
    <a href="tel:+77006272750" class="social-btn btn-2g" id="hero-call">📞 Позвонить</a>
  </div>
</header>

<!-- NAV -->
<nav class="nav-wrap">
  <div class="nav-scroll">
    <button class="nav-btn active" onclick="goTo('hot')"     id="nav-hot">🔥 Горячие</button>
    <button class="nav-btn"        onclick="goTo('pizza')"   id="nav-pizza">🍕 Пицца / Выпечка</button>
    <button class="nav-btn"        onclick="goTo('soups')"   id="nav-soups">🍲 Супы</button>
    <button class="nav-btn"        onclick="goTo('wings')"   id="nav-wings">🍗 Крылышки</button>
    <button class="nav-btn"        onclick="goTo('salads')"  id="nav-salads">🥗 Салаты</button>
    <button class="nav-btn"        onclick="goTo('combos')"  id="nav-combos">🎁 Комбо</button>
    <button class="nav-btn"        onclick="goTo('sets')"    id="nav-sets">🦞 Сеты</button>
    <button class="nav-btn"        onclick="goTo('sides')"   id="nav-sides">🍟 Гарниры</button>
    <button class="nav-btn"        onclick="goTo('lemonades')" id="nav-lemonades">🍋 Лимонады</button>
    <button class="nav-btn"        onclick="goTo('tea')"     id="nav-tea">🍵 Чай</button>
    <button class="nav-btn"        onclick="goTo('drinks')"  id="nav-drinks">🥤 Напитки</button>
    <button class="nav-btn"        onclick="goTo('reviews')" id="nav-reviews">⭐ Отзывы</button>
    <button class="nav-btn"        onclick="goTo('contacts')"id="nav-contacts">📍 Контакты</button>
  </div>
</nav>

<main class="main">

<!-- ═══ ГОРЯЧИЕ БЛЮДА ═══ -->
<section class="section" id="hot">
  <div class="section-header">
    <div class="section-icon">🔥</div>
    <div><div class="section-title">Горячие блюда</div><div class="section-kz">ЫСТЫҚ ТАҒАМДАР</div></div>
  </div>
  <div class="price-notice">⚖️ Цена зависит от веса рыбы (0.5 кг или 1 кг)</div>
  {fish_card("c-sazan",  "sazan",       "Сазан",                "Сазан балығы",        [("0.5 кг","3 650"),("1 кг","6 500")])}
  {fish_card("c-sudak",  "sudak",       "Судак",                "Кёксерке",            [("0.5 кг","3 350"),("1 кг","6 500")])}
  {fish_card("c-som",    "beliy_amur",  "Белый амур",           "Ақ амур",             [("0.5 кг","3 500"),("1 кг","6 800")])}
  {fish_card("c-som2",   "som",         "Сом",                  "Жайын",               [("0.5 кг","3 100"),("1 кг","6 000")])}
  {fish_card("c-karas",  "karas",       "Карась",               "Моңке балығы",        [("0.5 кг","2 100"),("1 кг","4 000")])}
  {fish_card("c-bersh",  "bersh",       "Берш",                 "Берш балығы",         [("0.5 кг","2 600"),("1 кг","5 000")])}
  {fish_card("c-okun",   "morskoy_okun","Морской окунь",        "Теңіз алабұғысы",     [("0.4 кг","3 500"),("0.8 кг","6 800")])}
  {fish_card("c-forel",  "forel_gril",  "Форель на гриле",      "Грильдегі Ханбалық",  [("0.4 кг","3 800"),("0.8 кг","7 500")])}
  {fish_card("c-dorado", "dorado",      "Дорадо",               "Дорадо",              [("0.4 кг","5 600"),("0.8 кг","10 900")])}
  {fish_card("c-karas-red", "karas_red", "Карась в красном соусе", "",                  [("0.5 кг","2 650"),("1 кг","4 500")])}
  {fish_card("c-sudak-red", "sudak_red", "Судак в красном соусе", "",                   [("0.5 кг","3 850"),("1 кг","7 000")])}
  {fish_card("c-dorado-salad", "dorado_salad", "Дорадо на гриле с салатом", "",        [("0.4 кг","6 200")])}
  {fish_card("c-semga",  "semga_ris",   "Сёмга с рисом и салатом","Аксерке күріш",    [("250 г","3 300")])}
  {fish_card("c-steyk",  "steyk_semga", "Стейк из сёмги с рисом","Аксерке стейкі",    [("0.4 кг","5 800")])}
</section>

<!-- ═══ ПИЦЦА / ВЫПЕЧКА ═══ -->
<section class="section" id="pizza">
  <div class="section-header">
    <div class="section-icon">🍕</div>
    <div><div class="section-title">Пицца / Выпечка</div><div class="section-kz">ПИЦЦА ЖӘНЕ НАН ӨНІМДЕРІ</div></div>
  </div>
  {simple_card("c-pizza-margarita", "pizza_margarita", "Пицца Маргарита", "", "", "2 000")}
  {simple_card("c-pizza-pepperoni", "pizza_pepperoni", "Пицца Пеперони", "", "", "2 200")}
  {simple_card("c-pizza-mushrooms", "pizza_mushrooms", "Пицца с грибами", "", "", "2 200")}
  {simple_card("c-pizza-chicken", "pizza_chicken", "Пицца с курицей", "", "", "2 200")}
  {simple_card("c-pizza-salmon", "pizza_salmon", "Пицца с сёмгой", "", "", "2 400")}
  {simple_card("c-hachapuri", "hachapuri", "Хачапури", "", "", "2 290")}
  {simple_card("c-flatbread", "flatbread", "Лепёшки", "", "", "300")}
</section>

<!-- ═══ СУПЫ ═══ -->
<section class="section" id="soups">
  <div class="section-header">
    <div class="section-icon">🍲</div>
    <div><div class="section-title">Супы</div><div class="section-kz">СОРПАЛАР</div></div>
  </div>
  {price_card("c-seafood-soup", "Суп из морепродуктов", "", [("", "2 450")])}
  {simple_card("c-tom-yam", "tom_yam", "Том-ям", "", "", "2 600")}
  {simple_card("c-uha", "uha", "Уха", "", "", "1 700")}
</section>

<!-- ═══ КРЫЛЫШКИ ═══ -->
<section class="section" id="wings">
  <div class="section-header">
    <div class="section-icon">🍗</div>
    <div><div class="section-title">Крылышки</div><div class="section-kz">ТАУЫҚ ҚАНАТТАРЫ</div></div>
  </div>
  {simple_card("c-kril1","krilishki",      "Крылышки",                "Тауық қанаттары","10 штук","1 800")}
  {simple_card("c-kril2","krilishki_teri", "Крылышки в соусе Терияки","Терияки қанаттары","10 штук","1 950")}
</section>

<!-- ═══ САЛАТЫ ═══ -->
<section class="section" id="salads">
  <div class="section-header">
    <div class="section-icon">🥗</div>
    <div><div class="section-title">Салаты</div><div class="section-kz">САЛАТТАР</div></div>
  </div>
  {simple_card("c-acuchuk",   "acuchuk",      "Ачучук",                "Ашытқы салат", "", "1 190")}
  {simple_card("c-svej",      "svej_salat",   "Свежий салат",          "Балғын салат", "", "1 590")}
  {simple_card("c-greek",     "grecheskiy",   "Греческий салат",       "Грек салаты",  "", "1 990")}
  {simple_card("c-baklaj",    "hrust_baklaj", "Хрустящие баклажаны",   "Қытырлақ баялды", "", "1 990")}
  {simple_card("c-kolca",     "lukovye_kolca","Луковые кольца",        "Пияз сақиналары","10 шт", "1 250")}
  {simple_card("c-gril-veg",  "ovoshi_gril",  "Овощи на гриле",        "Грильдегі көкөністер","350 г","1 550")}
  {simple_card("c-krevetki",  "krevetki",     "Креветки",              "Асшаяндар","350 г","3 550")}
</section>

<!-- ═══ КОМБО ═══ -->
<section class="section" id="combos">
  <div class="section-header">
    <div class="section-icon">🎁</div>
    <div><div class="section-title">Комбо</div><div class="section-kz">КОМБОЛАР</div></div>
  </div>
  {combo_card("c-combo1","combo_klassika",
    "Комбо «Классика»","«Классикалық» Комбо","10 990",
    "Судак 750 г, Сазан 750 г, Картофельные дольки 350 г, Фри 250 г, Соус, лук, лимон",
    "Кёксерке 750 г, Сазан 750 г, Картопсыналары 350 г, Фри 250 г, Тұздық, пияз, лимон")}
  {combo_card("c-combo2","combo_lyuks",
    "Комбо «Люкс»","«Люкс» Комбосы","12 990",
    "Судак 750 г, Сом 750 г, Луковые кольца 10 шт, Картопсыналары 350 г, Соус, лук, лимон",
    "Кёксерке 750 г, Сом 750 г, Пияз сақиналары 10 дана, Картопсыналары 350 г, Тұздық, пияз, лимон")}
  {combo_card("c-combo3","combo_shedevr",
    "Комбо «Шедевр»","«Шедевр» Комбосы","13 990",
    "Сазан 750 г, Сом 750 г, Крылышки терияки 700 г, Луковые кольца 10 шт, Дольки 350 г, Соус, лук, лимон",
    "Сазан 750 г, Сом 750 г, Терияки қанатшалары 700 г, Пияз сақиналары 10 дана, Картопсыналары 350 г, Тұздық, пияз, лимон")}
</section>

<!-- ═══ СЕТЫ ═══ -->
<section class="section" id="sets">
  <div class="section-header">
    <div class="section-icon">🦞</div>
    <div><div class="section-title">Сеты</div><div class="section-kz">СЕТТЕР</div></div>
  </div>
  {set_card("c-set1","set_mini",
    "Сет «Мини»","«Мини» сеті","На 3–4 персоны","13 990",
    "Сазан 500 г, Сом/Судак 500 г, Форель 400 г, Сёмга 300 г, Фри 250 г, Соус, лук, лимон",
    "Сазан 500 г, Сом/Кёксерке 500 г, Ханбалық 400 г, Аксерке 300 г, Фри 250 г, Тұздық, пияз, лимон")}
  {set_card("c-set2","set_delikates",
    "Сет «Деликатес»","«Деликатес» сеті","На 5–6 персон","16 490",
    "Сазан 500 г, Судак 500 г, Форель на гриле 800 г, Креветки 500 г, Фри 250 г, Овощи на гриле 250 г, Соус, лук, лимон",
    "Сазан 500 г, Кёксерке 500 г, Грильдегі Ханбалық 800 г, Асшаяндар 500 г, Фри 250 г, Грильдегі көкөністер 350 г, Тұздық, пияз, лимон")}
  {set_card("c-set3","set_daryi",
    "Сет «Дары Океана»","«Теңіз сыйлары» сеті","На 5–6 персон","17 990",
    "Сазан 500 г, Берш 550 г, Сёмга 700 г, Креветки 300 г, Фри 250 г, Дольки 350 г, Овощи 300 г, Соус, лук, лимон",
    "Сазан 500 г, Берш 550 г, Аксерке 700 г, Асшаяндар 300 г, Фри 250 г, Картопсыналары 350 г, Грильдегі көкөністер 500 г, Тұздық, пияз, лимон")}
  {set_card("c-set4","set_simfoniya",
    "Сет «Морская симфония»","«Теңіз симфониясы» сеті","На 5–6 персон","23 490",
    "Дорадо 400 г, Окунь 400 г, Судак 1 кг, Сёмга 700 г, Фри 250 г, Дольки 350 г, Королевские Креветки 350 г, Овощи на гриле 350 г, Соус, лук, лимон",
    "Дорадо 400 г, Алабуға 400 г, Кёксерке 1 кг, Аксерке 700 г, Фри 250 г, Картопсыналары 350 г, Асшаяндар 350 г, Грильдегі Көкөністер 350 г, Тұздық, пияз, лимон")}
  {set_card("c-set5","set_freshfish",
    "Сет «Fresh Fish»","«Fresh Fish» сеті","На 6–7 персон","25 490",
    "Сазан 500 г, Берш 500 г, Форель на гриле 800 г, Сёмга 700 г, Креветки 300 г, Фри 250 г, Овощи на гриле 300 г, Картопшарлары 250 г, Соус, лук, лимон",
    "Сазан 500 г, Берш 500 г, Грильдегі Ханбалық 800 г, Аксерке 700 г, Асшаяндар 300 г, Фри 250 г, Грильдегі Көкөністер 300 г, Картоп Шарлары 250 г, Тұздық, пияз, лимон")}
</section>

<!-- ═══ ГАРНИРЫ ═══ -->
<section class="section" id="sides">
  <div class="section-header">
    <div class="section-icon">🍟</div>
    <div><div class="section-title">Гарниры</div><div class="section-kz">ГАРНИРЛЕР</div></div>
  </div>
  {simple_card("c-fri",    "fri",           "Фри",                     "Картоп фри","250 г","850")}
  {simple_card("c-derev",  "derevenskiy",   "Картофель по-деревенски", "Рустикалық картоп","350 г","800")}
  {simple_card("c-shar",   "shar_kartof",   "Картофельные шарики",     "Картоп шарлары","250 г","850")}
  {simple_card("c-nagg",   "naggetsyi",     "Наггетсы",                "Наггетсылер","6 шт","800")}
  {simple_card("c-syr",    "syrn_palochki", "Сырные палочки",          "Ірімшік таяқшалары","6 шт","800")}
</section>

<!-- ═══ ЛИМОНАДЫ ═══ -->
<section class="section" id="lemonades">
  <div class="section-header">
    <div class="section-icon">🍋</div>
    <div><div class="section-title">Лимонады</div><div class="section-kz">ЛИМОНАДТАР</div></div>
  </div>
  {simple_card("c-lem-watermelon-pomegranate", "lemonade_watermelon_pomegranate", "Лимонад Арбуз и гранат", "", "1,2 л", "2 000")}
  {simple_card("c-lem-orange", "lemonade_orange", "Лимонад Апельсин", "", "1,2 л", "2 000")}
  {simple_card("c-lem-kiwi-lime", "lemonade_kiwi_lime", "Лимонад Киви лайм", "", "1,2 л", "2 000")}
  {simple_card("c-lem-strawberry-lime", "lemonade_strawberry_lime", "Лимонад Клубника лайм", "", "1,2 л", "2 000")}
  {simple_card("c-lem-mango-passion", "lemonade_mango_passion", "Лимонад Манго маракуйя", "", "1,2 л", "2 000")}
  {simple_card("c-lem-cherry", "lemonade_cherry", "Лимонад Вишня", "", "1,2 л", "2 000")}
  {simple_card("c-lem-berry", "lemonade_berry", "Лимонад Ягодный", "", "1,2 л", "2 000")}
  {simple_card("c-lem-kiwi-apple", "lemonade_kiwi_apple", "Лимонад Киви яблоко", "", "1,2 л", "2 000")}
  {simple_card("c-lem-strawberry-mojito", "lemonade_strawberry_mojito", "Лимонад Клубника мохито", "", "1,2 л", "2 000")}
  {simple_card("c-lem-mojito", "lemonade_mojito", "Лимонад Мохито", "", "1,2 л", "2 000")}
  {simple_card("c-lem-pomegranate", "lemonade_pomegranate", "Лимонад Гранат", "", "1,2 л", "2 000")}
</section>

<!-- ═══ ЧАЙ ═══ -->
<section class="section" id="tea">
  <div class="section-header">
    <div class="section-icon">🍵</div>
    <div><div class="section-title">Чай</div><div class="section-kz">ШАЙ</div></div>
  </div>
  {price_card("c-tea-tashkent", "Чай Ташкентский", "", [("", "1 500")])}
  {price_card("c-tea-black-1l", "Чай чёрный", "", [("1 л", "900"), ("0,35 л", "300")])}
  {price_card("c-tea-green-1l", "Чай зелёный", "", [("1 л", "900"), ("0,35 л", "300")])}
  {price_card("c-tea-milk", "Чай чёрный с молоком", "", [("", "1 700")])}
  {price_card("c-tea-berry", "Чай ягодный", "", [("", "1 700")])}
  {price_card("c-tea-ginger", "Чай имбирный", "", [("", "1 700")])}
  {price_card("c-tea-moroccan", "Чай марокканский", "", [("", "1 700")])}
</section>

<!-- ═══ НАПИТКИ ═══ -->
<section class="section" id="drinks">
  <div class="section-header">
    <div class="section-icon">🥤</div>
    <div><div class="section-title">Напитки</div><div class="section-kz">СУСЫНДАР</div></div>
  </div>
  {price_card("c-cola", "Кола", "", [("", "800")])}
  {price_card("c-pepsi", "Пепси", "", [("", "800")])}
  {price_card("c-fanta", "Фанта", "", [("", "800")])}
  {price_card("c-sprite", "Спрайт", "", [("", "800")])}
  {price_card("c-juice", "Сок", "", [("1 л", "1 100"), ("0,25 л", "400")])}
  {price_card("c-water", "Вода без газа", "", [("1 л", "600"), ("0,5 л", "300")])}
  {price_card("c-saryagash", "Сарыагаш", "1,2 л", [("", "650")])}
</section>

<!-- ═══ ОТЗЫВЫ ═══ -->
<section class="section reviews-section" id="reviews">
  <div class="reviews-intro">
    <h3>⭐ Видеоотзывы гостей</h3>
    <p>Смотрите как гости наслаждаются нашими блюдами в TikTok!</p>
  </div>
  <div class="review-cards">
    <div class="review-card" id="rev1">
      <div class="review-inner">
        <div class="review-thumb">🍽️<div class="play-over">▶️</div></div>
        <div class="review-info">
          <div class="review-name">Айгерим С.</div>
          <div class="review-stars">★★★★★</div>
          <div class="review-text">«Потрясающий сет Деликатес! Рыба свежайшая, очень сочная. Теперь ходим каждые выходные!»</div>
        </div>
      </div>
      <a href="https://www.tiktok.com/@fresh_fish.krg1" class="review-link" target="_blank">▶ Смотреть в TikTok</a>
    </div>
    <div class="review-card" id="rev2">
      <div class="review-inner">
        <div class="review-thumb">🐟<div class="play-over">▶️</div></div>
        <div class="review-info">
          <div class="review-name">Дмитрий К.</div>
          <div class="review-stars">★★★★★</div>
          <div class="review-text">«Дорадо — просто шедевр! Комбо Классика идеально на двоих. Лучшая рыбная кухня в Карагандe!»</div>
        </div>
      </div>
      <a href="https://www.tiktok.com/@fresh_fish.krg1" class="review-link" target="_blank">▶ Смотреть в TikTok</a>
    </div>
    <div class="review-card" id="rev3">
      <div class="review-inner">
        <div class="review-thumb">🦐<div class="play-over">▶️</div></div>
        <div class="review-info">
          <div class="review-name">Мадина Т.</div>
          <div class="review-stars">★★★★★</div>
          <div class="review-text">«Крылышки в Терияки и греческий салат — идеальное сочетание! Обязательно попробуйте сет Fresh Fish!»</div>
        </div>
      </div>
      <a href="https://www.tiktok.com/@fresh_fish.krg1" class="review-link" target="_blank">▶ Смотреть в TikTok</a>
    </div>
  </div>
  <a href="https://www.tiktok.com/@fresh_fish.krg1" class="reviews-cta" target="_blank" id="tiktok-all">
    🎵 Все видеоотзывы в TikTok @fresh_fish.krg1
  </a>
</section>

<!-- ═══ КОНТАКТЫ ═══ -->
<section class="contacts" id="contacts">
  <h2>📍 Контакты</h2>
  <div class="contact-item">
    <div class="contact-icon">📞</div>
    <div>
      <div class="contact-label">Телефоны</div>
      <div class="contact-value">
        <a href="tel:+77006272750">+7 700 627-27-50</a><br>
        <a href="tel:+77075832489">+7 707 583-24-89</a>
      </div>
    </div>
  </div>
  <hr class="branch-divider"/>
  <div class="contact-item">
    <div class="contact-icon">🕐</div>
    <div>
      <div class="contact-label">Режим работы</div>
      <div class="contact-value">
        <div class="hours-row"><span class="hours-day">Пн–Пт</span><span class="hours-time">11:00–23:00</span></div>
        <div class="hours-row"><span class="hours-day">Сб–Вс</span><span class="hours-time">10:00–24:00</span></div>
      </div>
    </div>
  </div>
  <div class="map-btns">
    <a href="https://2gis.kz/karaganda/search/Fresh%20Fish" class="map-btn" target="_blank" id="map-2gis">🗺️ 2ГИС</a>
    <a href="{WA}" class="map-btn" id="wa-contact">💬 Написать</a>
  </div>
</section>

</main>

<footer class="footer">
  <p>🐟 Fresh Fish Karaganda · Свежая рыба каждый день</p>
  <p>© 2024 Все права защищены</p>
</footer>

<div class="fab-wrap">
  <a href="{WA}" class="fab fab-wa" id="fab-wa">💬</a>
  <a href="tel:+77006272750" class="fab fab-call" id="fab-call">📞</a>
</div>

<script>
  function goTo(id) {{ document.getElementById(id).scrollIntoView({{behavior:'smooth',block:'start'}}); }}
  const secs = ['hot','pizza','soups','wings','salads','combos','sets','sides','lemonades','tea','drinks','reviews','contacts'];
  const btns = document.querySelectorAll('.nav-btn');
  function setActive(id) {{ btns.forEach(b=>b.classList.remove('active')); const i=secs.indexOf(id); if(i>=0) btns[i].classList.add('active'); }}
  const obs = new IntersectionObserver(entries=>{{
    entries.forEach(e=>{{
      if(e.isIntersecting){{
        e.target.classList.add('visible');
        if(secs.includes(e.target.id)) setActive(e.target.id);
      }}
    }});
  }},{{threshold:0.12}});
  document.querySelectorAll('.card,.review-card').forEach(el=>obs.observe(el));
  secs.forEach(id=>{{const el=document.getElementById(id);if(el)obs.observe(el);}});
</script>
</body>
</html>"""

os.makedirs(PUBLIC_DIR, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

size_kb = os.path.getsize(OUT) // 1024
print(f"\nDone! public/index.html = {size_kb} KB")
