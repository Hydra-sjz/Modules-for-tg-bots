from pyrogram import Client, filters
from pyrogram.types import Message
from speedtest import Speedtest

from mbot.helpers.decorators import ratelimiter, run_sync_in_thread
from mbot.helpers.functions import get_readable_bytes
from mbot.helpers.filters import sudo_cmd
from mbot.logging import LOG


@run_sync_in_thread
def speedtestcli():
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    return test.results.dict()


@Client.on_message(filters.command(["speedtest", "speed"]) & sudo_cmd)
@ratelimiter
async def speedtest(_, message: Message):
    """
    Give speedtest of the server where bot is running.
    """
    
    speed = await message.reply("Running speedtest....", quote=True)
    LOG(__name__).info("Running speedtest....")
    result = await speedtestcli()

    speed_string = f"""
Upload: {get_readable_bytes(result["upload"] / 8)}/s
Download: {get_readable_bytes(result["download"] / 8)}/s
Ping: {result["ping"]} ms
ISP: {result["client"]["isp"]}
"""
    await speed.delete()
    return await message.reply_photo(
        photo=result["share"], caption=speed_string, quote=True)
