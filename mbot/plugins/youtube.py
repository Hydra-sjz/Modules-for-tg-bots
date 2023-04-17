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

from pyrogram import filters, enums

from mbot import AUTH_CHATS, LOG_GROUP, LOGGER, Mbot
from mbot.utils.ytdl import audio_opt, getIds, thumb_down, ytdl_down



@Mbot.on_message(filters.regex(r'(https?://)?.*you[^\s]+') & filters.incoming | filters.command(["yt","ytd","ytmusic"]) & filters.regex(r'https?://.*you[^\s]+') & filters.chat(AUTH_CHATS))
async def _(_, message):
    m = await message.reply_text("🔎")
    n = await message.reply_chat_action(enums.ChatAction.TYPING)
    link = message.matches[0].group(0)
    if link in [
        "https://youtube.com/",
        "https://youtube.com",
        "https://youtu.be/",
        "https://youtu.be",
    ]:
        return await m.edit_text("Please send a valid playlist or video link.")
    elif "channel" in link or "/c/" in link:
        return await m.edit_text("**Channel** Download Not Available. ")
    try:
        ids = await getIds(message.matches[0].group(0))
        videoInPlaylist = len(ids)
        randomdir = "/tmp/" + str(randint(1, 100000000))
        mkdir(randomdir)
        for id in ids:
            PForCopy = await message.reply_photo(
                f"https://i.ytimg.com/vi/{id[0]}/hqdefault.jpg",
                caption=f"🎧 **Title** : `{id[3]}`\n🎤 **Artist** : `{id[2]}`\n🔗 **Link** : [Click here](https://youtu.be/{id[0]})\n\n💽 **Track No** : `{id[1]}`\n💽 **Total Track** : `{videoInPlaylist}`",
            )
            fileLink = await ytdl_down(audio_opt(randomdir, id[2]), id[0])
            thumnail = await thumb_down(id[0])
            dForChat = await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)
            AForCopy = await message.reply_audio(
                fileLink,
                caption=f"<i>{id[3]} | @Spotifyx_dlbot</i>",
                title=id[3].replace("_", " "),
                performer=id[2],
                thumb=thumnail,
                duration=id[4],
            )
            if LOG_GROUP:
                await PForCopy.copy(LOG_GROUP)
                await AForCopy.copy(LOG_GROUP)
        await m.delete()
    except Exception as e:
        LOGGER.error(e)
        await m.edit_text(e)
