### This download from saavn.me an unofficial api
from pyrogram import Client, filters, enums
import requests,os,wget 

from mbot import LOG_GROUP, Mbot


@Mbot.on_message(filters.command("saavn", "saavn@spotifysavetgbot")) #filters.text
async def saavn_song(client, message):
    await message.reply_chat_action(enums.ChatAction.TYPING)
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply(f"Nothing found {message.from_user.first_name} 🙂\neg: <code>/saavn thum hi ho</code>\n/saavn [get saavn song here].")
    if args.startswith(" "):
        await message.reply(f"Nothing found {message.from_user.first_name} 🙂\neg: <code>/saavn thum hi ho</code>\n/saavn [get saavn song here].")
        return ""
    pak = await message.reply('» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ\nsᴏɴɢ ғʀᴏᴍ sᴀᴀᴠɴ...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
    #album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)
    await pak.edit('» ᴜᴘʟᴏᴀᴅɪɴɢ\nsᴏɴɢ ғʀᴏᴍ sᴀᴀᴠɴ...')
    PForCopy = await message.reply_photo(photo=f"{thumbnail}", caption=f"🎧<b>Title:</b> <code>{sname}</code>\n<b>👨‍🎤 Singers:</b> <code>{ssingers}</code>\n🔗<b>Source Link:</b> [Click here]({r['data']['results'][0]['url']})\n❗️<b>Is Local:</b> <code>False</code>") #\n<b>Album:</b> <code>{album_id}</code>    
    AForCopy = await message.reply_audio(audio=ffile, title=sname, performer=ssingers, caption=f"<i>[song.link]({r['data']['results'][0]['url']}) | [via](https://telegram.me/Musicx_dlbot?start=abcde)</i>", thumb=thumbnail) #caption=f"[{sname}]() - from saavn
    await message.reply_text("Done ✅") 
     
    if LOG_GROUP:
        await PForCopy.copy(LOG_GROUP)
        await AForCopy.copy(LOG_GROUP)
   
    #await bot.send_audio(chat_id=BOT_CHAT_ID, audio=open(AForCopy, 'rb'))



    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()
