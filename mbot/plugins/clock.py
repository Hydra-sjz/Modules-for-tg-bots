from telethon import events
import asyncio
from collections import deque
from mbot import bot


@bot(outgoing=True, pattern=r"clock")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"))
	for _ in range(60):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
