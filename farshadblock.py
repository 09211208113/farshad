#pip install telethon


from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

import random
from time import sleep


import redis #sudo apt-get install redis / pip install redis
import asyncio #pip install redis

redis = redis.Redis(host='localhost', port=6379, db=0)

pmtags = []

feri = 'BAC2WUezDaB-CR63VY8xPKqRIFOVCR1LPTuLm7hxi2UMajFIvb3IlTNnJhZPtubtK8s5urXxlQ00qavoayF1yAXSIJ_3SL8SCZkLXA5oE9I8M5k2V3PcivjinEWAZgdcFgCmfdprNfKBPSfldoLhYIlLB6Ilq5urxuD-tEEwr-QE9dAT3UJA6ka70-JxN5eWqIYJQd-ZtxaXH9qpkYeJptygMUjGgE474GctsupS5SMYr0hVa3TDuk7W2Ex2sJfATsKKFxt4CWlgopy1q1e1JihNk-7kVUTq0peY4jyxkmjUPUdfNkxfk1yqKjgkuXFHBse_H0R5KU8XbAXtvg6fFVrCAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')
  
try:
    import socks #pip install socks 
    proxy = (socks.SOCKS5, '127.0.0.1', 9150) #start tor
    client = TelegramClient(phone, api_id, api_hash,proxy=proxy)
    client.connect()
except:
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()


if not client.is_user_authorized(): 
    try:
        client.send_code_request(phone) 
        client.sign_in(code=input('Your Code :')) 
    except SessionPasswordNeededError:
        client.sign_in(password=input('your Password :'))
        
admin = [2113150493]
bot_id = [198626752,175844556]
group_id = int(input("group id :-1001180855931"))


data_base = {'shkar':0,'ray':'','naghsh':'','ghofli':'','ros':0,'fereshte':0,'karagah':0,'pishgo':0,'negahbani':''}
me = client.get_me()
redis.set(me.id,str(data_base))

async def main():
    @client.on(events.NewMessage(pattern=r'/ping'))
    async def shekar_1(event):
        if event.chat_id == group_id:
            if event.sender_id in admin:
                await event.reply('online')

 
    @client.on(events.NewMessage(pattern=r'یک بازی با حالت'))
    async def start_ganme(event):
        if event.chat_id == group_id:
            if event.sender_id in bot_id:
                text_url = await client.get_messages(event.chat_id)
                bot_ids = event.sender_id
                text_url = str(text_url[0].reply_markup).split("start=")[1].split("'")[0]
                await client.send_message(bot_ids,"/start "+text_url)
                await asyncio.sleep(2) 
                await client.send_message(bot_ids,"/start "+text_url)
                await asyncio.sleep(2) 
                await client.send_message(bot_ids,"/start "+text_url)
                me = await client.get_me()
                get_list = redis.get(me.id)
                get_list = eval(get_list.decode('utf-8'))
                get_list['shkar'] = 0
                get_list['ros'] = 0
                get_list['karagah'] = 0
                get_list['fereshte'] = 0
                get_list['pishgo'] = 0
                get_list['negahbani'] = ''
                get_list['naghsh'] = ''
                get_list['ray'] = ''
                redis.set(me.id,str(get_list))
    
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
client.start()
client.run_until_disconnected() 
