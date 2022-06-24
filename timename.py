from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import threading

api_id = "2669159"
api_hash = "761194071ffe6e596a71e72056a9ae73"

app = Client("time", api_id, api_hash)
timer = False


def job():
    global timer
    t = threading.Timer(30, job)
    if timer:
        jdatetime.set_locale('fa_IR')
        now = jdatetime.datetime.now().strftime('%H:%M')
        font1 = "1234567890"
        font2 = "❶➁➂➃➄６７❽９０"
        now = now.translate(now.maketrans(font1, font2))
        t.start()
        try:app.update_profile(last_name=now)
        except:pass
    else:
        t.cancel()


@app.on_message(filters.command('timer', '!') & filters.me)
def tname(_, message: Message):
    global timer
    if len(message.command) == 2:
        if message.command[1].lower() == 'on':
            if timer:
                message.edit_text('<b>از قبل فعال بود</b>')
            else:
                timer = True
                message.edit_text('<b>فعال شد</b>')
                job()
        elif message.command[1].lower() == 'off':
            if timer:
                timer = False
                app.update_profile(last_name='')
                message.edit_text('<b>غیر فعال شد</b>')
            else:
                app.update_profile(last_name='')
                message.edit_text('<b>غیرفعال بود</b>')
        else:
            message.edit_text('<b>ورودی نامعتبر می باشد</b>')
    else:
        message.edit_text('<b>دستور صحیح نمی باشد</b>')


app.run()