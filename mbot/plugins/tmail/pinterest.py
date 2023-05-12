from requests import get 
from mbot import Mbot as pbot
from pyrogram import filters
from pyrogram.types import InputMediaPhoto
# credit to @NandhaBots
@pbot.on_message(filters.command("pinterest"))
async def pinterest(_, message):
     chat_id = message.chat.id
     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("Input image name for search 🔍")
     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()
     media_group = []
     count = 0
     msg = await message.reply(f"scaping images from pinterest...")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> ✅ Scaped {count}")
     try:
        
        await pbot.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()
     except Exception as e:
           await msg.delete()
           return await message.reply(f"Error\n{e}")
