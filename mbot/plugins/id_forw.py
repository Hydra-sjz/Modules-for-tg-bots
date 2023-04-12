import os
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("id"))
async def id_(bot: Client, msg: Message):
	if not msg.chat.type == "private":
		main = f"This {msg.chat.type}'s ID is `{msg.chat.id}`"
		if msg.reply_to_message:
			if msg.reply_to_message.from_user:
				main = f"{msg.reply_to_message.from_user.first_name}'s ID is `{msg.reply_to_message.from_user.id}`"
				if msg.reply_to_message.sticker:
					main += f"\n\nThis sticker's id is `{msg.reply_to_message.sticker.file_id}`"
		await msg.reply(main)
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Your Telegram ID is: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					uname = uname[1:]
				try:
					user = await bot.get_users(uname)
					name = user.mention
					if len(user.first_name) <= 20:
						pass
					elif user.is_bot:
						name = "This Bot"
					else:
						name = "This User"
				except IndexError:
					user = await bot.get_chat(uname)
					name = '@'+user.username if user.username else user.title
				id = user.id
				await msg.reply(f"{name}'s id is `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("This username is not occupied by anyone", quote=True)


@Client.on_message(filters.private & filters.forwarded)
async def forwarded(_, msg):
    if msg.forward_from:
        text = "Forward detected! \n\n"
        if msg.forward_from.is_bot:
            text += "**Bot**"
        else:
            text += "**User**"
        text += f'\n{msg.forward_from.first_name} \n'
        if msg.forward_from.username:
            text += f'@{msg.forward_from.username} \nID : `{msg.forward_from.id}`'
        else:
            text += f'ID : `{msg.forward_from.id}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"Forward Detected. \n\n"
            if msg.forward_from_chat.type == "channel":
                text += "**Channel**"
            if msg.forward_from_chat.type == "supergroup":
                text += "**Group**"
            text += f'\n{msg.forward_from_chat.title} \n'
            if msg.forward_from_chat.username:
                text += f'@{msg.forward_from_chat.username} \n'
                text += f'ID : `{msg.forward_from_chat.id}`'
            else:
                text += f'ID : `{msg.forward_from_chat.id}`'
            await msg.reply(text, quote=True)

# Sticker id-------
@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Here is your sticker id**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique id is: ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("ɴɪᴄᴇ,ɪᴛs ɴᴏᴛ ᴀ sᴛɪᴄᴋᴇʀ")

# Dc finder
@Client.on_message(filters.private & filters.command(["dc"]))
async def dc(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

START_TEXT = "Your dc is : `{}`"
