import os
from pyrogram import filters, idle
from mbot import Mbot


@Mbot.on_message(filters.new_chat_members)
def kick(_,message):
   chat_id = message.chat.id
   user_id = message.from_user.id
        app.kick_chat_member(chat_id, user_id)
        app.unban_chat_member(chat_id, user_id)
        message.reply('Good Bye')
