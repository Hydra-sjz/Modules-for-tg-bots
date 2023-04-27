from pyrogram import Client, filters
from database.kitsu_api import kitsu_get_title, kitsu_get_anime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["kitsu"]))
async def search_anime_kitsu(bot, update):
    try:
        if update.reply_to_message:
            name = update.reply_to_message.text
        else:
            name = update.text.split(" ", maxsplit=1)[1]
    except:
        name = None
    if name:
        await bot.send_message(
                chat_id=update.chat.id,
                text=f"Searching for: <code>{name}</code>",
                reply_to_message_id=update.message_id
            )
        titles, aids = await kitsu_get_title(name)
        if titles:
            inline_keyboard = []
            for aid in aids:
                inline_keyboard.append([InlineKeyboardButton(text=titles[aids.index(aid)], callback_data=f"k_{aid}")])
            inline_keyboard.append([InlineKeyboardButton(text="Close",callback_data="close")])
            await bot.send_message(
                chat_id=update.chat.id,
                text="<b>Select Anime to fetch details</b>",
                reply_markup=InlineKeyboardMarkup(inline_keyboard),
                reply_to_message_id=update.message.id
            ) 

@Client.on_callback_query(filters.regex("k_"))
async def get_anime_kitsu_cb(c: Client, cb: CallbackQuery):
    a_id = cb.data.split("_")[1]
    photo, msg = await kitsu_get_anime(a_id)
    if msg:
        await c.delete_messages(chat_id=cb.message.chat.id, message_ids=[cb.message.message_id])
        await c.send_photo(
            chat_id=cb.message.chat.id,
            photo=photo,
            caption=msg,
            reply_to_message_id=cb.message.reply_to_message.message.id
        ) 
