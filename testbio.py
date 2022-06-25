from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import threading
import pytz

feri = 'AQB-9RF0ZJ8C4BmAJFp3iLtDsN6Of_cplgxexaw2q_Y16m86AlITiw6m6b17ycH3u4Efthva4HC2n8qv-Ky9dCo5goj21uGpMrKidSIXojttYqTjaPIVAasG9EYAXArfojKqBAyOFtHiJlwklTNl0EP5YGZB4ndv1baKtT7_4kJJhmke_QMkpQpOS7Mv9ouNCyuGCPim8lYWMrRAyuW84yFqJdu-00jZl0Og_aOvzKvrnesiR79r3jenzDTw8KzNUIIo6R0Kb7LSS6Dq8rfS-bEjI1LBIKLLdh3CKgoDopa9w2v8o8XVRWWF1SceuvXRzeHPxUJ1oVTqsu9lH2jm2BBAAAAAATs5ToYA'

app = Client(session_name=feri, api_id=13970534, api_hash='b610e73718c72d2e6148124696d72361')
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
        try:app.update_profile(last_name=now)    
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
