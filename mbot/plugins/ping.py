import time
from datetime import datetime
from pyrogram.types import Message
from pyrogram import Client, filters, enums

StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(filters.command("ping"))
async def ping_bot(_, message):
    start_time = time.time()
    m = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    n = await message.reply_chat_action(enums.ChatAction.TYPING)
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await m.edit_text(f"**🏓 ᴘᴏɴɢ!!:** `{ping_time} ms`\n**🆙 ᴜᴘᴛɪᴍᴇ:** `{uptime}`")
