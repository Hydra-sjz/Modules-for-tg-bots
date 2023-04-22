
import io
import os
from datetime import datetime

import requests
from telethon import types
from telethon.tl import functions

from mbot import REM_BG_API_KEY, TEMP_DOWNLOAD_DIRECTORY, bot as telethn
from mbot.events import register


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await telethn(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/rmbg")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group and not await is_register_admin(
        event.input_chat, event.message.sender_id
    ):
        return
    if REM_BG_API_KEY is None:
        await event.reply("ʏᴏᴜ ɴᴇᴇᴅ API ᴛᴏᴋᴇɴ from ʀᴇᴍᴏᴠᴇ.ʙɢ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴘʟᴜɢɪɴ.")
        return False
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
        await event.reply("ᴘʀᴏᴄᴇssɪɴɢ....")
        try:
            downloaded_file_name = await telethn.download_media(
                reply_message, TEMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await event.reply(str(e))
            return
        else:
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    else:
        HELP_STR = "ᴜsᴇ `/rmbg` ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ"
        await event.reply(HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "rmbg.png"
            await telethn.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id,
            )
        end = datetime.now()
        ms = (end - start).seconds
        await event.reply(f"ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇᴅ ɪɴ {ms} sᴇᴄᴏɴᴅs")
    else:
        await event.reply(
            f"ʀᴇᴍᴏᴠᴇ.ʙɢ ᴀᴘɪ ʀᴇᴛᴜʀɴᴇᴅ ʀᴇᴛᴜʀɴᴇᴅ. ᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ  @Spotifyx_dlbot \n".format(
                output_file_name.content.decode("UTF-8")
            )
        )


def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    return requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
