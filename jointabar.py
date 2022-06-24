from pyrogram import Client, filters
from pyrogram.types import Message
import jdatetime
import threading


feri = 'AQB-9RF0ZJ8C4BmAJFp3iLtDsN6Of_cplgxexaw2q_Y16m86AlITiw6m6b17ycH3u4Efthva4HC2n8qv-Ky9dCo5goj21uGpMrKidSIXojttYqTjaPIVAasG9EYAXArfojKqBAyOFtHiJlwklTNl0EP5YGZB4ndv1baKtT7_4kJJhmke_QMkpQpOS7Mv9ouNCyuGCPim8lYWMrRAyuW84yFqJdu-00jZl0Og_aOvzKvrnesiR79r3jenzDTw8KzNUIIo6R0Kb7LSS6Dq8rfS-bEjI1LBIKLLdh3CKgoDopa9w2v8o8XVRWWF1SceuvXRzeHPxUJ1oVTqsu9lH2jm2BBAAAAAATs5ToYA'

app = Client(session_name=feri, api_id=13970534, api_hash='b610e73718c72d2e6148124696d72361')
   
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
