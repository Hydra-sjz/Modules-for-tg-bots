import wikipedia
from pyrogram.types import Message 
from pyrogram import filters, Client



@Client.on_message(filters.command(["wiki", "Wikipedia"]))
async def wikipediasearch(_, message: Message):
    reply = message.reply_to_message
    query =  message.text.split(None, 1)[1] 
    if not query:
        await message.reply_text("ɪɴᴠᴀʟɪᴅ sʏɴᴛᴀx sᴇᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
        return
    results = wikipedia.search(query)
    result = ""
    for s in results:
        try:
            page = wikipedia.page(s)
            url = page.url
            result += f"> [{s}]({url}) \n"
        except BaseException:
            pass
    await message.reply_text(
        "🌐**WikiPedia Search:** {} \n\n📜**Result: \n\n{}".format(query, result))
