from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BABUxuoXA_F_x7IxPQ1h3THXCQYxLmNPcsZ5DjTF0lQQOX6Qk_9Ik6LHFCfTdpmERrU0GZw1_opt7Umk_Sr_Jd0067nQDu-9bZ8ALeOeRaKq7_-OJ8TGcsynnc0ee6seiIls9PDvOPWPfqsX72J8KZbu9C082BjtMQ7ma5c9chxaM9G7Gr1XzbE-nlPwH6qu93oKymGHumhcW_zngTo_PBFrxGi6CovJeUfb3Uz-wNrsK3ZkrfA8Vh2VyoalThBKwW2P8Op5613VRv9G4ALMc7Moy5PAG0cLgLbwSvRzjJD501jo2vhdv7VPKz7lzFDcpbBMZ9iHFjF7TDbbOgHTYxmrAAAAATbMW4QA'

app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')
  
wwbot = [491459293, 175844556]


@app.on_message(filters.command('join', '!') & filters.me)
def join_game(_, m: Message):
    if len(m.command) == 3:
        chat_id = m.command[1]
        if m.command[2].lower() == 'on':
            if chat_id not in gp:
                gp.append(chat_id)
                m.edit_text('**فعال شد**')
            else:
                m.edit_text('**فعال بود**')
        elif m.command[2].lower() == 'off':
            if chat_id in gp:
                gp.remove(chat_id)
                m.edit_text('**غیرفعال شد**')
            else:
                m.edit_text('**غیرفعال بود**')
        else:
            m.edit_text('**ورودی اشتباس**')
    else:
        m.edit_text('**دستور صحیح ارسال گردد**')


@app.on_message(filters.caption & filters.inline_keyboard)
def doore(app: Client, m: Message):
    if m.from_user.id in wwbot and m.chat.id in gp:
        link = m.reply_markup.inline_keyboard[0][0].url
        link = link.split("=")[1]
        sleep(3)
        app.send_message(175844556, f"/start {link}")


app.run()
