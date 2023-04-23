from time import time 
from httpx import AsyncClient
from datetime import datetime

from pyrogram.types import Message
from pyrogram import filters 

from mbot import BotStartTime
from mbot.helpers.decorators import ratelimiter
from mbot.helpers.functions import get_readable_time
from mbot import Mbot

@Mbot.on_message(filters.command(["ping", "alive"]))
@ratelimiter
async def ping(_, message: Message):
    """
    Give ping speed of Telegram API along with Bot Uptime.
    """
    
    pong_reply = await message.reply_text("pong!", quote=True)
    
    start = datetime.now()
    async with AsyncClient() as client:
        await client.get("http://api.telegram.org")
    end = datetime.now()
    
    botuptime = get_readable_time(time() - BotStartTime)
    pong = (end - start).microseconds / 1000
    return await pong_reply.edit(
        f"**Ping Time:** `{pong}`ms | **Bot is alive since:** `{botuptime}`")