from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BAC2WUezDaB-CR63VY8xPKqRIFOVCR1LPTuLm7hxi2UMajFIvb3IlTNnJhZPtubtK8s5urXxlQ00qavoayF1yAXSIJ_3SL8SCZkLXA5oE9I8M5k2V3PcivjinEWAZgdcFgCmfdprNfKBPSfldoLhYIlLB6Ilq5urxuD-tEEwr-QE9dAT3UJA6ka70-JxN5eWqIYJQd-ZtxaXH9qpkYeJptygMUjGgE474GctsupS5SMYr0hVa3TDuk7W2Ex2sJfATsKKFxt4CWlgopy1q1e1JihNk-7kVUTq0peY4jyxkmjUPUdfNkxfk1yqKjgkuXFHBse_H0R5KU8XbAXtvg6fFVrCAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')
  
wwbot = [491459293, 175844556]
gp = []


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
