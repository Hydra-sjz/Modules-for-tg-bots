from pyrogram import filters, Client
from pyrogram.types import Message
from mbot import Mbot as app
import logging
from helper.http import http
from config import CURRENCY_API
__MODULE__ = "Currency"
__HELP__ = """
/currency - Send structure message Telegram in JSON using Pyrogram Style.
"""
LOGGER = logging.getLogger(__name__)
@app.on_message(filters.command(["currency"]))
async def currency(self: Client, ctx: Message):
    if CURRENCY_API is None:
        return await ctx.reply_msg(
            "<code>Oops!!get the API from</code> <a href='https://app.exchangerate-api.com/sign-up'>HERE</a> <code>& add it to config vars</code> (<code>CURRENCY_API</code>)",
            disable_web_page_preview=True,
        )
    if len(ctx.text.split()) != 4:
        return await ctx.reply_msg(f"Use format /{ctx.command[0]} [amount] [currency_from] [currency_to] to convert currency.", del_in=6)
    teks = ctx.text.split()
    amount = teks[1]
    currency_from = teks[2]
    currency_to = teks[3]
    if amount.isdigit() or (amount.replace('.','',1).isdigit() and amount.count('.') < 2):
        url = f"https://v6.exchangerate-api.com/v6/{CURRENCY_API}/{currency_from}/{currency_to}/{amount}"
        try:
            res = await http.get(url)
            data = res.json()
            try:
                conversion_rate = data["conversion_rate"]
                conversion_result = data["conversion_result"]
                target_code = data["target_code"]
                base_code = data["base_code"]
                last_update = data["time_last_update_utc"]
            except KeyError:
                return await ctx.reply_msg("<code>Invalid response from api !</i>")
            await ctx.reply_msg(f"**CURRENCY EXCHANGE RATE RESULT:**\n\n`{format(float(amount), ',')}` **{base_code}** = `{format(float(conversion_result), ',')}` **{target_code}**\n<b>Rate Today</b> = `{format(float(conversion_rate), ',')}`\n<b>Last Update:</b> {last_update}")
        except Exception as err:
            await ctx.reply_msg(f"Failed convert currency, maybe you give wrong currency format or api down.\n\n<b>ERROR</b>: {err}")
    else:
        await ctx.reply_msg("<code>This seems to be some alien currency, which I can't convert right now.. (⊙_⊙;)</code>")
