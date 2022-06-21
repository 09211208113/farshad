from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BAABiGqB8Z6nxt8HVgA-qR9hGNjebFp7Y6dHk5E5uzQL0utMRhxVGKoCwNPHNzZWGVCRDaAcx7LHptt7eW1jCRiNzVJghLrZeVMaLa-yQAbuG7wnFxWZKFEUouZ6QQtR5T0Xukn611revv5cZ3V0cQuxCtyMga95M5M20chuq4Wd48bGkTe_ieR4O1tgzUv3NCMTSqGxTbEsQsOsSoJdmrCVSmLirlsVrWuewPYg7U2o2gJC2oducVW126cXT0PH4usZPZUtYslA9mLFl9AWn26Pa10prl1ppxAeLJV92y3oyWKTwq1e732k-WmvUnoJnAz1MUAflnr6ZqJdnPBtjXSbAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')
  
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
