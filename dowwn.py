from pyrogram import Client,filters
from pyrogram.types import*
import os,pyminizip,random,time
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5102000083:AAHKoWGuHKriH4Z4_Oc-QwR4tz6IhM2fH68"
app=Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#-------------------------------------------------------------------------------------------------------------
START="""
سلام سلام \nخوش اومدی \n😍من hero هستم\nاگه میخای با قابلیت های من اشنا بشی منو تو گروهت ادد و بعد از اون ادمینم کن😍😎\nبزن بریم🏃🏻‍♂️ \n@learning_programing_language"""
NOTEXIS="""oops..\nyour not joined to my chanel\nplease join and so send /start\nmy chanel: @learning_programing_language"""
EXIS="""WELCOME FRIND.\ni'm moving.\nthanks for start me."""
PANEL="""😑🤦🏻تو که میدونی پنلی برام ننوشتی چرا هعی پنل پنل میکنی؟\n🥲حالا دلت و نمیشکنم بیا یه لیست کوچولو بدمت که میتونم انجام بدم \n**🔠✅ادد کردن کلمه برای پاسخگویی از طرف خود ربات با دستور :**\n-> tadd (kalame)|(javab)\n-> Tadd (kalame)|(javab)\n**☃️ادد کردن استیکر برای پاسخ گویی از طرف ربات:**\nریپلی کردن استیکر و سپس تایپ این دو دستور\n->sadd\n->Sadd\n**📝📘لیست استیکر هایی که برای پاسخ گویی دارم و نشون میدم به دستور سازنده📝📘**\n\n**📝📘لیست کلمه هایی که یاد دارم و نشون میدم به دستور سازنده📝📘**\n**🗑حذف پیام ها به دستور پدرم🗑**\n**🆔تگ کاربران توسط سازنده🆔**\n**❌⛔️بن کاربران توسط سازنده❌⛔️**\n**🧷📌سنجاق کردن پیام توسط سازنده🧷📌**\n\n**🧷📌برداشتن پیام سنجاق شده توسط سازنده🧷📌**\n**♥️♦️خوشامد گویی به دوستان تازه وارد♥️♦️**\n**🙆🏻‍♂️فعلا همیناس ولی پدرم داره رشدم میده و در اینده نزدیک کاملم میکنه🙆🏻‍♂️**"""
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
#     return exis-

# def main(client,message):
#     client.send_message(chat_id=message.chat.id,text=EXIS,reply_to_message_id=message.message_id)

def find_message(text):
    list=[]
    file=open("defult_answer.text","r",encoding="UTF-8")
    for line in file:
        st=line.find(text)
        s=line.find("|")
        te=line[:s]
        if text == te:
            en=line.find("\n",st)
            list.append(line[s+1:en])
    file.close()
    size=len(list)
    if size!=0:
        rand=random.randint(0,size-1)
        return list[rand]
    else:
        return "n"

def list_file(message):
    pyminizip.compress("defult_answer.text",None,"list_word.zip","reza0021",1)
    message.reply_document("list_word.zip")
    os.remove("list_word.zip")

def del_anderline():
    file=open("defult_answer.text","r",encoding="UTF-8")
    text=""
    for line in file:
        fin=line.find("|")
        kalam=line[:fin]
        kalame=""
        for i in kalam:
            if i!="_":
                kalame+=i
            else:
                kalame+=" "
        javab=line[fin+1:]
        javabe=""
        for i in javab:
            if i!="_":
                javabe+=i
            else:
                javabe+=" "
        text+=f"📝📘**kalame:** {kalame}\n->{javabe}\n---------------------------------\n"
    file.close()
    return text

def imogis(imogi):
    file=open("sticker.txt","r",encoding="UTF-8")
    list=[]
    for line in file:
        if imogi in line:
            img=line[2:]
            img=img.replace("\n","")
            list.append(img)
    size=len(list)
    if size==0:
        return "n"
    else:
        rand=random.randint(0,size-1)
        return list[rand]

@app.on_message(filters.group & filters.sticker)
def ech_sticker(client,message):
    stic=imogis(message.sticker.emoji)
    if stic!="n":
        message.reply_sticker(stic)

@app.on_message(filters.group & filters.regex("^(s|S)add$"))
def add_sticker(client,message):
    if message.reply_to_message.sticker:
        file=open("sticker.txt","a",encoding="UTF-8")
        id=message.reply_to_message.sticker.file_id
        imogi=message.reply_to_message.sticker.emoji
        file.write(imogi+"|"+str(id)+"\n")
        file.close()
        message.reply("✅")


@app.on_message(filters.user(618260788) & filters.regex("^(l|L)ists$"))
def add_sticker(client,message):
    pyminizip.compress("sticker.txt",None,"list_sticker.zip","reza0021",1)
    message.reply_document("list_sticker.zip")
    os.remove("list_sticker.zip")

@app.on_message(filters.user(618260788) & filters.regex("^(d|D)el "))
def delete_message(client,message):
    message_id=message.message_id
    chat_id=message.chat.id
    count=message.text[4:]
    if count=="all":
        count=message_id
    list_id=[]
    for i in range(int(message_id-1),int(message_id-1)-int(count),-1):
        list_id.append(i)
    client.delete_messages(chat_id,list_id)
    message.reply("✅")

@app.on_message(filters.command("start","/") & filters.private )
def main(client, message):
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
    name=str(message.new_chat_members)
    fin_name=name.find("first_name")
    fon_name=name.find(",",fin_name)
    na=name[fin_name+11:fon_name]
    na=na.replace("'","")
    fin_id=name.find("id")
    fon_id=name.find(",",fin_id)
    id=name[fin_id+3:fon_id]
    id=id.replace("'","")
    message.reply(f" سلام \nخوش اومدی [{na}](tg://user?id={int(id)})\nاز قوانین گروه پیروی کن تا مدیر ناراحت نشه😁")

@app.on_message(filters.group & filters.left_chat_member)
def left_member(client,message):
    message.reply("به درودی یا حق")
@app.on_message(filters.group & filters.regex("^(t|T)ag$") &filters.user(618260788))
def tag_all(client,message):
    list=[" بیدار شوید و از زیر اب خارج شوید \n همانا خداوند فرمود : زیر ابیان گنهکارند😁 \n","تو را به سمفونی شماره پنج بتهوون قسم بیا ببین این چی میگه"]
    list.append("الو \nالو الو خدا\nحاجی کجاعن اینا 😂😂")
    list.append("قال مدیر(ع):\nای کسانی که فعال نیستید بدانید که مدیر اگاه است \nایا برای شما گروه نساخته ایم؟")
    list.append("مدیر(ع)فرمود:\nای کسانی که فعال نیستید ایا ما شما را به این گروه دعوت نکرده ایم ؟\nایا در کنارتان ده ها نفر حوری نگذاشته ایم تا عاشق شوید؟😂")
    list.append("قال مدیر(ع):\nوای بر انان که فعال نیستند \nبترسید از روزی که اخراج شوید😒")
    text=""
    tex=list[random.randint(0,len(list)-1)]
    members=app.get_chat_members(f"{message.chat.id}")
    for member in members:
        text+=f"{tex}\n[{member.user.first_name}](tg://user?id={member.user.id}) , "
    message.reply(text) 

# @app.on_message(filters.group & filters.regex("^(s|S)ilent ") &filters.user(618260788))
# def ChatPermis(client,message):
#     if message.reply_to_message:
#         tim=str(message.text)[7:]
#         id=message.reply_to_message.from_user.id
#         client.restrict_chat_member(message.chat.id,id,ChatPermissions(),int(time()+(60*tim)))
#     else:
#         text=str(message.text)[7:]
#         id=text.split()[0]
#         tim=text.replace(id,"")
#         client.restrict_chat_member(message.chat.id,id,ChatPermissions(),int(time()+(30*tim)))
#     message.reply("✅")

@app.on_message(filters.group & filters.regex("^(p|P)in$") &filters.user(618260788))
def pin_message(client,message):
    client.pin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
    message.reply("✅")

@app.on_message(filters.group & filters.regex("^(u|U)npin$") &filters.user(618260788))
def unpin_message(client,message):
    client.unpin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
    message.reply("✅")
    
@app.on_message(filters.group & filters.regex("^(b|B)an$") &filters.user(618260788))
def ban_user(client,message):
    id=message.reply_to_message.from_user.id
    message.chat.kick_member(id)
    message.reply("✅")

@app.on_message(filters.group  & filters.regex("^(p|P)anel$")&filters.user(618260788))
def panel(client,message):
    message.reply(PANEL)


@app.on_message(filters.group  & filters.regex("^(t|T)add "))
def add_text(client,message):
    txt=str(message.text)
    f=txt[:5]
    text=txt.replace(f,"")
    tx=""
    for i in text:
        if i!=" ":
            tx+=i
        else:
            tx+="_"
    # mass=text.split()[0]
    # ans=text.replace(mass,"")
    file=open("defult_answer.text","a",encoding="UTF-8")
    file.write(tx+"\n")
    file.close()
    message.reply("ممنونم ازت دوست عزیزم که بهم کلمه یاد میدیی😍😍❤️")

@app.on_message(filters.group&filters.regex("^(l|L)ist$")&filters.user(618260788))
def list_kalamat(client,message):
    list_file(message)
    text=del_anderline()
    if len(text)<=4096:
        message.reply(text)
    else:
        ffile=open("list_word.txt","a",encoding="UTF-8")
        ffile.write(text)
        message.reply_document("list_word.txt")
        ffile.close()
        os.remove("list_word.txt")

@app.on_message(filters.group&filters.text)
def defulte_answer(client,message):
    text=message.text
    kalame=""
    for i in text:
        if i!=" ":
            kalame+=i
        else:
            kalame+="_"
    answer=find_message(kalame)
    ans=""
    for i in answer:
        if i!="_":
            ans+=i
        else:
            ans+=" "
    if answer=="n":
        pass
    else:
        message.reply(ans)

app.run()
