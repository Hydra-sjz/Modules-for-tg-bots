from pyrogram import *
from pyrogram.types import *
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from mbot import Mbot
import re
import requests
from jikanpy import Jikan
from jikanpy.exceptions import APIException

jikan = Jikan()





@Mbot.on_message(filters.command("character"))
async def character(_, msg: Message):
    res = ""
    query = msg.text.split(None, 1)[1]
    search = jikan.search("character", query).get("results")[0].get("mal_id")
    res = jikan.character(search)
    if res:
        name = res.get("name")
        kanji = res.get("name_kanji")
        about = res.get("about")
        about = re.sub(r"\\n", r"\n", about)
        about = re.sub(r"\r\n", r"", about)
        if len(about) > 4096:
            about = about[:4000] + "..."
        image = res.get("image_url")
        url = res.get("url")
        rep = f"<b>{name} ({kanji})</b>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"<i>{about}</i>"
        
        await msg.reply_text(rep,reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('View 💫' , url=f"{url}")]
    ]))
        

@Mbot.on_message(filters.command("2anime"))
async def animejrh(_, msg: Message):
    query = msg.text.split(None, 1)[1]
    res = ""
    res = jikan.search("anime", query)
    res = res.get("results")[0].get("mal_id") # Grab first result
    if res:
        anime = jikan.anime(res)
        title = anime.get("title")
        japanese = anime.get("title_japanese")
        type = anime.get("type")
        duration = anime.get("duration")
        synopsis = anime.get("synopsis")
        source = anime.get("source")
        status = anime.get("status")
        episodes = anime.get("episodes")
        score = anime.get("score")
        rating = anime.get("rating")
        genre_lst = anime.get("genres")
        genres = "".join(genre.get("name") + ", " for genre in genre_lst)
        genres = genres[:-2]
        studio_lst = anime.get("studios")
        studios = "".join(studio.get("name") + ", " for studio in studio_lst)
        studios = studios[:-2]
        duration = anime.get("duration")
        premiered = anime.get("premiered")
        image_url = anime.get("image_url")
        url = anime.get("url")
        trailer = anime.get("trailer_url")
    else:
        await msg.reply_text("No results found!")
        return
    rep = f"<b>{title} ({japanese})</b>\n"
    rep += f"<b>Type:</b> <code>{type}</code>\n"
    rep += f"<b>Source:</b> <code>{source}</code>\n"
    rep += f"<b>Status:</b> <code>{status}</code>\n"
    rep += f"<b>Genres:</b> <code>{genres}</code>\n"
    rep += f"<b>Episodes:</b> <code>{episodes}</code>\n"
    rep += f"<b>Duration:</b> <code>{duration}</code>\n"
    rep += f"<b>Score:</b> <code>{score}</code>\n"
    rep += f"<b>Studio(s):</b> <code>{studios}</code>\n"
    rep += f"<b>Premiered:</b> <code>{premiered}</code>\n"
    rep += f"<b>Rating:</b> <code>{rating}</code>\n\n"
    rep += f"<a href='{image_url}'>\u200c</a>"
    rep += f"<i>{synopsis}</i>\n"
    
    await msg.reply_text(rep)
    
    
@Mbot.on_message(filters.command("upcoming"))
async def upcomingbf(_, msg: Message):
    rep = "<b>Upcoming anime</b>\n"
    later = jikan.season_later()
    anime = later.get("anime")
    for new in anime:
        name = new.get("title")
        url = new.get("url")
        rep += f"➛ <a href='{url}'>{name}</a>\n"
        if len(rep) > 2000:
            break
    await msg.reply_text(rep)
    
@Mbot.on_message(filters.command("manga"))
async def manga(_, msg: Message):
    query = msg.text.split(None, 1)[1]
    res = ""
    manga = ""
    res = jikan.search("manga", query).get("results")[0].get("mal_id")
    if res:
        manga = jikan.manga(res)
        title = manga.get("title")
        japanese = manga.get("title_japanese")
        type = manga.get("type")
        status = manga.get("status")
        score = manga.get("score")
        volumes = manga.get("volumes")
        chapters = manga.get("chapters")
        genre_lst = manga.get("genres")
        genres = "".join(genre.get("name") + ", " for genre in genre_lst)
        genres = genres[:-2]
        synopsis = manga.get("synopsis")
        image = manga.get("image_url")
        url = manga.get("url")
        rep = f"<b>{title} ({japanese})</b>\n"
        rep += f"<b>Type:</b> <code>{type}</code>\n"
        rep += f"<b>Status:</b> <code>{status}</code>\n"
        rep += f"<b>Genres:</b> <code>{genres}</code>\n"
        rep += f"<b>Score:</b> <code>{score}</code>\n"
        rep += f"<b>Volumes:</b> <code>{volumes}</code>\n"
        rep += f"<b>Chapters:</b> <code>{chapters}</code>\n\n"
        rep += f"<a href='{image}'>\u200c</a>"
        rep += f"<i>{synopsis}</i>"
        
        await msg.reply_text(rep)

@Mbot.on_message(filters.command(["quote","animequote","quotes"]))
async def quoteif(_, message: Message):
    res = requests.get("https://animechan.vercel.app/api/random").json()
    anime = res['anime']
    character = res['character']
    quote = res['quote']

    rep = f"**Anime** - `{anime}`\n"
    rep += f"**Character** - `{character}`\n"
    rep += f"**Quote** - `{quote}`"
    
    await message.reply_text(rep)
