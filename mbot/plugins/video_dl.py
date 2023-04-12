from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from database.decorators import humanbytes
#from database.filters import command, other_filters

from mbot import LOG_GROUP



# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


#filters.group & 
@Client.on_message(filters.command(["mp4", "mp4@spotifysavetgbot", "video", "video@spotifysavetgbot", "v"]))
async def vsong(client, message):
    ydl_opts = {
        "format": "best", 
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    msg = await message.reply("🔎")
    n = await message.reply_chat_action(enums.ChatAction.TYPING)
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("🔽 Downloading video...")
        m = await message.reply_chat_action(enums.ChatAction.RECORD_AUDIO)
        mfd = await message.reply_text(f"🎧 {title}\n🔗{link}")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"#ERROR:\n {e}")
    preview = wget.download(thumbnail)
    await msg.edit("🔼 Uploading video...\n<i>(this may take a while.)</i>")
    await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)
    PForCopy = await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    if LOG_GROUP:
        await PForCopy.copy(LOG_GROUP)

    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)
