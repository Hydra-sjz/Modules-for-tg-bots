from mbot import app as tbot
from datetime import datetime
from pymongo import MongoClient
from config import DB_URL
from mbot import OWNER_ID
from telethon import events, types
import asyncio

global spamcounter
spamcounter = 0

def get_time(id):
    client = MongoClient(DB_URL)
    db = client["harita"]
    spammers = db.leecher
    return spammers.find_one({"id": id})

@tbot.on(events.NewMessage(pattern=None))
async def spammers(event):
    if str(event.sender_id) in str(OWNER_ID):
        return
    global spamcounter
    starttimer = datetime.now()
    spamcounter += 1
    sender = event.sender_id
    senderr = await event.get_sender()
    check = sender
    msg = event.text
    USERSPAM = []
    USERSPAM.append(check)
    USERSPAM.append(msg)

    for (ent, txt) in event.get_entities_text():
        if isinstance(ent, types.MessageEntityBotCommand):
            pass
        else:
            return

    if (
        spamcounter > 8
        and event.sender_id == USERSPAM[0]
        and ((datetime.now() - starttimer)).seconds <= 3
    ) or (
        spamcounter > 8 and event.sender_id == USERSPAM[0] and event.text == USERSPAM[1]
    ):
        spamcounter = 0
        if senderr.username is None:
            st = senderr.first_name
            hh = senderr.id
            final = f"[{st}](tg://user?id={hh}) you are detected as a spammer according to my algorithms.\nYou will be restricted from using any bot commands for 24 hours ! For Support join @HaritaSupport"
        else:
            st = senderr.username
            final = f"@{st} you are detected as a spammer according to my algorithms.\nYou will be restricted from using any bot commands for 24 hours !"
            pass
    else:
        return

    client = MongoClient(DB_URL)
    db = client["harita"]
    spammers = db.leecher

    users = spammers.find({})
    for c in users:
        if USERSPAM[0] == c["id"]:
            print("spammers never die")
            return
    spammers.insert_one({"id": USERSPAM[0], "time": datetime.now()})
    if event.is_group:
       msg = await event.respond(final)
       await asyncio.sleep(10)
       await msg.delete()
    else:
       await event.respond(final)

@tbot.on(events.NewMessage(pattern=None))
async def spammers(event):
    client = MongoClient(DB_URL)
    db = client["harita"]
    spammers = db.leecher
    users = spammers.find({})
    for c in users:
        if event.sender_id == c["id"]:
            to_check = get_time(id=event.sender_id)
            ttime = to_check["time"]
            if (datetime.now() - ttime).seconds > 86400:
                spammers.delete_one({"id": event.sender_id})
            else:
                return
