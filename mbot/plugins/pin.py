from telethon import events, Button, types
from mbot import bot as tbot
from mbot.utils.status import *

PINS_TEXT = """
**⚡ All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!**
‣ `/pin` - To pinned a reply msg.
‣ `/unpin` - To Unpin the latest pinned msg.
‣ `/unpinall` - To unpinall all pinned msgs at once.
‣ `/pinned` - To get current pinned msg.
**Note:** Add `notify` after /pin to notify all chat members.
"""

@tbot.on(events.NewMessage(pattern="^[/]pinned"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await tbot.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@tbot.on(events.NewMessage(pattern="^[/]pin ?(.*)"))
async def pin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to pin it!")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await tbot.pin_message(event.chat_id, msg, notify=True)
       return
    await tbot.pin_message(event.chat_id, msg)   

@tbot.on(events.NewMessage(pattern="^[/]unpin ?(.*)"))
async def unpin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await tbot.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await tbot.unpin_message(event.chat_id, ok)
    await event.reply(f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.", link_preview=False)

@tbot.on(events.NewMessage(pattern="^[/]permapin"))
async def permapin(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to permapin it.")
       return
    hn = await tbot.send_message(event.chat_id, msg.message)
    await tbot.pin_message(event.chat_id, hn, notify=True)


@tbot.on(events.NewMessage(pattern="^[/]unpinall"))
async def unpinall(event, perm):
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs!")
       return
    UNPINALL = """
Are you sure you want to 
unpin all msgs?
This action can't be undone!
"""

    await tbot.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("Confirm", data="unpin")], 
    [Button.inline("Cancel", data="cancel")]])

@tbot.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await tbot.unpin_message(event.chat_id)
        await event.edit("Unpinned All Msgs!")
        return 

    await event.answer("Group Creator Required!")

@tbot.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("Unpinning of all msgs has been cancelled!")
        return 

    await event.answer("Group Creator Required!")


@tbot.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("Back", data="help")]])
