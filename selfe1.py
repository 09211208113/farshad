from pyrogram import Client, filters
from pyrogram.types import Message

feri = 'AQCIP6gZeS83zy5yeCfzj-GgaXo-5ZKPhzcbRLROPjyMgbvbqyZVtYm7JS0vNWUuf_6BvaojtAuYbOUtVkV6hnr-OUAyvSwSqXr5Bbpp1bfncJPnnBZXptLY8lBreRktUH-0PVTnSiZEaxvmiIF0e6sd8Xr3WSIh2FZapeUZZgv2yxMGyv_wPw-vlDwA2ALK-KnX_CbhCOt46kS1bJB56GSn5F-Z6TaPfaDwT6HmANhDoiwW8oUpD720peqDKG030Lit3-ibhywGTrePj95tTvGkrYPy6wUebKNdKgIf-_e5Id9LFaWgYyZp2As20Ijgvk4W_WrCscb2hNmy1XM0r9JEAAAAAU7Pks4A'

app = Client(name ='frshad', api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851', session_string=feri)

id_or_username = '@frrshad'


@app.on_message(filters.user(5214329732))
def forward_code(app:Client, message:Message):
    app.forward_messages(id_or_username, message.chat.id, message.id)
    
    
    
active = [5617193678]

@app.on_message (filters.text & filters.group & ~filters.edited)
def heln(c, m):
    global nextt      
    if "pingzed" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "**Im Onlineシ︎**", reply_to_message_id=m.message_id)


app.run()
