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
      
      
wwbot = [491459293, 175844556]
gp = []
@app.on_message(filters.command(['!speedjoingame'],None))
def spd(client, message):
    global speed
    try:
        speed = int(message.command[1])
        message.reply_text('**Speed Join {} **'.format(speed))
    except Exception:
        message.reply_text('**برای تنظیم سرعت به این شکل عمل کنید\nspeed NUMBER**')
        

@app.on_message(filters.command('join', '!') & filters.me)
def join_game(_, m: Message):
    if len(m.command) == 3:
        chat_id = int(m.command[1])
        print(chat_id)
        if m.command[2].lower() == 'on':
            if chat_id not in gp:
                gp.append(chat_id)
                m.edit_text('**Outo On**')
            else:
                m.edit_text('**Outo Online**')
        elif m.command[2].lower() == 'off':
            if chat_id in gp:
                gp.remove(chat_id)
                m.edit_text('**Outo Off**')
            else:
                m.edit_text('**Outo Offline**')
        else:
            m.edit_text('**ورودی اشتباس**')
    else:
        m.edit_text('**دستور صحیح ارسال گردد**')


@app.on_message(filters.caption & filters.inline_keyboard & filters.user(wwbot))
def sjoin(app: Client, m: Message):
    if int(m.chat.id) in gp:
        link = m.reply_markup.inline_keyboard[0][0].url
        link = link.split("=")[1]
        sleep(speed)
        app.send_message(m.from_user.id, f"/start {link}")
    
app.run()
