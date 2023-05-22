 #  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE
#  Code edited By Cryptostark
import urllib
import urllib.parse
import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode

@bot.on_message(filters.command("pw"))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
        "**Now Send Your PW Auth Token:**"
    )  
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1=input1.text
    headers = {
            'Host': 'api.penpencil.co',
            'authorization': f"Bearer {raw_text1}",
            'client-id': '5eb393ee95fab7468a79d189',
            'client-version': '1910',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
            'randomid': 'e4307177362e86f1',
            'client-type': 'WEB',
            'content-type': 'application/json; charset=utf-8',
    }
    params = {
       'mode': '1',
       'amount': 'paid',
       'page': '1',
    }
    await m.reply_text("**You have these Batches :-\n\nBatch ID : Batch Name**")
    aa=''
    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch_name = data['name']
        batch_id = data['_id']
        aa = aa + f'**{batch_name}**  :  ```{batch_id}```\n\n'
    await m.reply_text(aa)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await m.reply_text("Subject : Subject_Id")
    bb= ''
    for data in response2:
        subject_name = data['subject']
        subject_id = data['_id']
        bb = bb  + f'**{subject_name}**  :  ```{subject_id}```\n\n'
    await m.reply_text(bb)
    editable2= await m.reply_text("**Now send the subject ID to Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await m.reply_text('**Now Send Content Type you want to extract.**\n```DppNotes```|```videos```|```notes```')
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xx =await m.reply_text("Genrating Course txt in this id")
    to_write = ''
    for i in range(1,15):
        params1 = {
        'page': f'{i}',
        'tag': '',
        'contentType': f'{raw_text5}',import requests
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
    await m.reply_text("**You have these Batches :-\n\nBatch ID : Batch Name**")
    aa=''
    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    for data in response:
        batch_name = data['name']
        batch_id = data['_id']
        aa = aa + f'**{batch_name}**  :  ```{batch_id}```\n\n'
    await m.reply_text(aa)
    editable1= await m.reply_text("**Now send the Batch ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
    await m.reply_text("Subject : Subject_Id")
    bb= ''
    for data in response2:
        subject_name = data['subject']
        subject_id = data['_id']
        bb = bb  + f'**{subject_name}**  :  ```{subject_id}```\n\n'
    await m.reply_text(bb)
    editable2= await m.reply_text("**Now send the subject ID to Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await m.reply_text('**Now Send Content Type you want to extract.**\n```DppNotes```|```videos```|```notes```')
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xx =await m.reply_text("Genrating Course txt in this id")
    to_write = ''
    for z in range(1,15): # max 15 pages
        print(z) 
        params1 = {
        'page': f'{z}',
        'tag': '',
        'contentType': f'{raw_text5}',
        }
        
        response3 = requests.get(f'https://api.penpencil.co/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]
        #with open(f"1pwnotes.json", "w", encoding="utf-8") as f:
        #    f.write(f'{response3}')
        #    print(1)
        #    sys.exit(1)
        
        if raw_text5 == 'videos':
            for data in response3:
                try:      
                    url = f"https://d26g5bnklkwsh4.cloudfront.net/{data['url'].split('/')[-2]}/hls/720/main.m3u8" if raw_text5 == "videos" else f"{data['baseUrl']}{data['key']}"
                    topic = data['topic']
                    #print(url)
                    write = f"{topic} {url}\n"
                    to_write = to_write + write
                except:
                    pass
        else: #for notes + dpps
            for i in range(len(response3)):
                #print(response3)
                #print(data1)
                try:
                    print(f'{i} {z} ')
                    c=response3[i]
                    b=c['homeworkIds'][0]
                    a = b['attachmentIds'][0]
                
                    #print(f'{b}')
                    name = response3[i]['homeworkIds'][0]['topic'].replace('|',' ').replace(':',' ')
                    #name = a['name']
                    url = a['baseUrl'] + a['key']
                    write = f"{name} {url}\n"
                    to_write = to_write + write
                except:
                    pass

    with open(f"{raw_text5} {raw_text4}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{raw_text5} {raw_text4}.txt", "rb") as f:   
       # print(3)  
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
        await xx.delete(True)
       # print(2)
    bot.run()

        


        

        

    
        }
        response3 = requests.get(f'https://api.penpencil.co/v2/batches/{raw_text3}/subject/{raw_text4}/contents', params=params1, headers=headers).json()["data"]
        if raw_text5 == 'videos':
            for data in response3:      
                url = f"https://d26g5bnklkwsh4.cloudfront.net/{data['url'].split('/')[-2]}/hls/720/main.m3u8" if raw_text5 == "videos" else f"{data['baseUrl']}{data['key']}"
                topic = data['topic']
                write = f"{topic} {url}\n"
                to_write = to_write + write
        else:
            for data in response3:
                a = data['homeworkIds'][0]['attachmentIds'][0]
                name = data['homeworkIds'][0]['topic'].replace('|',' ').replace(':',' ')
                url = a['baseUrl'] + a['key']
                write = f"{name} {url}\n"
                to_write = to_write + write

    with open(f"{raw_text5} {raw_text4}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
    with open(f"{raw_text5} {raw_text4}.txt", "rb") as f:   
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
        await xx.delete(True)
bot.run()
