from pyrogram import filters
from pyrogram.types import Message

from mbot import Mbot as pgram
from mbot.utils.errors2 import capture_err


@pgram.on_message(filters.command("webss"))
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ \nʟɪᴋᴇ ||xɴxx.ᴄᴏᴍ||."
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**ᴛᴀᴋɪɴɢ sᴄʀᴇᴇɴsʜᴏᴛ**")
        await m.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ ᴍᴀʏ ʙᴇ ʏᴏᴜ ɴᴏᴛ ᴜsᴇ  𝚇.ᴄᴏᴍ.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))


__mod_name__ = "𝚆ᴇʙss"
