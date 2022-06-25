from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import threading
import pytz

feri = 'BAAA0hRzSXzbsTh_AmCp8dM4hPSBphnTQHIGAlNm1ehbvkzfJuk8purnD9z5scTf_PIvRzhFQX4GRyLgmzHCnq-JA9mFCbVWUgRIvSoGTRgvR-6S_apmX_HnDRiaCwQhsS25I5jllNxDdcdVLQkFLO2fk4M2Jz46O2Q9Ou8hbQu67ZKBFdoKW6fO6dTj5AK7WtZeihwQ2RD1r1XRS9wiDa07A0hmf5mm_5OZwwA2TT6UE8phMjPMp4-Z6K0J27XjOKAJTUIhT8P7_kegxF1oOxAXKLWyzqk5LFpYnBFfk15eMfMJqmqpeelWYkX_gq589KntXdPtJJttizk1zy_M9CE9AAAAATbMW4QA'

app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')
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
        if mybio is not None:
            app.update_profile(bio=my_bio) 
        else:
            app.update_profile(bio=now)
    else:
        t.cancel()


@app.on_message(filters.command('time_bio') & filters.me)
def time_in_bio(client, message):
    global timer, last_bio
    mybio = app.get_chat(message.from_user.id).bio
    if len(message.command) == 2:
        if message.command[1].lower() == 'on':
            if timer:
                message.edit_text('فعال بود')
            else:
                timer = True
                last_bio = mybio
                job(mybio)
                message.edit_text('ok')
        if message.command[1].lower() == 'off':
            if timer:
                timer = False
                app.update_profile(bio=last_bio)
                message.edit_text('ok')
            else:
                message.edit_text('غیر فعال بود')
app.run()
app.run()
