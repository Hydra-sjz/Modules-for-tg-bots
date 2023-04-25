# The following code is exact (almost i mean) copy of 
# reverse search taken from @DeletedUser420's Userge-Plugins repo
# originally authored by
# Phyco-Ninja (https://github.com/Phyco-Ninja) (@PhycoNinja13b)
# but is in current state after DeletedUser420's edits
# which made this code shorter and more efficient

import random
import asyncio
import tracemoepy
from tracemoepy.errors import ServerError
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto, InputMediaVideo, Message
from config import BOT_NAME, TRIGGERS as trg
from mbot.ani_utils.helper import check_user, control_user, media_to_image, rand_key
from mbot.ani_utils.data_parser import check_if_adult
from mbot.ani_utils.db import get_collection
#from .anilist import no_pic

SFW_GRPS = get_collection("SFW_GROUPS")
DC = get_collection('DISABLED_CMDS')

TRACE_MOE = {}

@Client.on_message(filters.command(["reverse", f"reverse{BOT_NAME}"], prefixes=trg))
@control_user
async def trace_bek(client: Client, message: Message):
    """ Reverse Search Anime Clips/Photos """
    gid = message.chat.id
    find_gc = await DC.find_one({'_id': gid})
    if find_gc!=None and 'reverse' in find_gc['cmd_list'].split():
        return
    x = await message.reply_text("Reverse searching the given media")
    replied = message.reply_to_message
    if not replied:
        await x.edit_text("Reply to some media !")
        await asyncio.sleep(5)
        await x.delete()
        return
    dls_loc = await media_to_image(client, message, x, replied)
    if dls_loc:
        async with ClientSession() as session:
            tracemoe = tracemoepy.AsyncTrace(session=session)
            try:
                search = await tracemoe.search(dls_loc, upload_file=True)
            except ServerError:
                await x.edit_text('ServerError, retrying')
                try:
                    search = await tracemoe.search(dls_loc, upload_file=True)
                except ServerError:
                    await x.edit_text('Couldnt parse results!!!')
                    return
            result = search["result"][0]
            caption_ = (
                f"**Title**: {result['anilist']['title']['english']} (`{result['anilist']['title']['native']}`)\n"
                f"\n**Anilist ID:** `{result['anilist']['id']}`"
                f"\n**Similarity**: `{(str(result['similarity']*100))[:5]}`"
                f"\n**Episode**: `{result['episode']}`"
            )
            preview = result['video']
        button = []
        nsfw = False
        if await check_if_adult(int(result['anilist']['id']))=="True" and await (SFW_GRPS.find_one({"id": gid})):
            msg = no_pic[random.randint(0, 4)]
            caption="The results parsed seems to be 18+ and not allowed in this group"
            nsfw = True
        else:
            msg = preview
            caption=caption_
            button.append([InlineKeyboardButton("More Info", url=f"https://anilist.co/anime/{result['anilist']['id']}")])
        dls_js = rand_key()
        TRACE_MOE[dls_js] = dls_loc
        button.append([InlineKeyboardButton("Next", callback_data=f"tracech_1_{dls_js}_{gid}")])
        await (message.reply_video if nsfw==False else message.reply_photo)(msg, caption=caption, reply_markup=InlineKeyboardMarkup(button))
    else:
        await message.reply_text("Couldn't parse results!!!")
    await x.delete()


@Client.on_callback_query(filters.regex(pattern=r"tracech_(.*)"))
@check_user
async def tracemoe_btn(client: Client, cq: CallbackQuery):
    kek, page, dls_loc, user = cq.data.split("_")
    try:
        TRACE_MOE[dls_loc]
    except KeyError:
        return await cq.answer("Query Expired!!!\nCreate new one", show_alert=True)
    async with ClientSession() as session:
        tracemoe = tracemoepy.AsyncTrace(session=session)
        try:
            search = await tracemoe.search(TRACE_MOE[dls_loc], upload_file=True)
        except ServerError:
            return await cq.answer("ServerError!!!\nTry again after some time", show_alert=True)
        result = search["result"][int(page)]
        caption = (
            f"**Title**: {result['anilist']['title']['english']} (`{result['anilist']['title']['native']}`)\n"
            f"\n**Anilist ID:** `{result['anilist']['id']}`"
            f"\n**Similarity**: `{(str(result['similarity']*100))[:5]}`"
            f"\n**Episode**: `{result['episode']}`"
        )
        preview = result['video']
    button = []
    if await check_if_adult(int(result['anilist']['id']))=="True" and await (SFW_GRPS.find_one({"id": cq.message.chat.id})):
        msg = InputMediaPhoto(no_pic[random.randint(0, 4)], caption="The results parsed seems to be 18+ and not allowed in this group")
    else:
        msg = InputMediaVideo(preview, caption=caption)
        button.append([InlineKeyboardButton("More Info", url=f"https://anilist.co/anime/{result['anilist']['id']}")])
    if int(page)==0:
        button.append([InlineKeyboardButton("Next", callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}")])
    elif int(page)==(len(search['result'])-1):
        button.append([InlineKeyboardButton("Back", callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}")])
    else:
        button.append([
            InlineKeyboardButton("Back", callback_data=f"tracech_{int(page)-1}_{dls_loc}_{user}"),
            InlineKeyboardButton("Next", callback_data=f"tracech_{int(page)+1}_{dls_loc}_{user}")
        ])
    await cq.edit_message_media(msg, reply_markup=InlineKeyboardMarkup(button))
