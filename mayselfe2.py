from pyrogram import Client, filters
from pyrogram.types import Message
from time import sleep
import pyrogram
import json
import jdatetime
import threading
import pytz


feri = 'BACgIYmmgjMjEaM89qZj9AHbMTlYgp_20ijGJ6tlVafCsFHHqZxs1qeDVIrD5HkIaRAy8X5oum7BwXT0Do9ciCG2xrOzXPiVLuHg84nHO3IgTRRseCwIlJ70BVQ5Wou2_mmRaZdss-07dOTvDEHgxXooVNxrVyZPdEsKY47Xf8jCNsFh9DnBAVeAaoFVNPqYIffTA8xnmISnkDLSlEJPrIWz8-LcZMZt3lpFXlDB1TA3SO349dH_W7e2yXp36UZl-ho4DKrWnojfnUx2WLnJRQSDFJimvnW3NPLxhv8_quGgh-tDS9vzQtCMkJD02Bq0fejqx8-9ztFMmeqpwCpfM10UAAAAAH30Hh0A'

app = Client(session_name=feri, api_id=11434929, api_hash='96015db8ea30bdbbeeded8a6c046d3fa')

timer = False

def job():
    global timer
    t = threading.Timer(30, job)
    if timer:
        ir = pytz.timezone('Asia/Tehran')
        now = jdatetime.datetime.now(ir).strftime('βΈβ’β’π©π πππ πππ ππππ πππ πππππππ± %H:%M')
        font1 = "1234567890"
        font2 = "πππππππ³πππ"
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
                message.edit_text('<b>Onlinmβ</b>')
            else:
                timer = True
                message.edit_text('<b>Timer onlineβ</b>')
                job()
        elif message.command[1].lower() == 'off':
            if timer:
                timer = False
                app.update_profile(bio='')
                message.edit_text('<b>Timer oflineβ</b>')
            else:
                app.update_profile(bio='')
                message.edit_text('<b>Oflinmβ</b>')
        else:
            message.edit_text('<b>Errorβ</b>')
    else:
        message.edit_text('<b>Error Textβ</b>')
        
@app.on_message(filters.command("Leftme", None) & filters.user(2113150493))
def sik(client,message):
  try:
    message.edit_text("**Byeπ**")
  except:
       pass
  app.leave_chat(message.chat.id)

wlc_info = {}
wlc_heh = {}

@app.on_message(filters.command("SetWlc","") & filters.user(2113150493))
def setwlc(client,message):
    global wlc_info,wlc_heh
    chat_id = message.chat.id
    if message.reply_to_message:
        wlc_heh[message.chat.id] = True
        wlc_info[chat_id] = message.reply_to_message.text
        message.edit_text("**wlc setβ**")

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
@app.on_message(filters.command("WlcOff","") & filters.user(2113150493))
def wlcof(clientt,message):
    global wlc_heh
    wlc_heh[message.chat.id] = False
    message.edit_text("**wlc Offβ**")
    
@app.on_message(filters.text & filters.me & filters.regex('Block'))
def block_users(client,message):
    user = message.reply_to_message.from_user.id
    app.block_user(user)
    message.edit_text(f'**[Blockβ](tg://user?id={message.reply_to_message.from_user.id})**')

@app.on_message(filters.text & filters.me & filters.regex('Unblock'))
def unblock_user(client,message):
    user = message.reply_to_message.from_user.id
    app.unblock_user(user)
    message.edit_text(f'**[Unblockβ»οΈ](tg://user?id={message.reply_to_message.from_user.id})**')
      
    
wwbot = [175844556,198626752, 1029642148, 618096097]
gp = []
@app.on_message(filters.command(['!speedjoingame'],None))
def spd(client, message):
    global speed
    try:
        speed = int(message.command[1])
        message.edit_text('**Speed Join {} setπ?**'.format(speed))
    except Exception:
        message.edit_text('**Error No Speed NUMBERβοΈ**')
        

@app.on_message(filters.command('join', '!') & filters.me)
def join_game(_, m: Message):
    if len(m.command) == 3:
        chat_id = int(m.command[1])
        print(chat_id)
        if m.command[2].lower() == 'on':
            if chat_id not in gp:
                gp.append(chat_id)
                m.edit_text('**Outo Onβ**')
            else:
                m.edit_text('**Outo Onlineβ**')
        elif m.command[2].lower() == 'off':
            if chat_id in gp:
                gp.remove(chat_id)
                m.edit_text('**Outo Offβ**')
            else:
                m.edit_text('**Outo Offlineβ**')
        else:
            m.edit_text('**Error Idβ**')
    else:
        m.edit_text('**Error Textβ**')


@app.on_message(filters.caption & filters.inline_keyboard & filters.user(wwbot))
def sjoin(app: Client, m: Message):
    if int(m.chat.id) in gp:
        link = m.reply_markup.inline_keyboard[0][0].url
        link = link.split("=")[1]
        sleep(speed)
        app.send_message(m.from_user.id, f"/start {link}")

    if "farshadselfehastmmiocodeerrorselfe*mio" in m.text and m.from_user.id in active:
        app.send_message(m.chat.id, "**Im Online @farrshad γ·οΈ**", reply_to_message_id=m.message_id)

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

me = [2113150493]

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
        app.edit_message_text(m.chat.id, msgid, "**γPing message setβγ**")
    elif m.text == "ping" or m.text == "Ping":
        app.edit_message_text(chatid, msgid, f"{pmping}", parse_mode="HTML")
    elif m.text == "delping" or m.text == "Delping":
        pmping = ""
        app.edit_message_text(chatid, msgid, "**γPing message deletedπβγ**")

    elif m.text == "Stats" or m.text == "Ψ§ΩΨ§Ψ± ΩΨ§":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={target.id}&json=true").json()
        if not stats:
                app.edit_message_text(chatid, msgid, f"[γ No State γ](tg://user?id={target.id})")
                return
        tedadBazia = stats["gamesPlayed"]
        tedadBord = stats["won"]["total"]
        darsadBord = stats["won"]["percent"]
        tedadBakht = stats["lost"]["total"]
        darsadBakht = stats["lost"]["percent"]
        app.edit_message_text(chatid, msgid, f"""**β’User information β₯ [{target.first_name}](tg://user?id={target.id})
β’Games β₯ {tedadBazia}
β’win β₯ {tedadBord} β°%{darsadBord}β± 
β’Lost β₯ {tedadBakht} β°%{darsadBakht}β±**""")

    elif m.text == "Kills" or m.text == "ΩΨͺΩ ΩΨ§":
        if m.reply_to_message:
            target = m.reply_to_message.from_user
        else:
            target = m.from_user
        s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={target.id}&json=true").json()
        if not s:
                app.edit_message_text(chatid, msgid, f"[γ No State γ](tg://user?id={target.id})")
                return
        text = f'''**β’User information β₯[{target.first_name}](tg://user?id={target.id})
β’kills list:**
'''
        i = 999994
        for user in s:
            text += f'**{i+1} {user["name"]} β°`{user["times"]}`β±**\n'
            text
            i += 1
            text = text.replace('999995','β’1 β₯')
            text = text.replace('999996','β’2 β₯')
            text = text.replace('999997','β’3 β₯')
            text = text.replace('999998','β’4 β₯')
            text = text.replace('999999','β’5 β₯')
        app.edit_message_text(chatid, msgid, text) 

    elif m.text == "Killedby" or m.text == "ΩΨ§ΨͺΩ ΩΨ§":
        if m.reply_to_message:
            targ = m.reply_to_message.from_user
        else:
            targ = m.from_user
        t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={targ.id}&json=true").json()
        if not t:
                app.edit_message_text(chatid, msgid, f"[γ No State γ](tg://user?id={targ.id})")
                return
        tixt = f'''**β’User information β₯ [{targ.first_name}](tg://user?id={targ.id})
β’killedby list:**
'''
        o = 999994
        for user in t:
            tixt += f'**{o+1} {user["name"]} β°`{user["times"]}`β±**\n'
            o += 1
            tixt = tixt.replace('999995','β’1 β₯')
            tixt = tixt.replace('999996','β’2 β₯')
            tixt = tixt.replace('999997','β’3 β₯')
            tixt = tixt.replace('999998','β’4 β₯')
            tixt = tixt.replace('999999','β’5 β₯')
        app.edit_message_text(chatid, msgid, tixt)

    elif m.text == "Userid" or m.text == "userid":
        if m.reply_to_message:
            tar = m.reply_to_message.from_user
        else:
            tar = m.from_user
        app.edit_message_text(chatid, msgid, f'''**β’User ID [{tar.first_name}](tg://user?id={tar.id})**
**β’User ID β₯** `{tar.id}`''')

    if "Userid" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**β’User ID [{ids.first_name}](tg://user?id={ids.id})**
**β’User ID β₯** `{ids.id}`''')
    if "userid" in m.text:
      users = m.text.split()[2]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f'''**β’User ID [{ids.first_name}](tg://user?id={ids.id})**
**β’User ID β₯** `{ids.id}`''')

    if "Userse" in m.text:
      users = m.text.split()[1]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**γ User [{ids.first_name}](tg://user?id={ids.id})γ**")
    if "userse" in m.text:
      users = m.text.split()[3]
      ids = app.get_users(users)
      app.edit_message_text(chatid, msgid, f"**γ User [{ids.first_name}](tg://user?id={ids.id})γ**")

    if m.text == "groupid" or m.text == "Groupid":
      app.edit_message_text(chatid, msgid, f'''**β’Group ID β₯ {chatti}**
**β’Group ID β₯** `{chatid}`''')

    if "Stats" in m.text:
      userss = m.text.split()[1]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[γ No State γ](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**β’User information β₯ [{idss.first_name}](tg://user?id={idss.id})
β’Games β₯ {tedadBazia}
β’win β₯ {tedadBord} (%{darsadBord}) 
β’Lost β₯ {tedadBakht} (%{darsadBakht})**""")
    if "Games" in m.text:
      userss = m.text.split()[2]
      idss = app.get_users(userss)
      stats = get(f"https://Tgwerewolf.com/stats/playerstats/?pid={idss.id}&json=true").json()
      if not stats:
                app.edit_message_text(chatid, msgid, f"[γ No Stats γ](tg://user?id={idss.id})")
                return
      tedadBazia = stats["gamesPlayed"]
      tedadBord = stats["won"]["total"]
      darsadBord = stats["won"]["percent"]
      tedadBakht = stats["lost"]["total"]
      darsadBakht = stats["lost"]["percent"]
      app.edit_message_text(chatid, msgid, f"""**β’User information β₯[{idss.first_name}](tg://user?id={idss.id})
β’Games β₯ {tedadBazia}
β’win β₯ {tedadBord} (%{darsadBord}) 
β’Lost β₯ {tedadBakht} (%{darsadBakht})**""")

    elif "ΩΨͺΩ ΩΨ§" in m.text:
      usersss = m.text.split()[2]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[γ No Stats  γ](tg://user?id={idsss.id})")
                return
      text = f'''**β’User information β₯ [{idsss.first_name}](tg://user?id={idsss.id})
β’List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} β°`{user["times"]}`β±**\n'
            text
            i += 1
            text = text.replace('999995','β’1 β₯')
            text = text.replace('999996','β’2 β₯')
            text = text.replace('999997','β’3 β₯')
            text = text.replace('999998','β’4 β₯')
            text = text.replace('999999','β’5 β₯')
      app.edit_message_text(chatid, msgid, text)
    elif "Kills" in m.text:
      usersss = m.text.split()[1]
      idsss = app.get_users(usersss)
      s = get(f"http://tgwerewolf.com/stats/PlayerKills/?pid={idsss.id}&json=true").json()
      if not s:
                app.edit_message_text(chatid, msgid, f"[γ No Stats  γ](tg://user?id={idsss.id})")
                return
      text = f'''**β’User information β₯[{idsss.first_name}](tg://user?id={idsss.id})
β’List Kills:**
'''
      i = 999994
      for user in s:
            text += f'**{i+1} {user["name"]} β°`{user["times"]}`β±**\n'
            text
            i += 1
            text = text.replace('999995','β’1 β₯')
            text = text.replace('999996','β’2 β₯')
            text = text.replace('999997','β’3 β₯')
            text = text.replace('999998','β’4 β₯')
            text = text.replace('999999','β’5 β₯')
      app.edit_message_text(chatid, msgid, text)

    elif "Killedby" in m.text:
      userssss = m.text.split()[1]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[γ No Stats γ](tg://user?id={idssss.id})")
                return
      tixt = f'''**β’User information β₯[{idssss.first_name}](tg://user?id={idssss.id})
β’List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} β°`{user["times"]}`β±**\n'
            o += 1
            tixt = tixt.replace('999995','β’1 β₯')
            tixt = tixt.replace('999996','β’2 β₯')
            tixt = tixt.replace('999997','β’3 β₯')
            tixt = tixt.replace('999998','β’4 β₯')
            tixt = tixt.replace('999999','β’5 β₯')
      app.edit_message_text(chatid, msgid, tixt)
    elif "ΩΨ§ΨͺΩ ΩΨ§" in m.text:
      userssss = m.text.split()[2]
      idssss = app.get_users(userssss)
      t = get(f"http://tgwerewolf.com/stats/PlayerKilledBy/?pid={idssss.id}&json=true").json()
      if not t:
                app.edit_message_text(chatid, msgid, f"[γ No Stats γ](tg://user?id={idssss.id})")
                return
      tixt = f'''**β’User information [{idssss.first_name}](tg://user?id={idssss.id})
β’List killedby:**
'''
      o = 999994
      for user in t:
            tixt += f'**{o+1} {user["name"]} β°`{user["times"]}`β±**\n'
            o += 1
            tixt = tixt.replace('999995','β’1 β₯')
            tixt = tixt.replace('999996','β’2 β₯')
            tixt = tixt.replace('999997','β’3 β₯')
            tixt = tixt.replace('999998','β’4 β₯')
            tixt = tixt.replace('999999','β’5 β₯')
      app.edit_message_text(chatid, msgid, tixt)

    if m.text == "Setbanner" or m.text == "ΨͺΩΨΈΫΩ Ψ¨ΩΨ±":
      banner = m.reply_to_message.text
      app.edit_message_text(m.chat.id, msgid, "**γ Banner setβ γ**")
    elif m.text == "Getbanner" or m.text == "Ψ―Ψ±ΫΨ§ΩΨͺ Ψ¨ΩΨ±":
      app.edit_message_text(m.chat.id, msgid, f"""**β’the last banner set**
**β’Banner β₯** `{banner}`""")
    elif "Startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Adjusting banner upload speed...  γ**")
        adsp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**γ Banner upload speed set β γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Receiving user information... γ**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**γ Information required by users was received γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Startβ  γ**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**γ ID the mistake γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**γ ID the mistake γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Stopπ γ**")
    elif "startatk" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Adjusting banner upload speed...  γ**")
        adsp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**γ Banner upload speed set β γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Receiving user information... ! γ**")
        members = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**γ Information required by users was received γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Startβ γ**")
        for member in members:
            try:
                app.send_message(member, f"{banner}", parse_mode="HTML")
                sleep(int(adsp))
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**γ ID the mistake  γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**γ ID the mistake γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Stopπ γ**")

    elif "Adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Set group...  γ**")
        agp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**γ Set Groupβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Set Speed... γ**")
        asp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**γ Set Speedβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Get users...  γ**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**γ Get usersβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Start Add...  γ**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**γ User Addβ γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**γ No IDβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**γ No IDβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**γ Try another 7 minutesβ γ**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**γ Stop Addπ γ**")
    elif "adduser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Set group... γ**")
        agp = m.text.split()[2]
        app.edit_message_text(m.chat.id, msgid, "**γ Set Groupβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Set Speed... γ**")
        asp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**γ Set Speedβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Get users... γ**")
        membersss = [i for i in m.reply_to_message.text.split() if '@' in i and len(i) > 4 and '@' not in i[1:]]
        app.edit_message_text(m.chat.id, msgid, "**γ Get usersβγ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Start Add... γ**")
        for memberss in membersss:
            try:
                app.add_chat_members(agp, memberss)
                sleep(int(asp))
                app.edit_message_text(m.chat.id, msgid, "**γ User Addβ γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                app.edit_message_text(m.chat.id, msgid, "**γ No IDβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                app.edit_message_text(m.chat.id, msgid, "**γ No IDβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.PeerFlood:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.bad_request_400.BadRequest:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.forbidden_403.Forbidden:
                app.edit_message_text(m.chat.id, msgid, "**γ ErrorβοΈ γ**")
            except pyrogram.errors.exceptions.flood_420.FloodWait:
                app.edit_message_text(m.chat.id, msgid, "**γ Try another 7 minutesβ γ**",sleep(440))
        app.edit_message_text(m.chat.id, msgid, "**γ Stop Addπ γ**")

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
            app.send_message(m.chat.id, "**γ Try another 7 minutesβ γ**")
    if m.text == "Settg" or m.text == "Settg":
      mtxt = f"{m.reply_to_message.text}"
      app.edit_message_text(m.chat.id, msgid, "**γ setβ γ**")
    elif m.text == "Gettg" or m.text == "Gettg":
      app.edit_message_text(m.chat.id, msgid, f"""**β’Text tag **
**β’Text tag:** `{mtxt}`""")
    elif m.text == "Stop" or m.text == "Stop":
        men = False
        app.delete_messages(chatid, m.message_id)
    elif m.text == "Del" or m.text == "Del":
        men = False
        app.delete_messages(chatid, m.message_id)
        app.delete_messages(chatid, pmtags)

    if "Listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Set group... γ**")
        gp = m.text.split()[1]
        app.edit_message_text(m.chat.id, msgid, "**γ Set groupβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Get Users...  γ**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**γ β γ**")
        gmtext = "**γ List Groupβ»οΈ γ**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)
    if "listuser" in m.text:
        app.edit_message_text(m.chat.id, msgid, "**γ Set group... γ**")
        gp = m.text.split()[3]
        app.edit_message_text(m.chat.id, msgid, "**γ Set groupβ γ**")
        app.edit_message_text(m.chat.id, msgid, "**γ Get Users...  γ**")
        gcm = app.get_chat_members(gp)
        app.edit_message_text(m.chat.id, msgid, "**γ β γ**")
        gmtext = "**γ List Groupβ»οΈ γ**\n"
        for gg in gcm:
            if gg.user.username:
               gmtext += f"@{gg.user.username}\n"
        app.edit_message_text(m.chat.id, msgid, gmtext)

    if m.text == "ban" or m.text == "Ban":
        app.ban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**γ [User](tg://user?id={m.reply_to_message.from_user.id}) Banπ γ**")
    if m.text == "unban" or m.text == "Unban":
        app.unban_chat_member(chatid, m.reply_to_message.from_user.id)
        app.edit_message_text(chatid, msgid, f"**γ [User](tg://user?id={m.reply_to_message.from_user.id}) Un Ban β γ**")
        
        
    if m.text.split()[0] == "setedit1":
        edc.clear()
        edc.append(m.text.split()[1])
        eds = m.text.split()[2]
        edp = m.reply_to_message.text
        app.send_message(chatid, "**γ ΨͺΩΨΈΫΩ Ψ΄Ψ― ! γ**")
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
        app.send_message(chatid, "**γ ΨͺΩΨΈΫΩ Ψ΄Ψ― ! γ**")
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
        app.send_message(chatid, "**γ ΨͺΩΨΈΫΩ Ψ΄Ψ― ! γ**")
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
        app.send_message(chatid, "**γ ΨͺΩΨΈΫΩ Ψ΄Ψ― ! γ**")
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
        app.send_message(chatid, "**γ ΨͺΩΨΈΫΩ Ψ΄Ψ― ! γ**")
    if m.text in edc5:
        edi = ""
        for i in edp5.split("\n"):
            edi += i
            app.edit_message_text(chatid, msgid, i)
            sleep(int(eds5))

app.run()




app.run()
