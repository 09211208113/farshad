from pyrogram import Client, filters
from requests import get
import pyrogram
import json
from time import sleep

pmtags = []

feri = 'BAC2WUezDaB-CR63VY8xPKqRIFOVCR1LPTuLm7hxi2UMajFIvb3IlTNnJhZPtubtK8s5urXxlQ00qavoayF1yAXSIJ_3SL8SCZkLXA5oE9I8M5k2V3PcivjinEWAZgdcFgCmfdprNfKBPSfldoLhYIlLB6Ilq5urxuD-tEEwr-QE9dAT3UJA6ka70-JxN5eWqIYJQd-ZtxaXH9qpkYeJptygMUjGgE474GctsupS5SMYr0hVa3TDuk7W2Ex2sJfATsKKFxt4CWlgopy1q1e1JihNk-7kVUTq0peY4jyxkmjUPUdfNkxfk1yqKjgkuXFHBse_H0R5KU8XbAXtvg6fFVrCAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')
  
@app.on_message(filters.text & filters.me & filters.regex('Block'))
def block_users(client,message):
    user = message.reply_to_message.from_user.id
    app.block_user(user)
    message.reply_text('**User block✅**')


@app.on_message(filters.text & filters.me & filters.regex('Unblock'))
def unblock_user(client,message):
    user = message.reply_to_message.from_user.id
    app.unblock_user(user)
    message.reply_text('**User unblock✅**')
    
app.run()
