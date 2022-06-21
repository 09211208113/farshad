from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BABD1hMGa4zV0zkXsnhNcy9bxGcgRa8j0jnrzaoghmUv5NsZdmGM2jMqae2GF6hPC3S7wEV7-Vl0zntZXv3AF2AuzrWmQdDC605QCWBcra8LRg-SsKcN961neIR1tXmoNzsfU1NSu7vvo3Eizn8Rchz_dZlEByYz83O3Qid8wGErIHk8uFE72n39PsKcCtXUDAEIqCBw5GdPiAThSwU0ivqG7llIPDlSs_q7p4QDQYD2P6v7XH2JQDuExxJEK-Mra_XLT7UUgbq2CIhU-mUGXRvbwSvubQYT00o6aQPCzovB1cVVY43V9omfBFqOJ1zIIx1jdYYE5Pi-FL0n01-QOKOCAAAAAH30Hh0A'

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
