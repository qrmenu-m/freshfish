# freshfish

Статическое QR-меню Fresh Fish.

## Публикация в Cloudflare

```bash
npx wrangler deploy
```

Wrangler публикует папку `public`, указанную в `wrangler.jsonc`.
Итоговый `public/index.html` создаётся командой:

```bash
python generate_html.py
```
