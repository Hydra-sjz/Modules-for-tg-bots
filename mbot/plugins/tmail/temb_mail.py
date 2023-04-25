from pyrogram import *
import requests as re
from mbot import Mbot as app
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
import wget
import os 

buttons=InlineKeyboardMarkup(
                             [
                             [
            InlineKeyboardButton('Generate', callback_data='generate'),
            InlineKeyboardButton('Refresh', callback_data='refresh'),
            InlineKeyboardButton('Close', callback_data='close')
                   ] 
                             ])

msg_buttons=InlineKeyboardMarkup(
                             [
                             [
            InlineKeyboardButton('View message', callback_data='view_msg'),
            InlineKeyboardButton('Close', callback_data='close')
                   ] 
                             ])


# Fillout The variables in Config.py further queries @riz4d 0n telegram

email=''
@app.on_message(filters.command('tembmail'))
async def start_msgsd(client,message):
    await message.reply("**Hey❕**\n @ is a free service that allows to generates and receive emails at a temporary address that self-destructed after a certain time elapses.\n\n**__ How It Safe's You??**__\n- Using the temporary mail allows you to completely protect your real mailbox against the loss of personal information. Your temporary e-mail address is completely anonymous. Your details: information about your person and users with whom you communicate, IP-address, e-mail address are protected and completely confidential")
    await message.reply("**Generate a Email Now❕**",
                        reply_markup=buttons)
@app.on_callback_query()
async def mailbox(client,message):
    response=message.data
    if response=='generate':
       global email
       email = re.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
       await message.edit_message_text('__**Your Temporary E-mail: **__`'+str(email)+'`',
                                       reply_markup=buttons)
       print(email)
    elif response=='refresh':
        print(email)
        try:
            if email=='':
                await message.edit_message_text('Genaerate a email',reply_markup=buttons)
            else: 
                getmsg_endp =  "https://www.1secmail.com/api/v1/?action=getMessages&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:]
                print(getmsg_endp)
                ref_response = re.get(getmsg_endp).json()
                global idnum
                idnum=str(ref_response[0]['id'])
                from_msg=ref_response[0]['from']
                subject=ref_response[0]['subject']
                refreshrply='You a message from '+from_msg+'\n\nSubject : '+subject
                await message.edit_message_text(refreshrply,
                                                reply_markup=msg_buttons)
        except:
            await message.answer('No messages were received..\nin your Mailbox '+email)
    elif response=='view_msg':
        msg =re.get("https://www.1secmail.com/api/v1/?action=readMessage&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + idnum).json()
        print(msg)
        from_mail=msg['from']
        date=msg['date']
        subjectt=msg['subject']
        try:
          attachments=msg['attachments'][0]
        except:
            pass
        body=msg['body']
        mailbox_view='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body
        await message.edit_message_text(mailbox_view,reply_markup=buttons)
        mailbox_view='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body
        if attachments == "[]":
            await message.edit_message_text(mailbox_view,reply_markup=buttons)
            await message.answer("No Messages Were Recieved..", show_alert=True)
        else:
            dlattach=attachments['filename']
            attc="https://www.1secmail.com/api/v1/?action=download&login=" + email[:email.find("@")] + "&domain=" + email[email.find("@") + 1:] + "&id=" + idnum+"&file="+dlattach
            print(attc)
            mailbox_vieww='ID No : '+idnum+'\nFrom : '+from_mail+'\nDate : '+date+'\nSubject : '+subjectt+'\nmessage : \n'+body+'\n\n'+'[Download]('+attc+') Attachments'
            filedl=wget.download(attc)
            await message.edit_message_text(mailbox_vieww,reply_markup=buttons)
            os.remove(dlattach)
