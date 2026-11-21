from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from config import JOIN_URL


def start_keyboard(channels):
    rows = [[InlineKeyboardButton("Join", url=JOIN_URL)]]
    for link in channels:
        rows.append([InlineKeyboardButton("Join", url=link)])
    rows.append([InlineKeyboardButton("Add channel", callback_data="add_channel")])
    return InlineKeyboardMarkup(rows)
