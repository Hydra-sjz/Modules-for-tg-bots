import os
import traceback
import logging

from pyrogram import Client, filters, StopPropagation

from pyrogram import StopPropagation
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import LOG_CHANNEL, AUTH_USERS, DB_URL, DB_NAME

from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database



db = Database(DB_URL, DB_NAME)




#A = """Hi, {} with user id:- {} used /start command."""

force_subhydra = "songdownload_group"



@Client.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)

@Client.on_message(filters.private & filters.command("start"))
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
                 InlineKeyboardButton("Click start Botton", url="https://t.me/Musicx_dlbot?start")
                 ]]
                )
            )
            return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"🥳NEWUSER🥳 \n\n😼New User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) 😹started @Musicx_dlbot !!",
            )
        else:
            logging.info(f"🥳NewUser🥳 :- 😼Name : {message.from_user.first_name} 😹ID : {message.from_user.id}")
    joinButton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🥺 sᴛᴀʀᴛ ᴍᴇ ʙʀᴏ 🥺", callback_data='start')
            ]
        ]
    )
    photo = f"https://telegra.ph/file/4edfd324d1279e3999054.jpg" #https://telegra.ph/file/ceeca2da01f5d39550111.jpg
    await message.reply_photo(photo, reply_markup=joinButton)
    #await message.send_message(LOG_CHANNEL, A.format(bot.from_user.mention, bot.from_user.id))
    await message.reply_sticker("CAACAgUAAxkDAAIboWQXGQ9Ac1P4-sR4Ziseg_2nmFyPAAJICQACSkC5VIdQpmAl9rr3HgQ")
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
    elif update.data == "cmd2":
        await update.message.edit_text(
            text=CMDS_TEXT2,
            reply_markup=CMDS_BUTTONS2,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()
#=========CALLBACK========

START_TEXT = """ »━━━━━━«[𝗠ᴜsɪᴄ✘Dʟ]»━━━━━━«
ʜᴇʏ ᴛʜᴇʀᴇ {}  ɪ ᴀᴍ [˹𝗠ᴜsɪᴄ✘Dʟ˼](t.me/Musicx_dlbot) ʙᴏᴛ༒!,
➻ ᴀɴᴅ I'ᴍ ᴀ sɪᴍᴘʟᴇ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴅɪᴏ & ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ,
ᴏɴʟʏ ʜɪɢʜᴇʀ ǫᴜᴀʟɪᴛʏ ᴍᴜsɪᴄ⚝.
»━━━━━━━━━━━━━━━━━━«"
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⎆ ɢʀᴏᴜᴘ ⎆', url='https://t.me/songdownload_group'),
        InlineKeyboardButton('⎆ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ⎆', url='https://t.me/music_database_tg')
        ],[
        InlineKeyboardButton('⨳ ʜᴇʟᴘ ⨳', callback_data ='cmds'),
        InlineKeyboardButton('瓮 ᴀʙᴏᴜᴛ 瓮', callback_data='about')
        ],[
        InlineKeyboardButton('×««ᴄʟᴏsᴇ»»×', callback_data='close')
        ]]
    )


CMDS_TEXT = """
ʜᴇʟʟᴏ {}

"""
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start'),
        InlineKeyboardButton('×««ᴄʟᴏsᴇ»»×', callback_data='close')
        ]]
    )

CMDS_TEXT2 = """
**Welcome to help commands two.**
**Sticker tool**
sticker to image - send sticker to make image.
image to sticker - send image to make sticker.
"""

CMDS_BUTTONS2 = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('«==ʙᴀᴄᴋ', callback_data='cmds')
        ],[
        InlineKeyboardButton('«» ʜᴏᴍᴇ «»', callback_data='start'),
        InlineKeyboardButton('×««ᴄʟᴏsᴇ»»×', callback_data='close')
        ]]
    )

ABOUT_TEXT = """
 **ᴀʙᴏᴜᴛ ᴍᴇ** 
➻ **ʙᴏᴛ : 𝗠ᴜsɪᴄ✘Dʟ**
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

#==================•BROADCAST•==================
@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)

@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        quote=True
    )

@Client.on_message(filters.private & filters.command("ban_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban 🛑 any user from the bot 🤖.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."

        try:
            await c.send_message(
                user_id,
                f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**",
            )
            ban_log_text += "\n\nUser notified successfully!"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )

@Client.on_message(filters.private & filters.command("unban_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban 😃 any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )

@Client.on_message(filters.private & filters.command("banned_users"))
async def _banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"> **User_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, **Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)
