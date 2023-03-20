
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

from asyncio import sleep 
from os import mkdir
from random import randint

import spotipy
from pyrogram import filters

from mbot import AUTH_CHATS, LOG_GROUP, LOGGER, Mbot
from mbot.utils.mainhelper import (
    copy,
    download_songs,
    fetch_spotify_track,
    parse_spotify_url,
    thumb_down,
)
from mbot.utils.ytdl import audio_opt, getIds, ytdl_down

client = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyClientCredentials()
)


@Mbot.on_message(filters.regex(r"https?://open.spotify.com[^\s]+")& filters.incoming | filters.regex(r"https?://open.spotify.com[^\s]+") | filters.command(["spotify", "spotdl"]) | filters.incoming & filters.regex(r"spotify:") & filters.chat(AUTH_CHATS))
async def spotify_dl(_, message):
    link = message.matches[0].group(0)
    m = await message.reply_text(f"🔎")
    try:
        parsed_item = await parse_spotify_url(link)
        item_type, item_id = parsed_item[0], parsed_item[1]
        randomdir = f"/tmp/{str(randint(1,100000000))}"
        mkdir(randomdir)
        if item_type in ["show", "episode"]:
            items = await getIds(link)
            for item in items:
                PForCopy = await message.reply_photo(
                    item[5],
                    caption=f"✔️ Episode Name : `{item[3]}`\n🕔 Duration : {item[4]//60}:{item[4]%60}",
                )
                fileLink = await ytdl_down(
                    audio_opt(randomdir, item[2]),
                    f"https://open.spotify.com/episode/{item[0]}",
                )
                thumbnail = await thumb_down(item[5], item[0])
                AForCopy = await message.reply_audio(
                    fileLink,
                    title=item[3].replace("_", " "),
                    performer="Spotify",
                    duration=int(item[4]),
                    caption=f"[{item[3]}](https://open.spotify.com/episode/{item[0]})",
                    thumb=thumbnail,
                )
                if LOG_GROUP:
                    await copy(PForCopy, AForCopy)
            return await m.delete()
        elif item_type == "track":
            song = await fetch_spotify_track(client, item_id)
            PForCopy = await message.reply_photo(photo=f"https://open.spotify.com/track/{song.get('deezer_id')}", caption=f"🎧 <b>Title:</b> `{song['name']} | {song.get('album')}`\n🎤 <b>Artist:</b> `{song['artist']}`\n💽 <b>Album:</b> `{song['album']}`\n🗓 <b>Release Year:</b> `{song['year']}`\n🔗 **Source url:** [Click here](https://open.spotify.com/track/{song.get('deezer_id')})\n**❗️Is Local**: `False`")
            path = await download_songs(song, randomdir)
            thumbnail = await thumb_down(song.get("cover"), song.get("name"))
            AForCopy = await message.reply_audio(
                path,
                performer=song.get("artist"),
                title=f"{song.get('name')} - {song.get('artist')}",
                caption=f"{song.get('name')} | @spotifysavetgbot",
                thumb=thumbnail,
            )
            if LOG_GROUP:
                await copy(PForCopy,AForCopy)
            return await m.delete()
        elif item_type == "playlist":
      #     #pForCopy = await message.reply_photo(photo="https://telegra.ph/file/477fbab1510586e2199ce.jpg", caption="🔽 SPOTIFY PLAYLIST 🔽")
            tracks = client.playlist_items(
                playlist_id=item_id, additional_types=["track"]
            )
            total_tracks = tracks.get("total")
            track_no = 1
            for track in tracks["items"]:
                song = await fetch_spotify_track(
                    client, track.get("track").get("id")
                )
                PForCopy = await message.reply_photo(song.get("cover"), caption=f"🎧 **Title:** `{song['name']} | {song.get('album')}`\n🎤 **Artist:** `{song['artist']}`\n💽 **Album:** `{song['album']}`\n🗓 **Release Year:** `{song['year']}`\n🔗 **Source url:** [Click here](https://open.spotify.com/track/{song.get('deezer_id')})\n**❗️Is Local**: `False`\n\n🔢 **Track No:** `{track_no}`\n🔢 **Total Track:** `{total_tracks}`")
                path = await download_songs(song, randomdir)
                thumbnail = await thumb_down(
                    song.get("cover"), song.get("name")
                )
                AForCopy = await message.reply_audio(
                    path,
                    performer=song.get("artist"),
                    title=f"{song.get('name')} - {song.get('artist')}",
                    caption=f"{song.get('name')} | @spotifysavetgbot",
                    thumb=thumbnail,
                )
                track_no += 1
                if LOG_GROUP:
                    await sleep(2.5)
                    await PForCopy.copy(LOG_GROUP)
                    await AForCopy.copy(LOG_GROUP)
            return await m.delete()
        elif item_type == "album":
            #pForCopy = await message.reply_photo(photo="https://telegra.ph/file/a2c32b680fc44df2244d7.jpg", caption="🔽 SPOTIFY ALBUM 🔽")
            tracks = client.album_tracks(album_id=item_id)
            for track in tracks["items"]:
                song = await fetch_spotify_track(client, track.get("id"))
                PForCopy = await message.reply_photo(song.get("cover"), caption=f"🎧 **Title:**  `{song['name']} | {song.get('album')}`\n🎤 **Artist:** `{song['artist']}`\n💽 **Album:**  `{song['album']}`\n🗓 **Release Year:** `{song['year']}`\n🔗 **Source url:** [Click here](https://open.spotify.com/track/{song.get('deezer_id')})\n❗️**Is Local:** `False`")
                path = await download_songs(song, randomdir)
                thumbnail = await thumb_down(
                    song.get("cover"), song.get("name")
                )
                AForCopy = await message.reply_audio(
                    path,
                    performer=song.get("artist"),
                    title=f"{song.get('name')} - {song.get('artist')}",
                    caption=f"<i>{song.get('name')}</i> | @spotifysavetgbot",
                    thumb=thumbnail,
                )
                if LOG_GROUP:
                    await sleep(2.5)
                    await PForCopy.copy(LOG_GROUP)
                    await AForCopy.copy(LOG_GROUP)
            return await m.delete()
    except Exception as e:
        LOGGER.error(e)
        await m.edit_text(e)
