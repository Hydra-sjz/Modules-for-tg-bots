import re

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid

from mbot import API_ID, API_HASH, log_chat


@Client.on_message((filters.regex(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}')) & filters.private)
async def on_clone(self, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', message.text, re.IGNORECASE)
    bot_token = bot_token[0] if bot_token else None
    bot_id = re.findall(r'\d[0-9]{8,10}', message.text)

    if not str(message.forward_from.id) != "93372553":
        msg = await message.reply_text(f"🔑 <code>{bot_token}</code>\n\ncopying my system...")
        try:
            ai = Client(
                f"{bot_token}", API_ID, API_HASH,
                bot_token=bot_token,
                plugins={"root": "eduu.plugins"},
            )
            await ai.start()
            bot = await ai.get_me()
            details = {
                'bot_id': bot.id,
                'is_bot': True,
                'user_id': user_id,
                'name': bot.first_name,
                'token': bot_token,
                'username': bot.username
            }
            await msg.edit_text(f"✅ Bot @{bot.username} is now working as a Chat Manager! It's working like me, my partner.\n\n⚠️ <u>DO NOT send to anyone</u> the message with the <u>Bot token</u>, whoever has it can control your Bot!\n <i>If you think someone found out about your Bot token, go to @Botfather , use /revoke , then select @{bot.username}</i>")
        except BaseException as e:
            await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\nForward this message to correct.")
