from telethon import events, Button
from mbot import bot as tbot
from mbot.utils.status import *
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@tbot.on(events.callbackquery.CallbackQuery(data="gadmin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("Back", data="help")]])

@tbot.on(events.NewMessage(pattern="^[/]promote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("This command is made to be used in groups, not in PM!")
       return

    if not perm.add_admins:
        await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to promote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"Successfully Promoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!")
        return

    await event.reply(f"Succesfully Promoted {input_str} in {event.chat.title}")
 
@tbot.on(events.NewMessage(pattern="^[/]demote ?(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return
    if not perm.add_admins:
        await event.reply("You are missing the following rights to use this command:CanAddAdmins!")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("Reply to a user or give its username to demote him!")
        return
    sed = await tbot(GetFullUserRequest(id=user.sender_id or input_str))
    await tbot(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"Successfully Demoted [{sed.user.first_name}](tg://user?id={user.sender_id}) in {event.chat.title}!")
        return

    await event.reply(f"Succesfully Demoted {input_str} in {event.chat.title}")
 

@tbot.on(events.NewMessage(pattern="^[/]invitelink"))
async def invitelink(event):

    if event.is_private:
       await event.reply("This cmd is made to be used in groups, not in PM!")
       return
    link = await tbot(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"Group link of {event.chat.title} is [here]({link.link})", link_preview=False)

ADMIN_TEXT = """
**✘ A module from which admins of the chat can use!**
‣ `/promote` - To Promote a user in the chat.
‣ `/demote` - To Demote a user in the chat.
‣ `/invitelink` - To get invitelink of a chat.
"""
