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
        msg = await message.reply_text(f"🔑 <code>{bot_token}</code>\n\nCopiando meu system...")
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
            await msg.edit_text(f"✅ O bot @{bot.username} agora está trabalhando como Gerenciador de chat! Está funcionando como eu, meu parceiro.\n\n⚠️ <u>NÃO envie para ninguém</u> a mensagem com <u>o token</u> do Bot, quem o tem pode controlar o seu Bot!\n<i>Se você acha que alguém descobriu sobre o seu token Bot, vá para @Botfather, use /revoke e, em seguida, selecione @{bot.username}</i>")
        except BaseException as e:
            await msg.edit_text(f"⚠️ <b>BOT ERROR:</b>\n\n<code>{e}</code>\n\n❔ Encaminhar esta mensagem para @The_Panda_Official corrigir.")
