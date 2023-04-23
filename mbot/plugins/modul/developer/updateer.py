import os
import sys

from pyrogram import filters
from pyrogram.types import Message

from mbot.helpers.decorators import ratelimiter
from mbot.helpers.filters import dev_cmd
from mbot.logging import LOG
from mbot import Mbot

@Mbot.on_message(filters.command("update") & dev_cmd)
@ratelimiter
async def update(_, message: Message):
    """
    Update the bot with the latest commit changes from GitHub.
    """

    msg = await message.reply_text("Pulling changes with latest commits...", quote=True)
    os.system("git pull")
    LOG(__name__).info("Bot Updated with latest commits. Restarting now..")
    await msg.edit("Changes pulled with latest commits. Restarting bot now... ")
    os.execl(sys.executable, sys.executable, "-m", "TelegramBot")


@Mbot.on_message(filters.command("restart") & dev_cmd)
@ratelimiter
async def restart(_, message: Message):
    """
    Just Restart the bot and update the bot with local changes.
    """

    LOG(__name__).info("Restarting the bot. shutting down this instance")
    await message.reply_text(
        "Starting a new instance and shutting down this one...", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "TelegramBot")
