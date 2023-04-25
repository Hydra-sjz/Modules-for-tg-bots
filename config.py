import os
from os import getenv
from dotenv import load_dotenv
from os import environ
import json



if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))

AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

#Port
PORT = os.environ.get("PORT", "8080")


TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)  # From:- https://www.remove.bg/

AUTO_DELETE = bool(environ.get("AUTO_DELETE", True))
AUTO_DELETE_SECOND = int(environ.get("AUTO_DELETE_SECOND", 300))

OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)


BOT_NAME = os.environ.get("BOT_NAME", "@Spotifyx_dlbot")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1001616139929"))
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split()

DOWN_PATH = "anibot/downloads/"
HELP_DICT = dict()
plugins = dict(root="anibot/plugins")
