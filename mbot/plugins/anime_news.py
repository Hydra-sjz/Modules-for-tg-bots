from pyrogram import filters
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
from mbot import Mbot as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.private & filters.command("animenews")) 
async def animenews(_, message): 

    new_page = urlopen("https://myanimelist.net/news")
    soup = BeautifulSoup(new_page, "html.parser")

    AnimeNews = soup.findAll(
        "div", {"class": "news-unit clearfix rect"}
    )

    title, image, description, newlink = [], [], [], []

    for x in AnimeNews:

        text = x.findChildren("p")[0]
        a = text.find("a", href=True)
        text = a.get_text()

        newslinkx = a["href"]

        images = x.find("img")
        imagex = images["src"]

        descriptionx = x.findChildren("div", {"class": "text"})[0]

        title.append(text)
        image.append(imagex)      
        description.append(" ".join(descriptionx.text.split()))
        newlink.append(newslinkx)

    description = description
    title = title
    buttons = [[
        InlineKeyboardButton("Read More", url=f"{newlink[0]}")
    ]]

    photo = f"{image[0]}"
    
    await message.reply_photo(photo=photo, caption=f"**Title:** {title[0]}\n**Description:** {description[0]}", reply_markup=InlineKeyboardMarkup(buttons))

