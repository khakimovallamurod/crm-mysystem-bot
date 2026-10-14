from html import escape

from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Ism va familiyani formatlash
    first_name = user.first_name or ""
    last_name = user.last_name or ""
    full_name = f"{first_name} {last_name}".strip() or "Foydalanuvchi"

    # Usernameni formatlash
    username = f"@{user.username}" if user.username else "Mavjud emas"

    text = (
        f"👋 Assalomu alaykum, {escape(full_name)}!\n\n"
        f"🆔 Sizning Telegram ID: <code>{chat_id}</code>\n"
        f"👤 Username: {escape(username)}\n\n"
        f"✅ Ma'lumotlaringiz muvaffaqiyatli saqlandi.\n\n"
        f"📌 Ushbu ID raqamni ustozingiz Sarimova Umidaga (@sarimova_umida) yuboring. "
        f"Shundan so'ng farzandingizning darsga qatnashishi haqidagi xabarlar shu bot orqali sizga kelib turadi.\n\n"
        f"📚 Sarimova Umida | Matematika markazi — o'quvchilar davomati va natijalarini "
        f"ota-onalarga yetkazib boruvchi tizim."
    )

    await update.message.reply_text(text, parse_mode="HTML")
