from telegram import Update
from telegram.ext import ContextTypes

from image_maker import make_congrats_image
from keyboards import start_keyboard
from storage import load_channels


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=make_congrats_image(),
        caption="Good job! 🎉 Your bot is active.",
        reply_markup=start_keyboard(load_channels()),
    )
