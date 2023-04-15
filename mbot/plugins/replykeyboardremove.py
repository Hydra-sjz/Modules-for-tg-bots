from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram import Client, filters


@Client.on_message(filters.command("replyremov")) 
async def reply_rmv(client, message):
    await message.reply_text(
        text="Click Down Botton to KeyboardRemove", 
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
async def mg_myr(client, message):
    await message.reply_text(
        text="https://t.me/songdownload_group", 
    ) 

@Client.on_message(filter.reggex("❌ CLOSE ❌"))
async def close_myr(client, message):
    await message.reply_text(
        text="Botton Close", 
        reply_markup=ReplyKeyboardRemove() 
    ) 
