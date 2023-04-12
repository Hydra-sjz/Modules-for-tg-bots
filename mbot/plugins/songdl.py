
from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

#from pyrogram.enums import ChatType


ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True, 
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))



@Client.on_message(filters.command(["song@spotifysavetgbot", "song", "mp3", "mp3@spotifysavetgbot", "s"]))
def song_gtr(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("🔎")
    n = await message.reply_chat_action(enums.ChatAction.TYPING)
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        views = results[0]["views"]
        performer = f"[ᴍᴜsɪᴄ ɢᴀʟᴀxʏ]"
        channel = results[0]["channel"]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        if time_to_seconds(duration) >= 1000:  # duration limit
            m.edit(f"**Duration Limit Exceeded:**\n\n**Allowed Duration:** 10 minute(s)\n**Received Duration:** {duration} hour(s)\nSend songs less than 10 minutes")
            return

    except Exception as e:
        m.edit(f"Nothing Found {message.from_user.first_name} :(\n\nPlease check, you using correct format or your spellings are correct and try again.\n Correct Format : /song song_name or /s song_name")
        print(str(e))
        return
    m.edit("🔽 Downloading Audio...") 
    dForChat = await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)

    PForCopy = message.reply_photo(photo=f"{link}.jpg", caption=f"🎧<b>Title:</b> <code>{title}</code>\n🎤<b>Artist:</b> <code>{channel}</code>\n<b>⏱️Duration:</b> <code>{duration}</code>\n🔗<b>Song link:</b> [Click here]({link})")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"<i>{title} - {channel}</i>"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("🔼 Uploading to Telegram...\n<i>(this may take a while.)</i>") 
        dForChat = await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)
        AForCopy = message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            performer=performer,
            title=title,
            duration=dur,
        )

        message.reply_text(f"Done✅",   
          reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Done ✅", callback_data="feed")
          ]]
          )
      )
        if LOG_GROUP:
            PForCopy.copy(LOG_GROUP)
            AForCopy.copy(LOG_GROUP)
       
        m.delete()
    except Exception as e:
        m.edit("#ERROR")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
