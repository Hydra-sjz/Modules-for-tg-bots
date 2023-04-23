from pyrogram import filters
from pyrogram.types import Message
from mbot import SUDO_USERS, OWNER_ID


def dev_users(_, __, message: Message) -> bool:
    return message.from_user.id in OWNER_ID if message.from_user else False


def sudo_users(_, __, message: Message) -> bool:
    return message.from_user.id in SUDO_USERS if message.from_user else False


dev_cmd = filters.create(dev_users)
sudo_cmd = filters.create(sudo_users)
