import asyncio
import datetime
import re
from datetime import datetime
from telethon import custom, events
from mbot import bot as bot
from mbot import bot as tgbot
from mbot.events import register
edit_time = 5
""" =======================MAKIMA====================== """
file1 = "https://te.legra.ph/file/a7b9d85ff1c76d1443b33.jpg"
file2 = "https://te.legra.ph/file/c15aef6eac07e186c1732.jpg"
file3 = "https://te.legra.ph/file/2cae3667556c4b8f4ddf6.jpg"
file4 = "https://te.legra.ph/file/b89feab3943deb5457340.jpg"
file5 = "https://te.legra.ph/file/01c470e7a3ee54fe33c56.jpg"
""" =======================MAKIMA====================== """
@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )
    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)
    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)
    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "POWERED BY 𝓚𝒶кคѕⒽᎥ ђ𝔞𝓉ᗩЌ𝒆 ⸙『𝕭𝖎𝖓𝖌𝖊』 ᭄™ \n\n"
        LILIE += f"FIRST NAME : {PRO.first_name} \n"
        LILIE += f"LAST NAME : {PRO.last_name}\n"
        LILIE += f"YOU BOT : {PRO.bot} \n"
        LILIE += f"RESTRICTED : {PRO.restricted} \n"
        LILIE += f"USER ID : {boy}\n"
        LILIE += f"USERNAME : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")
