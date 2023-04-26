from pyrogram import filters
from pyrogram.types import Message
from mbot import Mbot
from mbot.utils import commands, http


@Mbot.on_message(filters.command("cat"))
async def cat(c: Client, m: Message, strings):
    r = await http.get("https://api.thecatapi.com/v1/images/search")
    rj = r.json()

    if rj[0]["url"].endswith(".gif"):
        await m.reply_animation(rj[0]["url"], caption=strings("meow"))
    else:
        await m.reply_photo(rj[0]["url"], caption=strings("meow"))

commands.add_command("cat", "general")
