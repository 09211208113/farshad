from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import threading
import pytz

feri = 'BAAA0hRzSXzbsTh_AmCp8dM4hPSBphnTQHIGAlNm1ehbvkzfJuk8purnD9z5scTf_PIvRzhFQX4GRyLgmzHCnq-JA9mFCbVWUgRIvSoGTRgvR-6S_apmX_HnDRiaCwQhsS25I5jllNxDdcdVLQkFLO2fk4M2Jz46O2Q9Ou8hbQu67ZKBFdoKW6fO6dTj5AK7WtZeihwQ2RD1r1XRS9wiDa07A0hmf5mm_5OZwwA2TT6UE8phMjPMp4-Z6K0J27XjOKAJTUIhT8P7_kegxF1oOxAXKLWyzqk5LFpYnBFfk15eMfMJqmqpeelWYkX_gq589KntXdPtJJttizk1zy_M9CE9AAAAATbMW4QA'

app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')

timere = False

def job():
    global timere
    t = threading.Timer(30, job)
    if timere:
        ir = pytz.timezone('Asia/Tehran')
        now = jdatetime.datetime.now(ir).strftime('⸙••𝑩𝒆 𝒃𝒊𝒈 𝒂𝒏𝒅 𝒘𝒂𝒏𝒕 𝒃𝒊𝒈 𝒕𝒉𝒊𝒏𝒈𝒔𑱘 %H:%M')
        font1 = "1234567890"
        font2 = "𝟏𝟐𝟑𝟒𝟓𝟔𝟳𝟖𝟗𝟎"
        now = now.translate(now.maketrans(font1, font2))
        t.start()
        try:app.update_profile(bio=now)
        except:pass
    else:
        t.cancel()


@app.on_message(filters.command('timer', '!') & filters.me)
def tname(_, message: Message):
    global timere
    if len(message.command) == 2:
        if message.command[1].lower() == 'on':
            if timere:
                message.edit_text('<b>Onlinm❗</b>')
            else:
                timere = True
                message.edit_text('<b>Timer online✅</b>')
                job()
        elif message.command[1].lower() == 'off':
            if timere:
                timere = False
                app.update_profile(bio='')
                message.edit_text('<b>Timer ofline❌</b>')
            else:
                app.update_profile(bio='')
                message.edit_text('<b>Oflinm❗</b>')
        else:
            message.edit_text('<b>Error❗</b>')
    else:
        message.edit_text('<b>Error Text❗</b>')
        
        
        
timer = False


def job():
    global timer
    t = threading.Timer(30, job)
    if timer:
        ir = pytz.timezone('Asia/Tehran')
        now = jdatetime.datetime.now(ir).strftime('%H:%M')
        font1 = "1234567890"
        font2 = "❶➁➂➃➄６７❽９０"
        now = now.translate(now.maketrans(font1, font2))
        t.start()
        try:app.update_profile(last_name=now)
        except:pass
    else:
        t.cancel()


@app.on_message(filters.command('timername', '!') & filters.me)
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
