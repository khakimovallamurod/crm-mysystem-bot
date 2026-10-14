# Sarimova Umida | Matematika markazi — Telegram Bot

O'quvchilar davomati va natijalarini ota-onalarga yetkazib boruvchi tizim uchun bot.

## Asosiy imkoniyatlar
- `/start` komandasi foydalanuvchining ism-familiyasi, Telegram ID (chat_id) va username'ini qaytaradi.
- Ota-onaga ID raqamni ustozga (@sarimova_umida) yuborish bo'yicha yo'riqnoma beradi.

## Fayllar strukturasi
- `admin-bot.py` — botni ishga tushiruvchi asosiy fayl.
- `handlers.py` — komandalarga javob qaytaruvchi funksiyalar.
- `config.py` — `.env` fayldan sozlamalarni o'qiydi.
- `.env` — maxfiy ma'lumotlar (token). Namuna: `.env.example`.
- `requirements.txt` — kerakli kutubxonalar.

## O'rnatish va ishga tushirish

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

`.env` faylida `BU_YERGA_BOT_TOKEN_KIRITING` o'rniga [@BotFather](https://t.me/BotFather) dan olingan tokenni yozing:

```
BOT_TOKEN=123456:ABC...
```

Botni ishga tushirish:

```bash
python admin-bot.py
```
