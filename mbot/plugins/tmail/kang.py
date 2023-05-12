"""
MIT License
Copyright (c) 2023 Arsh
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import random
import emoji
from motor import motor_asyncio
from telethon import Button, TelegramClient, events
from telethon.errors.rpcerrorlist import PackShortNameOccupiedError
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.stickers import CreateStickerSetRequest
from telethon.tl.types import DocumentAttributeSticker, InputDocument, InputStickerSetEmpty, InputStickerSetID, InputStickerSetItem
from mbot import bot as telethn
from config import DB_URL

# variables


BOT_USERNAME = "@Spotifyx_dlbot"
# telethon library
# connecting to mongodb
mongo = motor_asyncio.AsyncIOMotorClient(DB_URL)
db = mongo["Emilia"]
pkang = db.pack_kang
def get_emoji(v):
    p = "".join(c for c in v if c in emoji.UNICODE_EMOJI["en"])
    if len(p) != 0:
        return p[0]
    return None
@telethn.on(events.NewMessage(pattern=f"^/(pkang|packkang)(@{BOT_USERNAME})? ?(.*)"))
async def pck_kang__(e):
    if not e.reply_to:
        return await e.reply("Reply to a sticker.")
    r = await e.get_reply_message()
    if not r.sticker:
        return await e.reply("That's not a sticker file.")
    if len(e.text.split(" ", 1)) == 2:
        pname = e.text.split(" ", 1)[1]
        emoji = get_emoji(pname)
        if emoji:
            if pname.startswith(emoji):
                emoji = None
            else:
                pname = pname.replace(emoji, "")
    else:
        pname = f"{e.sender.first_name}'s pKang pack"
        emoji = None
    id = access_hash = None
    for x in r.sticker.attributes:
        if isinstance(x, DocumentAttributeSticker):
            if not isinstance(x.stickerset, InputStickerSetEmpty):
                id = x.stickerset.id
                access_hash = x.stickerset.access_hash
    if not (id or access_hash):
        return await e.reply("That sticker is not part of any pack to kang!")
    _stickers = await telethn(GetStickerSetRequest(stickerset=InputStickerSetID(id=id, access_hash=access_hash), hash=0))
    stk = []
    if emoji:
        for x in _stickers.documents:
            stk.append(InputStickerSetItem(document=InputDocument(id=x.id, access_hash=x.access_hash, file_reference=x.file_reference), emoji=emoji))
    else:
        for x in _stickers.documents:
            stk.append(InputStickerSetItem(document=InputDocument(id=x.id, access_hash=x.access_hash, file_reference=x.file_reference), emoji=(x.attributes[1]).alt))
    pack = 1
    xp = await pkang.find_one({"user_id": e.sender_id})
    if xp:
        pack = xp.get("pack") + 1
    await pkang.update_one({"user_id": e.sender_id}, {"$set": {"pack": pack}}, upsert=True)
    pm = random.choice(["af", "bq", "cj", "dp", "eu", "fw", "g", "hu", "wuw", "uw", "hk", "lm", "jr"])
    try:
        p = await telethn(CreateStickerSetRequest(user_id=e.sender_id, title=pname, short_name=f"{pm}{e.sender_id}_{pack}_by_Elf_Robot", stickers=stk))
    except PackShortNameOccupiedError:
        pack += 1
        p = await telethn(CreateStickerSetRequest(user_id=e.sender_id, title=pname + f"Vol {pack}", short_name=f"{pm}{e.sender_id}_{pack}_by_Elf_Robot", stickers=stk))
    except Exception as ex:
        return await e.reply(str(ex))
    await e.reply(f"Sticker Set successfully Kanged to <b><a href='http://t.me/addstickers/{p.set.short_name}'>Pack</a></b>.", buttons=Button.url("View Pack", url=f"http://t.me/addstickers/{p.set.short_name}"), parse_mode="html")
