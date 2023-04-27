# myanilist api
from pyrogram import Client, filters
from database.mal_api import get_anime_list, get_anime_by_id
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["search_anime"]))
async def search_anime_mal(bot, update):
    try:
        name = update.text.split(" ", maxsplit=1)[1]
    except:
        name = None
    if name:
        titles, id_list = await get_anime_list(name)
        if titles:
            msg = ""
            for id in id_list:
                name = titles[id_list.index(id)]
                msg += f"<b>Title :</b> {name}\n<b>ID :</b> {id}\n\n"
                
            await bot.send_message(
                    chat_id=update.chat.id,
                    text=msg,
                    reply_to_message_id=update.message_id
                )

@Client.on_message(filters.command(["get_anime"]))
async def get_anime_mal(bot, update):
    try:
        a_id = update.text.split(" ", maxsplit=1)[1]
    except:
        a_id = None
    if a_id:
        photo, msg, trailer = await get_anime_by_id(a_id)
        if msg:
            inline_keyboard = [] 
            if trailer:
                inline_keyboard.append([InlineKeyboardButton(text="Trailer", url=trailer)])
            inline_keyboard.append([InlineKeyboardButton(text="Close",callback_data="close")])
            await bot.send_photo(
                chat_id=update.chat.id,
                photo=photo,
                caption=msg,
                reply_markup=InlineKeyboardMarkup(inline_keyboard),
                reply_to_message_id=update.message_id
            )
