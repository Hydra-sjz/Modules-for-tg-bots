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
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736 5422115985").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))

AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

## A sql database url from elephantsql.com
DB_URI = os.environ.get("DB_URl", "")
#PostgreSQL
PDB_URL = os.environ.get("PDB_URL", "")
#Port
PORT = os.environ.get("PORT", "8080")


TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)  # From:- https://www.remove.bg/

AUTO_DELETE = bool(environ.get("AUTO_DELETE", True))
AUTO_DELETE_SECOND = int(environ.get("AUTO_DELETE_SECOND", 300))

OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", None)
CURRENCY_API = environ.get("CURRENCY_API", None)

SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/8be5b452a11964129d60b.jpg")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
