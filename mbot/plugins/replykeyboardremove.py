from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram import Client, filters


@Client.on_message(filters.command("start")) 
async def start_txt(client, message):
    await message.reply_text(
        text="Hi Bro how are U", 
        reply_markup=ReplyKeyboardMarkup(
            ]]
                "♣️Music🎵Galaxy♣️" 
            ],[
                "➡️➡️➡️", "❌ CLOSE ❌", "⬅️⬅️⬅️"
            ]]
            resize_keyboard=True, 
        ) 
    ) 


@Client.on_message(filter.reggex("♣️Music🎵Galaxy♣️"))
async def start_myr(client, message):
    await message.reply_text(
        text="https://t.me/songdownload_group", 
    ) 

@Client.on_message(filter.reggex("Close ❌"))
async def close_myr(client, message):
    await message.reply_text(
        text="Botton Close", 
        reply_markup=ReplyKeyboardRemove() 
    ) 
