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

from datetime import datetime
from os import execvp, sys

from pyrogram import filters
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from mbot import AUTH_CHATS, OWNER_ID, SUDO_USERS, Mbot


@Mbot.on_message(filters.private & filters.command("st"))
async def start(client, message):
    reply_markup = [
        [
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ 📨", callback_data="http"
            ),
            InlineKeyboardButton(
                text="ʜᴇʟᴘ 🦄", callback_data="helphome"
            ),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ 📨", url="https://t.me/songdownload_group"),
        ],
        [
            InlineKeyboardButton(
                text="🎵ʟᴏɢ ᴄʜᴀɴɴᴇʟ🎵", url="https://t.me/music_database_tg",
            ),
        ],
    ]
        
  
    if (
        message.chat.type != "private"
        and message.chat.id not in AUTH_CHATS
        and message.from_user.id not in SUDO_USERS
    ):
        return await message.reply_text(
            "This Bot Will Not Work In Groups Unless It's Authorized.",
            reply_markup=InlineKeyboardMarkup(reply_markup),
        )
    return await message.reply_text(
        f"ʜᴇʟʟᴏ {message.from_user.first_name},\nᴍʏ ɴᴀᴍᴇ ɪs <b>Sᴘᴏᴛɪғʏ✘Dʟ</b> Mᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ.\n\nI ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ғʀᴏᴍ Sᴘᴏᴛɪғʏ, Dᴇᴇᴢᴇʀ, SᴏᴜɴᴅCʟᴏᴜᴅ, Mɪx Cʟᴏᴜᴅ ᴀɴᴅ Yᴏᴜᴛᴜʙᴇ Pʟᴀᴛғᴏʀᴍs.\n\nCʟɪᴄᴋ ʜᴇʟᴘ ғᴏʀ ᴍᴏʀᴇ ᴋɴᴏᴡ ᴍᴇ.",
        reply_markup=InlineKeyboardMarkup(reply_markup),
    )


@Mbot.on_message(
    filters.command("restart") & filters.chat(OWNER_ID) & filters.private
)
async def restart(_, message):
    await message.delete()
    execvp(sys.executable, [sys.executable, "-m", "mbot"])


@Mbot.on_message(filters.command("log") & filters.chat(SUDO_USERS))
async def send_log(_, message):
    await message.reply_document("bot.log")


@Mbot.on_message(filters.command("p"))
async def pijsh(client, message):
    start = datetime.now()
    await client.send(Ping(ping_id=0))
    ms = (datetime.now() - start).microseconds / 1000
    await message.reply_text(f"**Pong!**\nResponse time: `{ms} ms`")


HELP = {
    "ʏᴏᴜᴛᴜʙᴇ": "Send **Youtube** Link in Chat to Download Song.",
    "sᴘᴏᴛɪғʏ": "Send **Spotify** Track/Playlist/Album Link. I'll Download It For You.",
    "ᴅᴇᴇᴢᴇʀ": "Send Deezer Playlist/Album/Track Link. I'll Download It For You.",
    "ᴍɪx ᴄʟᴏᴜᴅ": "Send **Mix Cloud** Track Link. I'll Download It For You.",
    "sᴏᴜɴᴅ ᴄʟᴏᴜᴅ": "Send **Sound Cloud** Track Link. I'll Download It For You.",
    "sᴀᴀᴠɴ": "Send /saavn [song name] - To download song from Saavn.", 
    "ʟᴏɢ ᴄʜᴀɴɴᴇʟ": "My Music Database @music_database_tg",
}


@Mbot.on_message(filters.command("hp"))
async def help(_, message):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]

    await message.reply_text(
        f"Hello **{message.from_user.first_name}**,\nI'm Here to download your music.",
        reply_markup=InlineKeyboardMarkup(button),
    )


@Mbot.on_callback_query(filters.regex(r"help_(.*?)"))
async def helpbtn(_, query):
    i = query.data.replace("help_", "")
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Back", callback_data="helphome")]]
    )
    text = f"Help for **{i}**\n\n{HELP[i]}"
    await query.message.edit(text=text, reply_markup=button)


@Mbot.on_callback_query(filters.regex(r"helphome"))
async def help_home(_, query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    await query.message.edit(
        f"Hello **{query.from_user.first_name}**,\nI'm Here to download your music.",
        reply_markup=InlineKeyboardMarkup(button),
    )
