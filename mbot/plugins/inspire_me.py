import requests
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mbot import Mbot

@Mbot.on_message(filters.command("inspire"))
async def inspireme(bot, update):
    s = await update.reply_text("Processing...⏳",quote=True)
    url = "http://inspirobot.me/api?generate=true"
    get = requests.get(url)
    img = get.text
    await update.reply_photo(photo=img, caption="Inspire me again! © spoty", quote=True)
    await s.delete()
