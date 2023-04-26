import random

from pyrogram import Client, filters
from pyrogram.types import Message
from mbot import Mbot
from mbot.utils import commands, http



@Mbot.on_message(filters.command("coub"))
async def coub(c: Client, m: Message, strings):
    if len(m.command) == 1:
        return await m.reply_text(strings("string_coub_usage"))
    text = m.text.split(maxsplit=1)[1]
    r = await http.get("https://coub.com/api/v2/search/coubs", params=dict(q=text))
    rjson = r.json()
    try:
        content = random.choice(rjson["coubs"])
        links = content["permalink"]
        title = content["title"]
    except IndexError:
        await m.reply_text(strings("no_results", context="general"))
    else:
        await m.reply_text(f'<b><a href="https://coub.com/v/{links}">{title}</a></b>')

commands.add_command("coub", "general")
