import aiohttp
from pyrogram import Client, filters


__mod_name__ = "Github"


@Client.on_message(filters.private & filters.command("github"))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("Wrong santex 🚫\nExample:\n/github Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""**Info Of {name}**
**👨‍💼 ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
**✍️ ʙɪᴏ:** `{bio}`
**🔗 ᴘʀᴏғɪʟᴇ ʟɪɴᴋ:** [Here]({url})
**🏢 ᴄᴏᴍᴘᴀɴʏ:** `{company}`
**📒 ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created_at}`
**⛵️ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs:** `{repositories}`
**🧖 ʙʟᴏɢ:** `{blog}`
**📍 ʟᴏᴄᴀᴛɪᴏɴ:** `{location}`
**➡️ ғᴏʟʟᴏᴡᴇʀs:** `{followers}`
**⬅️ ғᴏʟʟᴏᴡɪɴɢ:** `{following}`
**ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** @Htgtoolv4bot"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)
