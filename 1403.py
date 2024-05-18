
from pyrogram import Client, filters
import random
from time import sleep
feri = 'BACx5OIph6_9dsghZo87y5Vl3juIQ5mTWLg0icvI2VaAU5a-Wv8U_fD7XfLEzDRQNDhLHmfAPQRPbtuwlwVEU9vK21kNFny_yRj6Br4QXNlo4wBhhrp1u6_1EQvYTJMpkbjxwBCA__c2FYV68h9euis7LLxqWvw-_vC72F_ZyQzk-TTsk9Njzf-c1bxqUP2omVPQSOzwEU1x1gC_vE51g3qQcuURB9EusN95GPIi8enADicMByTdSZjJadVl3vdiq0MAFR0qHReYM7nRJEQfqek1hqb24R7VBufVzsatKIWeuFOAqGUEWNdXVVnhkTo_Xe_j0sqTtUSo9C-uaVeRW8EAAAAAATuwAm0A'
tag_stop = {};tags = {};mention = '';tglist = '';speed = 1

api_id =2094105 #your api id 
api_hash = '91eb9e4b583b6e7ec3a6df7ef5be2be0'#your api hash
app = Client('feri', api_id, api_hash,workers=7)


@app.on_message(filters.command(['speed'],None))
def spd(client, message):
    global speed
    try:
        speed = int(message.command[1])
        message.reply_text('**Speed  to {} Changed ✅**'.format(speed))
    except Exception:
        message.reply_text('**برای تنظیم سرعت به این شکل عمل کنید\nspeed NUMBER**')
        
@app.on_message(filters.text & filters.user([205092371,5617193678]) & filters.regex('tag'))
@app.on_message(filters.text & filters.user([205092371,5617193678]) & filters.regex('deltag'))
@app.on_message(filters.text & filters.regex('stop'))
@app.on_message(filters.text & filters.regex('بسه'))
def tag(client, message):
    global tags, tag_stop
    if message.text.split()[0] == 'tag':
        try:
            text = message.text[5:]
        except:
            text = ''
        tag_stop[message.chat.id] = False
        result2 = app.get_chat_members(message.chat.id, limit=500)
        s = []
        for usr in result2:
            if tag_stop[message.chat.id]:
                break
            if usr.user.id != message.from_user.id and not usr.user.is_bot and usr.user.first_name is not None:
                result = app.send_message(chat_id=message.chat.id,
                                          text=f'[{usr.user.first_name}](tg://user?id={usr.user.id}) {text}')
                s.append(result.message_id)
                sleep(speed)
        try:
            u = tags[message.chat.id]
            u += s
            tags[message.chat.id] = u
        except:
            tags[message.chat.id] = s
    elif message.text.split()[0] == 'deltag':
        try:
            try:
                Ids = tags[message.chat.id]
            except:
                app.send_message(message.chat.id, '**tag pyda nshd !**')
                Ids = message.message_id
            app.send_message(chat_id=message.chat.id,
                                      text="**Ok シ︎**")
            app.delete_messages(chat_id=message.chat.id, message_ids=tags[message.chat.id])
            app.send_message(chat_id=message.chat.id,
                                      text="**tags pak shud✔︎**")
            try:
                tags.pop(message.chat.id)
            except:
                None
        except Exception as e:
            app.send_message(message.chat.id, str(e))
    elif message.text.split()[0] == 'stop':
        tag_stop[message.chat.id] = True
        app.send_message(chat_id=message.chat.id, text='**Ok !**')
    elif message.text.split()[0] == 'بسه':
        tag_stop[message.chat.id] = True
        app.send_message(chat_id=message.chat.id, text='**Ok !**')


app.run()
