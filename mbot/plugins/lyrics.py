import os
from pyrogram import Client, filters
import lyricsgenius
from pyrogram.types import Message, User
import requests




#  Lyrics--------------------
@Client.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):  
    m = await message.reply_text("🔎")
    query = query = message.text.split(None, 1)[1]
    x = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lʏʀɪᴄs ɴᴏᴛ ғᴏᴜɴᴅ...")
        
    xxx = f"""
🔎 **Searched Song:** __{query}__
🎶 **Found Lyrics For:** __{S.title}__
👨‍🎤 **Artist:** {S.artist}
💋 **Requested by:** {message.from_user.mention}

**Lyrics:**
`{S.lyrics}`

©️ **Lyrics Search Powered By @Spotifyx_dlbot**"""
    await m.edit(xxx)
