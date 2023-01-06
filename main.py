import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import pyrogram
import logging
from pyrogram import Client, filters
from subprocess import getstatusoutput
import re
from pyrogram.types import User, Message
import os

import requests
bot = Client(
    "CW",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@bot.on_message(filters.command(["start"]))
async def start(bot, update):
       await update.reply_text("Hi i am **physics wallah Downloader**.\n\n"
                              "**NOW:-** "
                                       
                                       "Press **/login** to continue..\n\n")

@bot.on_message(filters.command(["login"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "Send **Auth code** in this manner otherwise bot will not respond.\n\nSend like this:-  **AUTH CODE**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {

    

    

            'Host': 'api.penpencil.xyz',

            'authorization': f"Bearer {raw_text1}",

            'client-id': '5f439b64d553cc02d283e1b4',

            'client-version': '19.0',

            'user-agent': 'Android',

            'randomid': '987daa96a6200e17',

            'client-type': 'MOBILE',

            'device-meta': '{APP_VERSION:19.0,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.khansirofficial}',

            'content-type': 'application/json; charset=UTF-8',

        # 'content-length': '41',

        # 'accept-encoding': 'gzip' ,
    }

    params = {
       'mode': '2',
       'filter': 'false',
       'exam': '',
       'amount': '',
       'organisationId': '5f439b64d553cc02d283e1b4',
       'classes': '',
       'limit': '20',
       'page': '1',
       'programId': '5f476e70a64b4a00ddd81379',
       'ut': '1652675230446', 
    }
    await editable.edit("**You have these Batches :-\n\nBatch ID : Batch Name**")
    response = requests.get('https://api.penpencil.xyz/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        #batch=(data["name"])
        #batchId=(data["_id"])
        aa=f"```{data['name']}```  :  ```{data['_id']}\n```"
        await m.reply_text(aa)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await editable1.edit("subject : subjectId")
    for data in response2:
       #topic=(data["subject"])
       #topic_id=(data["_id"])
        bb=f"```{data['subject']}```  :  ```{data['_id']}\n```"
        await m.reply_text(bb)
    editable2= await m.reply_text("**Now send the subject ID to Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    for i in range(1,4): 
      params1 = {
        'page': '{i}',
        'tag': '',
        'contentType': 'notes-videos',
        'ut': '',
    }
    response3 = requests.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]
    #await m.reply_text(response3)
    for data in response3:
       #class_title=(data["topic"])
       #class_url=(data["url"])
        cc=f"```{data['topic']}```  :  ```{data['url']}\n```"
        await m.reply_text(cc)
bot.run()

        


        

        

    
