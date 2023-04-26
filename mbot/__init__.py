"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import logging
from os import environ, mkdir, path, sys

from dotenv import load_dotenv
from pyrogram import Client
from telegraph import Telegraph

import time
import deethon
from dotenv import load_dotenv
from telethon import TelegramClient, events, functions, types
from telegraph import Telegraph


telegraph = Telegraph()
CMD_HELP = {}

formatter = logging.Formatter('%(levelname)s %(asctime)s - %(name)s - %(message)s')

fh = logging.FileHandler(f'{__name__}.log', 'w')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

telethon_logger = logging.getLogger("telethon")
telethon_logger.setLevel(logging.WARNING)
telethon_logger.addHandler(ch)
telethon_logger.addHandler(fh)

botStartTime = time.time()



load_dotenv()



# Saving user preferences locally
users = {}

#=========================
load_dotenv("config.env")

# Log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Mandatory Variable
try:
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    BOT_TOKEN = environ["BOT_TOKEN"]
    OWNER_ID = int(environ["OWNER_ID"])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)

# Optional Variable

SUDO_USERS = environ.get("SUDO_USERS", str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
AUTH_CHATS = environ.get("AUTH_CHATS").split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
LOG_GROUP = environ.get("LOG_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)

telegraph = Telegraph()

logger.debug(f'Using deethon v{deethon.__version__}')

bot = TelegramClient(__name__, API_ID, API_HASH, base_logger=telethon_logger).start(bot_token=BOT_TOKEN)
logger.info("TELETHON STARTED BROOO")


#========lol===========

class Mbot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir="./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30,
        )

    async def start(self):
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists("/tmp/thumbnails/"):
            mkdir("/tmp/thumbnails/")
        for chat in AUTH_CHATS:
            await self.send_photo(
                chat,
                "https://telegra.ph/file/5791b80b0c4349c85c604.jpg",
                "**Bot Started.** 🎵",
            )
        LOGGER.info(f"PYROGRAM STARTED AS {BOT_INFO.username}\n")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("PYROGRAM STOPPED BRO.")
