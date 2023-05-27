import openai
import asyncio
import html
from aiohttp import ClientSession
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.errors import MessageTooLong


from mbot import Mbot as app
#from misskaty.helper.localization import use_chat_lang
from helper2 import post_to_telegraph, check_time_gap
from mbot.utils2.ratelimiter import ratelimiter
from config import OPENAI_API
from mbot import SUDO_USERS

openai.api_key = OPENAI_API
#COMMAND_HANDLER = ","!", "/"


@app.on_message(filters.command("ask"))
@ratelimiter
async def chatbot(self: Client, ctx: Message, strings):
    if len(ctx.command) == 1:
        return await ctx.reply_message("Please use command <code>/{cmd} [question]</code> to ask your question.").format(cmd=ctx.command[0]), quote=True, del_in=5)
    uid = ctx.from_user.id if ctx.from_user else ctx.sender_chat.id
    is_in_gap, sleep_time = await check_time_gap(uid)
    if is_in_gap and (uid not in SUDO_USERS):
        return await ctx.reply_message("Don't spam please, please wait second or i will ban you from this bot."), del_in=5)
    openai.aiosession.set(ClientSession())
    pertanyaan = ctx.input
    msg = await ctx.reply_messages("Wait a moment looking for your answer."), quote=True)
    num = 0
    answer = ""
    try:
        response = await openai.ChatCompletion.acreate(model="gpt-3.5-turbo", messages=[{"role": "user", "content": pertanyaan}], temperature=0.2, stream=True)
        async for chunk in response:
            if not chunk.choices[0].delta or chunk.choices[0].delta.get("role"):
                continue
            num += 1
            answer += chunk.choices[0].delta.content
            if num == 30:
                await msg.edit_msg(answer)
                await asyncio.sleep(1.5)
                num = 0
        await msg.edit_msg(answer)
    except MessageTooLong:
        answerlink = await post_to_telegraph(False, "Open Ai", html.escape(answer))
        await msg.edit_message(f"Question for youmnswer has exceeded TG text limit, check this link to view.\n\n{answerlink}").format(answerlink=answerlink), disable_web_page_preview=True)
    except Exception as err:
        await msg.edit_msg(f"ERROR Bro: {str(err)}")
    await openai.aiosession.get().close()
