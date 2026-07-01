import re

with open(r'C:\Users\akika\Downloads\VS_code_projects\for_clients\qr_menu_fresfish\generate_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

orig_start = content.find('ORIGINALS = {')
orig_end = content.find('}', orig_start) + 1
originals_text = content[orig_start:orig_end]
originals_dict = eval(originals_text.split('=', 1)[1].strip())

used_keys = set()
for line in content.splitlines():
    for func in ['fish_card(', 'simple_card(', 'combo_card(', 'set_card(']:
        if func in line:
            parts = line.split(',')
            if len(parts) > 1:
                key = parts[1].strip().strip('\"').strip(' ')
                if key:
                    used_keys.add(key)

missing = sorted(list(used_keys - set(originals_dict.keys())))
print('Missing originals:')
for k in missing:
    print('-', k)
