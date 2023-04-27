import requests
import nekos
from PIL import Image
import os

from pyrogram import filters, Client
from pyrogram.types import Message

    

@Client.on_message(filters.command("wallpaper"))
def wallpaper(_,  m: Message):
    target = "wallpaper"
    m.reply_photo(nekos.img(target))


@Client.on_message(filters.command("ngif"))
def ngif(_,  m: Message):
    target = "ngif"
    m.reply_video(nekos.img(target))


@Client.on_message(filters.command("gasm"))
def gasm(_,  m: Message):
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    m.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


@Client.on_message(filters.command("foxgirl"))
def foxgirl(_,  m: Message):
    target = "fox_girl"
    m.reply_photo(nekos.img(target))


@Client.on_message(filters.command("8ball"))
def baka(_,  m: Message):
    target = "8ball"
    m.reply_photo(nekos.img(target))
