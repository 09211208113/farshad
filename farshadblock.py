from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BAAa9CENs3rs_hivaAEY-lifZsIO172CaqbsaAjfDco1oMG-TGno24cL2B8LHoBtMO9BQ1rnpnYB4bFy42UTi_P2p3pzYNyNq2QkU6eFz1MTeJ94qPM345V94RhqNRbFeiuMls7XPx2hMIJ7UzlJDtzKyqEw6E_3_10DmmSADjFcKVJviYL_ZUgw5reTaYvB8FHRNXl6J3sHYq_JMzyzsotqJS7eNRcaqLERWupuUO7WWeiefXKa5RiHSdRAbuzauEWNimc_hcL2ayyHQ37gOFv6Jg6xp1yuhLB1YPNKD_R4W-juyAX3vaCmlpqF-zFMdLbcquyXR4xJ6lh_WAqTi-AAAAAH30Hh0A'

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
