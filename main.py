import logging

from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters

from add_channel_handler import add_channel_button, receive_channel_link
from config import BOT_TOKEN
from start_handler import start


def main():
    if not BOT_TOKEN:
        raise SystemExit("BOT_TOKEN is not set. Add it in the environment variables.")
    logging.basicConfig(level=logging.INFO)

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(add_channel_button, pattern="^add_channel$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_channel_link))
    app.run_polling()


if __name__ == "__main__":
    main()
