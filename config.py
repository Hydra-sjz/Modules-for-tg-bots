import os
from os import getenv
from dotenv import load_dotenv
from os import environ

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))


#Port
PORT = os.environ.get("PORT", "8080")
