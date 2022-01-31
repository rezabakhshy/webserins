from pyrogram import Client,filters
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5102000083:AAHKoWGuHKriH4Z4_Oc-QwR4tz6IhM2fH68"
app=Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#-------------------------------------------------------------------------------------------------------------
START="""سلام من به تو ای جیگرگوشه بابات 😁\nمن هنوز تازه ساخته شدم و زیاد فضولی نمیکنم\nولی اگه دوس داشته باشی میتونی تو کانالم عضو بشی و دوستاتم عضو کنی تا وقتی موقش برسه شرو به فعالیت کنیم و شما هم لذت ببری \n@learning_programing_language"""
NOTEXIS="""oops..\nyour not joined to my chanel\nplease join and so send /start\nmy chanel: @learning_programing_language"""
EXIS="""WELCOME FRIND.\ni'm moving.\nthanks for start me."""
#-------------------------------------------------------------------------------------------------------------
# def user():
#     file=open("user.txt","w+")
#     f=app.get_chat_members("@learning_programing_language")
#     for member in f:
#         file.write(str(member.user.id))
#         file.write("\n")
#     file.close()

# def fin(user):
#     fil=open("user.txt","r")
#     file=fil.read()
#     exis=file.find(str(user))
#     return exis

# def main(client,message):
#     client.send_message(chat_id=message.chat.id,text=EXIS,reply_to_message_id=message.message_id)

def find_message(text):
    file=open("defult_answer.text","r",encoding="UTF-8")
    for line in file:
        if text in line:
            st=line.find(text)
            s=len(text)
            en=line.find("\n",st)
            tex=line[st+s:en]
            return tex
    return "n"

@app.on_message(filters.command("start","/") & filters.private )
def echo(client, message):
    client.send_message(chat_id=message.chat.id,text=START,reply_to_message_id=message.message_id)
    # chat_id=message.chat.id
    # user()
    # exis=fin(chat_id)
    # if exis==-1:
    #     client.send_message(chat_id=chat_id,text=NOTEXIS,reply_to_message_id=message.message_id)
    # else:
    #     main(client,message)

@app.on_message(filters.group & filters.new_chat_members)
def new_member(client,message):
    name=message.from_user.first_name
    message.reply(f" خوش امدی به جمع ما   [{name}](tg://openmessage?user_id={message.from_user.id})  عزیز \n اینجا قوانین خاصی نداره و از هفت دولت ازادی😁")

@app.on_message(filters.group & filters.regex("رضا"))
def my_creater(client,message):
    message.reply("باشه الان صداش میکنم ببینم کجاس این پدر من😁")
    message.reply(f"[پدر نازنینم](tg://user?id=618260788) انلاین شدی بیا ببین [{message.from_user.first_name}](tg://user?id={message.from_user.id}) صدات کرده چیکار داره")

@app.on_message(filters.group & filters.regex("^(t|T)ag$") &filters.user(618260788))
def tag_all(client,message):
    text=" بیدار شوید و از زیر اب خارج شوید \n همانا خداوند فرمود : زیر ابیان گنهکارند😁 \n"
    members=app.get_chat_members(f"{message.chat.id}")
    for member in members:
        text+=f"[{member.user.first_name}](tg://user?id={member.user.id}) , "
    message.reply(text) 

@app.on_message(filters.group & filters.regex("^(p|P)in$") &filters.user(618260788))
def pin_message(client,message):
    client.pin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
    message.reply("✅")

@app.on_message(filters.group & filters.regex("^(b|B)an$") &filters.user(618260788))
def ban_user(client,message):
    id=message.reply_to_message.from_user.id
    message.chat.kick_member(id)
    message.reply("✅")

@app.on_message(filters.group  & filters.regex("^(a|A)dd ") &filters.user(618260788))
def delete(client,message):
    txt=str(message.text)
    f=txt[:4]
    text=txt.replace(f,"")
    fin=text.find("|")
    mass=text[:fin]
    ans=text[fin+1:]
    # mass=text.split()[0]
    # ans=text.replace(mass,"")
    file=open("defult_answer.text","a",encoding="UTF-8")
    file.write(mass+" "+ans+"\n")
    file.close()
    message.reply("✅")

@app.on_message(filters.group&filters.all)
def defulte_answer(client,message):
    text=message.text
    answer=find_message(text)
    if answer=="n":
        pass
    else:
        message.reply(answer)

app.run()
