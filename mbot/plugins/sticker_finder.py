import os
import time
from pyrogram import Client, filters



@Client.on_message(filters.command(["findsticker"]))
async def findsticker(bot, message):  
  try:
       if message.reply_to_message.text: 
          txt = await message.reply_text("**Validating Sticker ID...**")
          stickerid = str(message.reply_to_message.text)
          chat_id = str(message.chat.id)
          await txt.delete()
          await message.reply_chat_action("choose_sticker")
          await bot.send_sticker(chat_id,f"{stickerid}")
       else:
          await message.reply_text("**__Please reply to a ID to get its STICKER.__**")
  except Exception as error:
          await message.reply_text(str(error))
