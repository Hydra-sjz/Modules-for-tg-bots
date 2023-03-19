"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from os import mkdir
from random import randint

from deezer import Client
from pyrogram import filters
#from config import LOG_CHANNEL

from mbot import AUTH_CHATS, LOG_GROUP, Mbot
from mbot.utils.mainhelper import (
    download_songs,
    fetch_tracks,
    parse_deezer_url, 
    thumb_down,
)

client = Client()



#A = """#DEEZR_START 🟣\n🟣<b>Bot user:</b> {}\n🟣<b>User name:</b> @{}\n🟣<b>User Id:</b> <code>{}</code>\n🟣<b>Used command:</b> /start\n\n🔽<b>Started Bot</b>🔽\n@spotifysavetgbot\n@spotifysavetgbot"""


@Mbot.on_message(filters.regex(r'https?://.*deezer[^\s]+') & filters.incoming | filters.regex(r'https?://.*deezer[^\s]+') & filters.command("deezer") & filters.chat(AUTH_CHATS))
async def link_handler(_, message):
    #gg = await message.reply_text(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.username, message.from_user.id))
    link = message.matches[0].group(0)
    try:
        items = await parse_deezer_url(link)
        item_type = items[0]
        item_id = items[1]
        m = await message.reply_text("🔎")
        songs = await fetch_tracks(client, item_type, item_id)
        if item_type in ["playlist", "album", "track"]:
            randomdir = f"/tmp/{str(randint(1,100000000))}"
            mkdir(randomdir)
            for song in songs:
                PForCopy = await message.reply_photo(song.get("cover"), caption=f"🎧 <b>Title:</b> `{song['name']}`\n🎤 <b>Artist:</b> `{song['artist']}`\n💽 <b>Album:</b> `{song['album']}`\n💽 <b>Song Number:</b> `{song['playlist_num']}`")
                path = await download_songs(song, randomdir)
                thumbnail = await thumb_down(song.get("thumb"), song.get("name"))
                AForCopy = await message.reply_audio(
                    path,
                    performer=song.get("artist"),
                    title=f"{song.get('name')} - {song.get('artist')}",
                    caption=f"[{song['name']}](https://www.deezer.com/track/{song['deezer_id']}) | {song['album']} - {song['artist']}",
                    thumb=thumbnail,
                    duration=song["duration"],
                )
                if LOG_GROUP:
                    await PForCopy.copy(LOG_GROUP)
                    await AForCopy.copy(LOG_GROUP)
            await m.delete()
        elif item_type == "artist":
            await m.edit_text(
                "This Is An Artist Account Link. Send me Track, Playlist or Album Link :)"
            )
        else:
            await m.edit_text("Link Type Not Available for Download.")
    except Exception as e:
        await m.edit_text(f"Error: {e}", quote=True)
