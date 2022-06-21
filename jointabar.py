from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep


feri = 'AQB-9RF0ZJ8C4BmAJFp3iLtDsN6Of_cplgxexaw2q_Y16m86AlITiw6m6b17ycH3u4Efthva4HC2n8qv-Ky9dCo5goj21uGpMrKidSIXojttYqTjaPIVAasG9EYAXArfojKqBAyOFtHiJlwklTNl0EP5YGZB4ndv1baKtT7_4kJJhmke_QMkpQpOS7Mv9ouNCyuGCPim8lYWMrRAyuW84yFqJdu-00jZl0Og_aOvzKvrnesiR79r3jenzDTw8KzNUIIo6R0Kb7LSS6Dq8rfS-bEjI1LBIKLLdh3CKgoDopa9w2v8o8XVRWWF1SceuvXRzeHPxUJ1oVTqsu9lH2jm2BBAAAAAATs5ToYA'

app = Client(session_name=feri, api_id=13970534, api_hash='b610e73718c72d2e6148124696d72361')
   
   
wwbot = [491459293, 175844556]
gp = []
@app.on_message(filters.command(['speedjoin'], & filters.me))
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
