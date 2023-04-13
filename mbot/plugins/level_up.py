from pyrogram import filters
from pymongo import MongoClient
import os
from config import DB_URL

from mbot import Mbot
#Client

Chat_Group = [-1001671054664]





levellink =["https://telegra.ph/file/b507aa1334caacbbbf3b5.mp4", "https://telegra.ph/file/028fb314488a82422d85d.mp4", "https://telegra.ph/file/cca115d41d2c90edaa0be.mp4", "https://telegra.ph/file/a74c0dfc2fd656cf11c64.mp4", "https://telegra.ph/file/81e09bea9b389166f5a70.mp4", "https://telegra.ph/file/afd7ad7349c5382e206f4.mp4", "https://telegra.ph/file/8713be38beb9e1d3a2969.mp4", "https://telegra.ph/file/86ffec208e702d7634506.mp4"]
levelname = ["Team ACE", "Stray God", "Vector", "Hero Association", "Z Warrior", "Black Knight", "Ghoul", "Overlord"]
levelnum = [2,5,15,25,35,50,70,100]




@Mbot.on_message(
    (filters.document
     | filters.text
     | filters.photo
     | filters.sticker
     | filters.animation
     | filters.audio)
    & ~filters.private,
    group=8,
)
async def level(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    

    leveldb = MongoClient(DB_URL)
    
    level = leveldb["LevelDb"]["Level"] 
 
    if message.chat.id in Chat_Group:
        xpnum = level.find_one({"level": user_id})

        if not message.from_user.is_bot:
            if xpnum is None:
                newxp = {"level": user_id, "xp": 10}
                level.insert_one(newxp)   
                    
            else:
                xp = xpnum["xp"] + 10
                level.update_one({"level": user_id}, {
                    "$set": {"xp": xp}})
                l = 0
                while True:
                    if xp < ((50*(l**2))+(50*(l))):
                         break
                    l += 1
                xp -= ((50*((l-1)**2))+(50*(l-1)))
                if xp == 0:
                    await message.reply_text(f"🎉 **GG {message.from_user.mention}**, `you just advanced to level` **{l}!**")
    
                    for lv in range(len(levelname)) and range(len(levellink)):
                            if l == levelnum[lv]:            
                                Link = f"{levellink[lv]}"
                                await message.reply_video(video=Link, caption=f"{message.from_user.mention}, You have reached Rank Name **{levelname[lv]}**")
                  

                               
@Mbot.on_message(
    filters.command("rank", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rank(client, message):
    chat = message.chat.id
    user_id = message.from_user.id    
    
    leveldb = MongoClient(DB_URL)
    
    level = leveldb["LevelDb"]["Level"] 
    
    if message.chat.id in Chat_Group:
        xpnum = level.find_one({"level": user_id})
        xp = xpnum["xp"]
        l = 0
        r = 0
        while True:
            if xp < ((50*(l**2))+(50*(l))):
                break
            l += 1

        xp -= ((50*((l-1)**2))+(50*(l-1)))
        rank = level.find().sort("xp", -1)
        for k in rank:
            r += 1
            if xpnum["level"] == k["level"]:
                break                     
        await message.reply_animation(animation="https://telegra.ph/file/3534a982396187925d294.mp4", caption=f"🔰<b>LEVEL INFO🔰</b>\n\n🙋‍♂️ <b>User:</b> {message.from_user.mention} \n🎖 <b>Level:</b> <code>{l}</code>\n⏳ <b>Progess:</b> <code>{xp}/{int(200 *((1/2) * l))}</code>\n🏆 <b>Ranking:</b> <code>{r}</code>")
