import requests
from telethon import Button

from mbot.events import register as asau


@asau(pattern="[/!]ud")
async def ud_(e):
    try:
        text = e.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await e.reply("ɪɴᴠᴀʟɪᴅ ᴀʀɢs")
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_txt = f'<bold>{text}</bold>\n\n{results["list"][0]["definition"]}\n\n<i>{results["list"][0]["ᴇxᴀᴍᴘʟᴇ"]}</i>'
    except:
        reply_txt = "ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ."
    await e.reply(
        reply_txt,
        buttons=Button.url("🔎 ɢᴏᴏɢʟᴇ ɪᴛ!", f"https://www.google.com/search?q={text}"),
