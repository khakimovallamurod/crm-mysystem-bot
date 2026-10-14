import logging
from telegram import Update
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from handlers import start_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def main():
    if not BOT_TOKEN or BOT_TOKEN == "BU_YERGA_BOT_TOKEN_KIRITING":
        logger.error("BOT_TOKEN topilmadi. .env faylga tokenni kiriting.")
        return

    # Bot dasturini yaratish
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_handler))

    logger.info("Bot ishga tushdi...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
