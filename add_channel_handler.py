from telegram import Update
from telegram.ext import ContextTypes

from keyboards import start_keyboard
from link_parser import parse_channel_link
from owner import is_owner
from storage import load_channels, save_channels

WAITING_KEY = "waiting_for_channel"


async def add_channel_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not is_owner(query.from_user):
        await query.answer("Only the owner can add channels.", show_alert=True)
        return
    await query.answer()
    context.user_data[WAITING_KEY] = True
    await query.message.reply_text("Send the channel link, like https://t.me/mychannel")


async def receive_channel_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get(WAITING_KEY) or not is_owner(update.effective_user):
        return
    link = parse_channel_link(update.message.text)
    if not link:
        await update.message.reply_text("That doesn't look like a channel link. Try: https://t.me/mychannel")
        return
    channels = load_channels()
    if link not in channels:
        channels.append(link)
        save_channels(channels)
    context.user_data[WAITING_KEY] = False
    await update.message.reply_text("Channel added!", reply_markup=start_keyboard(channels))
