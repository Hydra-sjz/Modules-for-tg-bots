import os 
from os import error, system, name
import logging
import pyrogram
import PyPDF2
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import ForceReply
from pyrogram.types import User, Message, Document 



DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/PyDF/")
# TXT_LOCATION =  os.environ.get("TXT_LOCATION", "./DOWNLOADS/txt/")
path = './DOWNLOADS/txt/bughunter0.txt'

Disclaimer = """ THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE """  


  
@Client.on_message(filters.private & filters.command(["pdf2txt"])) # PdfToText 
async def pdf_to_text(bot, message):
      try :
           if message.reply_to_message:
                pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
                txt = await message.reply("Downloading.....")
                await message.reply_to_message.download(pdf_path)  
                await txt.edit("Downloaded File")
                pdf = open(pdf_path,'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
                await txt.edit("Getting Number of Pages....")
                num_of_pages = pdf_reader.getNumPages() # Number of Pages
                await txt.edit(f"Found {num_of_pages} Page")
                page_no = pdf_reader.getPage(0) # pageObject
                await txt.edit("Extracting Text from PDF...")
                page_content = """ """ # EmptyString   
                with open(f'{message.chat.id}.txt', 'a+') as text_path:   
                  for page in range (0,num_of_pages):
                      file_write = open(f'{message.chat.id}.txt','a+') 
                      page_no = pdf_reader.getPage(page) # Iteration of page number
                      page_content = page_no.extractText()
                      file_write.write(f"\n page number - {page} \n") # writing Page Number as Title
                      file_write.write(f" {page_content} ")   # writing page content
                      file_write.write(f"\n © BugHunterBots \n ") # Adding Page footer
                   #  await message.reply_text(f"**Page Number  :  {page}  **\n\n  ` {page_content} `\n     @BugHunterBots\n\n") # Use this Line of code to get Pdf Text as Messages
                        
                with open(f'{message.chat.id}.txt', 'a+') as text_path:  
                      await message.reply_document(f"{message.chat.id}.txt",caption="Uploaded by: @HTGToolBot")      
         
                os.remove(pdf_path)
                os.remove(f"{message.chat.id}.txt")  
           else :
                await message.reply("Please Reply to PDF file")
      except Exception as error :
           await txt.delete()
           await message.reply_text(f"{error}")
           os.remove(pdf_path)
           os.remove(f"{message.chat.id}.txt")      
           
@Client.on_message(filters.command(["pinfo"]))
async def pinfo(bot, message):
     try:
         if message.reply_to_message:
              txt = await message.reply_text("Validating Pdf ")  
              pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
              await txt.edit("Downloading.....")
              await message.reply_to_message.download(pdf_path)  
              await txt.edit("Downloaded File")
              pdf = open(pdf_path,'rb')
              pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
              await txt.edit("Getting Number of Pages....")
              num_of_pages = pdf_reader.getNumPages()
              await txt.edit(f"Found {num_of_pages} Page")
              await txt.edit("Getting PDF info..")
              info = pdf_reader.getDocumentInfo()
              await txt.edit(f"""
**Author :** `{info.author}`
**Creator :** `{info.creator}`
**Producer :** `{info.producer}`
**Subject :** `{info.subject}`
**Title :** `{info.title}`
**Pages :** `{num_of_pages}`""")

              os.remove(pdf_path)
         else:
             await message.reply_text("Please Reply to a Pdf File")
     except Exception as error :
         await message.reply_text(f"Oops , {error}")
