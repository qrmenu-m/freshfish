# -*- coding: utf-8 -*-
import sys; sys.stdout.reconfigure(encoding='utf-8')
"""
Build freshfish_menu.html with all dish photos embedded as base64.
"""
import base64, os, re

PHOTOS_DIR = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\dish_photos"
HTML_IN    = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\freshfish_menu.html"
HTML_OUT   = r"C:\Users\akika\Downloads\VS_code_projects\for_clients\task1-qr-menu\freshfish_menu.html"

def b64(filename):
    path = os.path.join(PHOTOS_DIR, filename)
    if not os.path.exists(path):
        print(f"  MISSING: {filename}")
        return None
    with open(path, "rb") as f:
        data = f.read()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()

# Map: dish key -> photo file
PHOTOS = {
    "sazan":           "sazan.jpg",
    "sudak":           "sudak.jpg",
    "som":             "som.jpg",
    "karas":           "karas.jpg",
    "bersh":           "bersh.jpg",
    "krilishki":       "krilishki.jpg",
    "krilishki_teri":  "krilishki_teri.jpg",
    "combo_klassika":  "combo_klassika.jpg",
    "combo_lyuks":     "combo_lyuks.jpg",
    "combo_shedevr":   "combo_shedevr.jpg",
    "set_mini":        "set_mini.jpg",
    "set_delikates":   "set_delikates.jpg",
    "set_daryi":       "set_daryi.jpg",
    "set_simfoniya":   "set_simfoniya.jpg",
    "set_freshfish":   "set_freshfish.jpg",
    "fri":             "fri.jpg",
    "derevenskiy":     "derevenskiy.jpg",
    "shar_kartof":     "shar_kartof.jpg",
    "naggetsyi":       "naggetsyi.jpg",
    "syrn_palochki":   "syrn_palochki.jpg",
    "acuchuk":         "acuchuk.jpg",
    "svej_salat":      "svej_salat.jpg",
    "grecheskiy":      "grecheskiy.jpg",
    "hrust_baklaj":    "hrust_baklaj.jpg",
    "morskoy_okun":    "morskoy_okun.jpg",
    "forel_gril":      "forel_gril.jpg",
    "forel_dorad":     "forel_dorad.jpg",
    "dorado":          "dorado.jpg",
    "semga_ris":       "semga_ris.jpg",
    "steyk_semga":     "steyk_semga.jpg",
    "krevetki":        "krevetki.jpg",
    "lukovye_kolca":   "lukovye_kolca.jpg",
    "ovoshi_gril":     "ovoshi_gril.jpg",
}

print("Loading photos...")
b64_map = {}
for key, fname in PHOTOS.items():
    result = b64(fname)
    if result:
        b64_map[key] = result
        print(f"  {key}: {len(result)//1024}KB")
    else:
        b64_map[key] = ""

print(f"\nLoaded {len([v for v in b64_map.values() if v])} photos")
print("Reading HTML...")

with open(HTML_IN, "r", encoding="utf-8") as f:
    html = f.read()

# Replace photo placeholder data-attrs with actual base64 src
# We'll replace all dish-img src="..." or data-src="..." patterns
# First, just report the current state
print(f"HTML size: {len(html)//1024}KB")
print("Saving with base64 map as JS variable...")

# Inject JS object with all base64 photos before </body>
js_inject = "\n<script>\n// Dish photos (base64)\nwindow.DISH_PHOTOS = {\n"
for key, val in b64_map.items():
    if val:
        js_inject += f'  "{key}": "{val}",\n'
js_inject += "};\n"
js_inject += """
// Apply photos to all dish-img elements
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('[data-dish-photo]').forEach(function(el) {
    var key = el.getAttribute('data-dish-photo');
    if (window.DISH_PHOTOS[key]) {
      if (el.tagName === 'IMG') {
        el.src = window.DISH_PHOTOS[key];
      } else {
        el.style.backgroundImage = 'url(' + window.DISH_PHOTOS[key] + ')';
      }
    }
  });
});
</script>
"""

html = html.replace("</body>", js_inject + "</body>")

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done! Output: {len(html)//1024}KB")
print("Note: Now we need to add data-dish-photo attributes to menu items in the HTML.")
