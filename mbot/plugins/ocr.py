import os
from pyrogram import filters, Client
from pyrogram.types import Message
from telegraph.aio import Telegraph

from mbot import Mbot as app
from mbot.utils2.ratelimiter import ratelimiter
from mbot.utils.errors import capture_err
#from misskaty.helper.localization import use_chat_lang
from mbot.helper.http import http
#from misskaty.vars import COMMAND_HANDLER
__MODULE__ = "OCR"
__HELP__ = "/ocr [reply to photo] - Read Text From Image"
@app.on_message(filters.command(["ocr"]))
@capture_err
@ratelimiter
async def ocr(self: Client, ctx: Message, strings):
    reply = ctx.reply_to_message
    if not reply or not reply.photo or not (reply.document and reply.document.mime_type.startswith("image")) or not reply.sticker:
        return await ctx.reply_msg(("Reply photo with /ocr command to scan text from images.").format(cmd=ctx.command[0]), quote=True, del_in=6)
    msg = await ctx.reply_msg(("Scanning your images.."), quote=True)
    try:
        file_path = await reply.download()
        if reply.sticker:
            file_path = await reply.download(f"ocr_{ctx.from_user.id if ctx.from_user else ctx.sender_chat.id}.jpg")
        response = await Telegraph().upload_file(file_path)
        url = f"https://telegra.ph{response[0]['src']}"
        req = (
            await http.get(
                f"https://script.google.com/macros/s/AKfycbwURISN0wjazeJTMHTPAtxkrZTWTpsWIef5kxqVGoXqnrzdLdIQIfLO7jsR5OQ5GO16/exec?url={url}",
                follow_redirects=True,
            )
        ).json()
        await msg.edit_msg((f"Hasil OCR:\n<code>{result}</code>").format(result=req["text"]))
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        await msg.edit_msg(str(e))
        if os.path.exists(file_path):
            os.remove(file_path)
