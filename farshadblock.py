from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
feri = 'BAABiGqB8Z6nxt8HVgA-qR9hGNjebFp7Y6dHk5E5uzQL0utMRhxVGKoCwNPHNzZWGVCRDaAcx7LHptt7eW1jCRiNzVJghLrZeVMaLa-yQAbuG7wnFxWZKFEUouZ6QQtR5T0Xukn611revv5cZ3V0cQuxCtyMga95M5M20chuq4Wd48bGkTe_ieR4O1tgzUv3NCMTSqGxTbEsQsOsSoJdmrCVSmLirlsVrWuewPYg7U2o2gJC2oducVW126cXT0PH4usZPZUtYslA9mLFl9AWn26Pa10prl1ppxAeLJV92y3oyWKTwq1e732k-WmvUnoJnAz1MUAflnr6ZqJdnPBtjXSbAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')
  
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
