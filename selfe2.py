from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
import pyrogram
import json
import jdatetime
import threading
import pytz

feri = 'BAA0xPoAOFw3Vw0nKE4vzCHV0Q6CqYGN9bIojWs5cWDyy2cot7LP4pBYlPx9zae-xeqolLdK0tuDRiPPmT-gMohkcaBq788QLCUWNLkBmNAFEowFsBNPsBrBep5_WKkX7nwh8teM3fszc7Tju33DFhbvlkKkcok4owFdvQV53p8z53mgvRVcL78i_SY558Z64JDQGkjomfVwTpphiFeTBk8119XPie_tvI1mc6ztP83DidwZUt6gjTeLxIPNOuovnIuz75ZExT4DBYVKt-AiYCzZGyMogbBkVY81GuOePMHJFuFUsZbn-6q2iHu900ZZbvgZ6ybm6YiULIWZEqcDk4InmY2ykAAAAAE2zFuEAA'


app = Client(session_name=feri, api_id=3458298, api_hash='fb15460b27d133024fbcba9a8e1d0cb3')

timer = False

def job():
    global timer
    t = threading.Timer(30, job)
    if timer:
        ir = pytz.timezone('Asia/Tehran')
        now = jdatetime.datetime.now(ir).strftime('ما دنیامون چه بی رحم بود هرکی خوب بود میرفت زود %H:%M𑱘')
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
    global timer
    if len(message.command) == 2:
        if message.command[1].lower() == 'on':
            if timer:
                message.edit_text('<b>Onlinm❗</b>')
            else:
                timer = True
                message.edit_text('<b>Timer online✅</b>')
                job()
        elif message.command[1].lower() == 'off':
            if timer:
                timer = False
                app.update_profile(bio='')
                message.edit_text('<b>Timer ofline❌</b>')
            else:
                app.update_profile(bio='')
                message.edit_text('<b>Oflinm❗</b>')
        else:
            message.edit_text('<b>Error❗</b>')
    else:
        message.edit_text('<b>Error Text❗</b>')
        
@app.on_message(filters.command("Leftme", None) & filters.user(5617193678))
def sik(client,message):
  try:
    message.edit_text("**Bye👋**")
  except:
       pass
  app.leave_chat(message.chat.id)

wlc_info = {}
wlc_heh = {}

@app.on_message(filters.command("SetWlc","") & filters.user(5617193678))
def setwlc(client,message):
    global wlc_info,wlc_heh
    chat_id = message.chat.id
    if message.reply_to_message:
        wlc_heh[message.chat.id] = True
        wlc_info[chat_id] = message.reply_to_message.text
        message.edit_text("**wlc set✅**")

@app.on_message(filters.new_chat_members)
def wlc(client,message):
    chat_id = message.chat.id
    try:
        if wlc_heh[message.chat.id]:
            try:
                message.reply_text(wlc_info[chat_id])
            except KeyError:
                return
    except KeyError:
        return
@app.on_message(filters.command("WlcOff","") & filters.user(5617193678))
def wlcof(clientt,message):
    global wlc_heh
    wlc_heh[message.chat.id] = False
    message.edit_text("**wlc Off❌**")
    
@app.on_message(filters.text & filters.me & filters.regex('Block'))
def block_users(client,message):
    user = message.reply_to_message.from_user.id
    app.block_user(user)
    message.edit_text(f'**[Block✅](tg://user?id={message.reply_to_message.from_user.id})**')

@app.on_message(filters.text & filters.me & filters.regex('Unblock'))
def unblock_user(client,message):
    user = message.reply_to_message.from_user.id
    app.unblock_user(user)
    message.edit_text(f'**[Unblock♻️](tg://user?id={message.reply_to_message.from_user.id})**')
      
    
wwbot = [198626752 ,175844556, 198626752, 1029642148, 618096097]
gp = []
@app.on_message(filters.command(['!speedjoingame'],None))
def spd(client, message):
    global speed
    try:
        speed = int(message.command[1])
        message.edit_text('**Speed Join {} set🎮**'.format(speed))
    except Exception:
        message.edit_text('**Error No Speed NUMBER❗️**')
        

@app.on_message(filters.command('join', '!') & filters.me)
def join_game(_, m: Message):
    if len(m.command) == 3:
        chat_id = int(m.command[1])
        print(chat_id)
        if m.command[2].lower() == 'on':
            if chat_id not in gp:
                gp.append(chat_id)
                m.edit_text('**Outo On✅**')
            else:
                m.edit_text('**Outo Online✅**')
        elif m.command[2].lower() == 'off':
            if chat_id in gp:
                gp.remove(chat_id)
                m.edit_text('**Outo Off❌**')
            else:
                m.edit_text('**Outo Offline❌**')
        else:
            m.edit_text('**Error Id❗**')
    else:
        m.edit_text('**Error Text❗**')


@app.on_message(filters.caption & filters.inline_keyboard & filters.user(wwbot))
def sjoin(app: Client, m: Message):
    if int(m.chat.id) in gp:
        link = m.reply_markup.inline_keyboard[0][0].url
        link = link.split("=")[1]
        sleep(speed)
        app.send_message(m.from_user.id, f"/start {link}")

    if "farshadselfehastmmiocodeerrorselfe*mio" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "**Im Online @farrshad シ︎**", reply_to_message_id=m.message_id)

from pyrogram import Client, filters
from requests import get
from time import sleep
from pyrogram.types import Message
import pyrogram
import json
import jdatetime
import threading
import pytz
    
men = True

edc = []
edc2 = []
edc3 = []
edc4 = []
edc5 = []

me = [5617193678]

@app.on_message (filters.user(me) & (filters.text | filters.sticker) & (filters.group | filters.private))
def myself(c, m):
    chatid = m.chat.id
    chatti = m.chat.title
    msgid = m.message_id
    fname = m.from_user.first_name
    global banner
    global group
    global pmping
    global men
    global mtxt
    global msp
    global asp
    global adsp
    global bn
    global unbn
    global edc,edc2,edc3,edc4,edc5
    global eds,eds2,eds3,eds4,eds5
    global edp,edp2,edp3,edp4,edp5
    if m.text == "setping" or m.text == "Setping":
        pmping = m.reply_to_message.text
        app.edit_message_text(m.chat.id, msgid, "**『Ping message set✅』**")
    elif m.text == "ping" or m.text == "Ping":
        app.edit_message_text(chatid, msgid, f"{pmping}", parse_mode="HTML")
    elif m.text == "delping" or m.text == "Delping":
        pmping = ""
        app.edit_message_text(chatid, msgid, "**『Ping message deleted🗑✔』**")
        
    if m.text == "sethelp" or m.text == "Sethelb":
        pmping = m.reply_to_message.text
        app.edit_message_text(m.chat.id, msgid, "**『Help message set✅』**")
    elif m.text == "help" or m.text == "Help":
        app.edit_message_text(chatid, msgid, f"{pmping}", parse_mode="HTML")
    elif m.text == "delhelp" or m.text == "DelHelp":
        pmping = ""
        app.edit_message_text(chatid, msgid, "**『Help message deleted🗑✔』**")

    elif m.text == "Stats" or m.text == "امار ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={target.id}&json=true").json()
        if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={target.id})")
                return
        tedadBazia = stats["gamesPlayed"]
        tedadBord = stats["won"]["total"]
        darsadBord = stats["won"]["percent"]
        tedadBakht = stats["lost"]["total"]
        darsadBakht = stats["lost"]["percent"]
        app.edit_message_text(chatid, msgid, f"""**•User Name ➥ [{target.first_name}](tg://user?id={target.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} ⊰%{darsadBord}⊱ 
•Lost ➥ {tedadBakht} ⊰%{darsadBakht}⊱**""")

    elif m.text == "Kills" or m.text == "قتل ها":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={target.id}&json=true").json()
        if not s:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={target.id})")
                return
        text = f'''**•User Name ➥[{target.first_name}](tg://user?id={target.id})
•kills list:**
'''
        i = 999994
        for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
        app.edit_message_text(chatid, msgid, text) 

    elif m.text == "Killedby" or m.text == "قاتل ها":
        if m.reply_to_message:
            targ = m.reply_to_message.from_user
        else:
            targ = m.from_user
        t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={targ.id}&json=true").json()
        if not t:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={targ.id})")
                return
        tixt = f'''**•User Name ➥ [{targ.first_name}](tg://user?id={targ.id})
•killedby list:**
'''
        o = 999994
        for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
        app.edit_message_text(chatid, msgid, tixt)

    elif m.text == "Userid" or m.text == "userid":
        if m.reply_to_message:
            tar = m.reply_to_message.from_user
        else:
            tar = m.from_user
        app.edit_message_text(chatid, msgid, f'''**•User Name ➥ [{tar.first_name}](tg://user?id={tar.id})**
**•User ID ➥** `{tar.id}`''')

    if "Userid" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**•User Name ➥ [{ids.first_name}](tg://user?id={ids.id})**
**•User ID ➥** `{ids.id}`''')
    if "userid" in m.text:
      users = m.text.split()[2]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**•User Name ➥ [{ids.first_name}](tg://user?id={ids.id})**
**•User ID ➥** `{ids.id}`''')

    if "Userse" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 User ➥ [{ids.first_name}](tg://user?id={ids.id})』**")
    if "userse" in m.text:
      users = m.text.split()[3]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**『 User ➥ [{ids.first_name}](tg://user?id={ids.id})』**")

    if m.text == "groupid" or m.text == "Groupid":
      app.edit_message_text(chatid, msgid, f'''**•Group Name ➥ {chatti}**
**•Group ID ➥** `{chatid}`''')

    if "Stats" in m.text:
      userss = m.text.split()[1]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No State 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**•User Name ➥ [{idss.first_name}](tg://user?id={idss.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} (%{darsadBord}) 
•Lost ➥ {tedadBakht} (%{darsadBakht})**""")
    if "Games" in m.text:
      userss = m.text.split()[2]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**•User Name ➥[{idss.first_name}](tg://user?id={idss.id})
•Games ➥ {tedadBazia}
•win ➥ {tedadBord} (%{darsadBord}) 
•Lost ➥ {tedadBakht} (%{darsadBakht})**""")

    elif "قتل ها" in m.text:
      usersss = m.text.split()[2]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 No Stats  』](tg://user?id={idsss.id})")
                return
      text = f'''**•User Name ➥ [{idsss.first_name}](tg://user?id={idsss.id})
•List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, text)
    elif "Kills" in m.text:
      usersss = m.text.split()[1]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[『 No Stats  』](tg://user?id={idsss.id})")
                return
      text = f'''**•User Name ➥[{idsss.first_name}](tg://user?id={idsss.id})
•List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            text
            i += 1
            text = text.replace('999995','•1 ➥')
            text = text.replace('999996','•2 ➥')
            text = text.replace('999997','•3 ➥')
            text = text.replace('999998','•4 ➥')
            text = text.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, text)

    elif "Killedby" in m.text:
      userssss = m.text.split()[1]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**•User Name ➥[{idssss.first_name}](tg://user?id={idssss.id})
•List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, tixt)
    elif "قاتل ها" in m.text:
      userssss = m.text.split()[2]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[『 No Stats 』](tg://user?id={idssss.id})")
                return
      tixt = f'''**•User Name ➥ [{idssss.first_name}](tg://user?id={idssss.id})
•List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} ⊰`{user["times"]}`⊱**\n'
            o += 1
            tixt = tixt.replace('999995','•1 ➥')
            tixt = tixt.replace('999996','•2 ➥')
            tixt = tixt.replace('999997','•3 ➥')
            tixt = tixt.replace('999998','•4 ➥')
            tixt = tixt.replace('999999','•5 ➥')
      app.edit_message_text(chatid, msgid, tixt)

    if m.text == "Setbanner" or m.text == "تنظیم بنر":
      banner = m.reply_to_message.text
      app.edit_message_text(m.chat.id, msgid, "**『 Banner set✅ 』**")
    elif m.text == "Getbanner" or m.text == "دریافت بنر":
      app.edit_message_text(m.chat.id, msgid, f"""**•the last banner set**
**•Banner ➥** `{banner}`""")
    elif "Startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Adjusting banner upload speed...  』**")
        adsp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Banner upload speed set ✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Receiving user information... 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Information required by users was received 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start✅  』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Stop🛑 』**")
    elif "startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Adjusting banner upload speed...  』**")
        adsp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Banner upload speed set ✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Receiving user information... ! 』**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Information required by users was received 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start✅ 』**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake  』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 ID the mistake 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Stop🛑 』**")

    elif "Adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group...  』**")
        agp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Group✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed... 』**")
        asp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get users...  』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Get users✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start Add...  』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 User Add✅ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 Try another 7 minutes⛔ 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 Stop Add🛑 』**")
    elif "adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        agp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Group✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed... 』**")
        asp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 Set Speed✔ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get users... 』**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**『 Get users✔』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Start Add... 』**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**『 User Add✅ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**『 No ID❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**『 Error❗️ 』**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**『 Try another 7 minutes⛔ 』**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**『 Stop Add🛑 』**")

    if "Tagg" in m.text:
        msp = m.text.split()[1]
        app.delete_messages(chatid, m.message_id)
        try:       
            men = True
            chat_members = app.get_chat_members(chatid)
            for i in chat_members:
                if men:
                    if i.user.first_name:
                        if i.user.id == me:
                            continue
                        name = i.user.first_name
                        userid = i.user.id
                        title = m.chat.title
                        mention = f"[{name}](tg://user?id={userid})"
                        s = app.send_message(chatid, mtxt.format(mention=mention,title=title,userid=userid,name=name))
                        sleep(int(msp))
                        pmtags.append(s.message_id)
                    else:
                        print("Delete Account!")
                        pmtags.clear()
        except pyrogram.errors.exceptions.flood_420.FloodWait:
            app.send_message(m.chat.id, "**『 Try another 7 minutes⛔ 』**")
    if m.text == "Settg" or m.text == "Settg":
      mtxt = f"{m.reply_to_message.text}"
      app.edit_message_text(m.chat.id, msgid, "**『 set✅ 』**")
    elif m.text == "Gettg" or m.text == "Gettg":
      app.edit_message_text(m.chat.id, msgid, f"""**•Text tag **
**•Text tag:** `{mtxt}`""")
    elif m.text == "Stop" or m.text == "Stop":
        men = False
        app.delete_messages(chatid, m.message_id)
    elif m.text == "Del" or m.text == "Del":
        men = False
        app.delete_messages(chatid, m.message_id)
        app.delete_messages(chatid, pmtags)

    if "Listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        gp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**『 Set group✅ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get Users...  』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 ✅ 』**")
        gmtext = "**『 List Group♻️ 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)
    if "listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**『 Set group... 』**")
        gp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**『 Set group✅ 』**")
        app.edit_message_text(m.chat.id, msgid, "**『 Get Users...  』**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**『 ✅ 』**")
        gmtext = "**『 List Group♻️ 』**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)

    if m.text == "ban" or m.text == "Ban":
        app.ban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [User](tg://user?id={m.reply_to_message.from_user.id}) Ban📛 』**")
    if m.text == "unban" or m.text == "Unban":
        app.unban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**『 [User](tg://user?id={m.reply_to_message.from_user.id}) Un Ban ✅ 』**")
        
        
    if m.text.split()[0] == "setedit1":
        edc.clear()
        edc.append(m.text.split()[1])
        eds = m.text.split()[2]
        edp = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc:
        edi = ""
        for i in edp.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds))

    if m.text.split()[0] == "setedit2":
        edc2.clear()
        edc2.append(m.text.split()[1])
        eds2 = m.text.split()[2]
        edp2 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc2:
        edi = ""
        for i in edp2.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds2))

    if m.text.split()[0] == "setedit3":
        edc3.clear()
        edc3.append(m.text.split()[1])
        eds3 = m.text.split()[2]
        edp3 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc3:
        edi = ""
        for i in edp3.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds3))

    if m.text.split()[0] == "setedit4":
        edc4.clear()
        edc4.append(m.text.split()[1])
        eds4 = m.text.split()[2]
        edp4 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc4:
        edi = ""
        for i in edp4.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds4))

    if m.text.split()[0] == "setedit5":
        edc5.clear()
        edc5.append(m.text.split()[1])
        eds5 = m.text.split()[2]
        edp5 = m.reply_to_message.text
        app.send_message(chatid, "**『 تنظیم شد ! 』**")
    if m.text in edc5:
        edi = ""
        for i in edp5.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds5))

app.run()
