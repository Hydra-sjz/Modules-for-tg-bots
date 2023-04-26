from pyrogram import filters
from pyrogram.types import Message
from mbot import Mbot
from mbot.utils import commands, http


@Mbot.on_message(filters.command("dog")) 
async def dog(c: Client, m: Message, strings):
    r = await http.get("https://random.dog/woof.json")
    rj = r.json()

    await m.reply_photo(rj["url"], caption=strings("woof"))


commands.add_command("dog", "general")
