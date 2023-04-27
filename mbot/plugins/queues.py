import os
import requests
import pyrogram
import json
#from info import LOG_CHANNEL
from mbot import Mbot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#A = """{} with user id:- {} used /quote command."""

@Mbot.on_message(filters.command("quot"))
async def get_dquote(bot, message):
    await message.reply_chat_action("typing")
    if len(message.command) != 2:
        await message.reply_text("/quot [quote category] \n\n Like:- `/quot love`", quote=True, reply_markup=BUTTONS)
        return
    k = await message.reply_text("**Processing...⏳**", quote=True)    
    nu = message.text.split(None, 1)[1]
    URL = f'https://api.quotable.io/random?tags={nu}'
    request = requests.get(URL)
    result = request.json()
    qt = result['content']
    athr = result['author']
    tgs = result['tags']
    gett_qt = f"""**{qt}**\n                  - __{athr}__\n\nCategory:- {tgs}
\n **Powered by: @Htgtoolv4bot**"""
    await k.edit_text(
        text=gett_qt,
        disable_web_page_preview=True,
    )
    #await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id))
