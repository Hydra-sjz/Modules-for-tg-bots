from pyrogram.types import Message
from pyrogram import filters, Client
import random
import requests 
        
        
@Client.on_message(filters.group & filters.regex('good morning') | filters.group & filters.regex('Good morning'))
def gm(_, m: Message):
    reply = m.reply_to_message
    if reply:
        m.reply(f"good morning! {reply.from_user.mention}")
    else:
        m.reply(f"good morning! {m.from_user.mention}")
 

@Client.on_message(filters.group & filters.regex('good night') | filters.group & filters.regex('Good night'))
def goodnight(_, n: Message):
    reply = n.reply_to_message
    if reply:
        n.reply(f"good night! {reply.from_user.mention}")
    else:
        n.reply(f"good night! {n.from_user.mention}")
