import os
import traceback
import logging

from pyrogram import Client, filters, StopPropagation

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
#from config import LOG_CHANNEL







#A = """Hi, {} with user id:- {} used /start command."""

force_subhydra = "songdownload_group"




@Client.on_message(filters.private & filters.command("st"))
async def start_command(bot, message):
    if force_subhydra:
        try:
            user = await bot.get_chat_member(force_subhydra, message.from_user.id)
            if user.status == "kick out":
                await message.reply_text("you are banned")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="🙄ʏᴏᴜʀ ɴᴏᴛ jᴏɪɴᴇᴅ ᴍʏ ɢʀᴏᴜᴘ🧐\n😿ᴘʟᴇᴀsᴇ jᴏɪɴ ᴍʏ ɢʀᴏᴜᴘ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ!😽",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🥺 Join here 🥺", url=f"t.me/{force_subhydra}")
                 ],[
                 InlineKeyboardButton("Click start Botton", url="https://t.me/spotifysavetgbot?start")
                 ]]
                )
            )
            return
    photo = f"https://telegra.ph/file/edb207dec790713be03b3.mp4" #https://telegra.ph/file/ceeca2da01f5d39550111.jpg
    await message.reply_animation(photo, reply_markup=joinButton)
    #await message.send_message(LOG_CHANNEL, A.format(bot.from_user.mention, bot.from_user.id))
    await message.reply_sticker("CAACAgUAAxkBAAIkBWQ1bqqHVW-gWo6ZI8JQ57hckzTAAALnAwACuYbZV_YX-PS370ywHgQ")
    raise StopPropagation

#=======CALLBACK==================
@Client.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.mention),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
#=======
    elif update.data == "yt":
        await update.message.edit_text(
            text=YOUTUB_TEXT,
            reply_markup=YOUTUB_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "sp":
        await update.message.edit_text(
            text=SPOTY_TEXT,
            reply_markup=SPOTY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "dz":
        await update.message.edit_text(
            text=DEEZER_TEXT,
            reply_markup=DEEZER_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "sv":
        await update.message.edit_text(
            text=SAAVN_TEXT,
            reply_markup=SAAVN_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "sc":
        await update.message.edit_text(
            text=SOUNDC_TEXT,
            reply_markup=SOUNDC_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "mx":
        await update.message.edit_text(
            text=MIXC_TEXT,
            reply_markup=MIXC_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "lg":
        await update.message.edit_text(
            text=LOGC_TEXT,
            reply_markup=LOGC_BUTTONS,
            disable_web_page_preview=True
        )
#========
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()
#=========CALLBACK========

START_TEXT = """ 
ʜᴇʟʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪs Sᴘᴏᴛɪғʏ✘Dʟ Mᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ

I ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ғʀᴏᴍ Sᴘᴏᴛɪғʏ, Dᴇᴇᴢᴇʀ, SᴏᴜɴᴅCʟᴏᴜᴅ, Mɪx Cʟᴏᴜᴅ ᴀɴᴅ Yᴏᴜᴛᴜʙᴇ Pʟᴀᴛғᴏʀᴍs.
Cʟɪᴄᴋ ʜᴇʟᴘ ғᴏʀ ᴍᴏʀᴇ ᴋɴᴏᴡ ᴍᴇ.
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ɢʀᴏᴜᴘ 📨', url='https://t.me/songdownload_group'),
        InlineKeyboardButton('ʜᴇʟᴘ 🦄', callback_data='cmds'),
        InlineKeyboardButton('ᴀʙᴏᴜᴛ 🐬', callback_data='about'), 
        InlineKeyboardButton('ᴄʜᴀɴɴᴇʟ 📨', callback_data='hhd')
        ],[
        InlineKeyboardButton('🎵ʟᴏɢ ᴄʜᴀɴɴᴇʟ🎵', url='https://t.me/music_database_tg')
        ]]
    )


CMDS_TEXT = """
ʜᴇʟʟᴏ {}
ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ᴍᴜsɪᴄ.
©️ @spotifysavetgbot
"""
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="么 sᴇᴀʀᴄʜ 么", switch_inline_query_current_chat="")
        ],[
        InlineKeyboardButton("Youtube", callback_data="yt"), 
        InlineKeyboardButton("Spotify", callback_data="sp"), 
        InlineKeyboardButton("Deezer", callback_data="dz") 
        ],[
        InlineKeyboardButton("Jio Saavn", callback_data="sv"), 
        InlineKeyboardButton("Sound Cloud", callback_data="sc"), 
        InlineKeyboardButton("Mix Cloud", callback_data="mx") 
        ],[
        InlineKeyboardButton("Log Channel", callback_data="lg") 
        ],[
        InlineKeyboardButton("«» ʜᴏᴍᴇ «»", callback_data="start"),
        InlineKeyboardButton("×««ᴄʟᴏsᴇ»»×", callback_data="close")
        ]]
    )
#=============Bottons==========
YOUTUB_TEXT = """
Send **Youtube** Link in Chat to Download Song.
"""
YOUTUB_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("«==ʙᴀᴄᴋ", callback_data="cmds"), 
        InlineKeyboardButton("«» ʜᴏᴍᴇ «»", callback_data="start")
        ]]
    ) 

SPOTY_TEXT = """
Send **Spotify** Track/Playlist/Album Link. I'll Download It For You.
"""
SPOTY_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )

DEEZER_TEXT = """
Send Deezer Playlist/Album/Track Link. I'll Download It For You.
"""
DEEZER_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )

SAAVN_TEXT = """
Send /saavn [song name] - To download song from Saavn. 
"""
SAAVN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )

SOUNDC_TEXT = """
Send **Sound Cloud** Track Link. I'll Download It For You.
"""
SOUNDC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )

MIXC_TEXT = """
Send **Mix Cloud** Track Link. I'll Download It For You.
"""
MIXC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )

LOGC_TEXT = """
My Music Database @music_database_tg
"""
LOGC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds'), 
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start')
        ]]
    )
#=================
ABOUT_TEXT = """
 **ᴀʙᴏᴜᴛ ᴍᴇ** 
➻ **ʙᴏᴛ : 𝗦ᴘᴏᴛɪғʏ•✘•Dʟ**
➻ **ᴏᴡɴᴇʀ: [X:D](t.me/Kelvin_calumbot)**
➻ **ɢʀᴏᴜᴘ : [CLICK HERE](https://t.me/songdownload_group)**
➻ **sᴏᴜʀᴄᴇ : [CLICK HERE](https://t.me/NOKIERUNNOIPPKITTUM/3)**
➻ **ʟᴀɴɢᴜᴀɢᴇ : [Python3](https://python.org)**
➻ **ʟɪʙʀᴀʀʏ : [Pyrogram](https://pyrogram.org)**
➻ **sᴇʀᴠᴇʀ : [Heroku](https://heroku.com)**
"""
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start'),
        InlineKeyboardButton('×««ᴄʟᴏsᴇ»»×', callback_data='close')
        ]]
    )

