from pyrogram import Client,filters
import os,pyminizip
api_id=13893053
api_hash="f586d92837b0f6eebcaa3e392397f47c"
bot_token="5102000083:AAHKoWGuHKriH4Z4_Oc-QwR4tz6IhM2fH68"
app=Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
#-------------------------------------------------------------------------------------------------------------
START="""سلام من به تو ای جیگرگوشه بابات 😁\nمن هنوز تازه ساخته شدم و زیاد فضولی نمیکنم\nولی اگه دوس داشته باشی میتونی تو کانالم عضو بشی و دوستاتم عضو کنی تا وقتی موقش برسه شرو به فعالیت کنیم و شما هم لذت ببری \n@learning_programing_language"""
NOTEXIS="""oops..\nyour not joined to my chanel\nplease join and so send /start\nmy chanel: @learning_programing_language"""
EXIS="""WELCOME FRIND.\ni'm moving.\nthanks for start me."""
PANEL="""😑🤦🏻تو که میدونی پنلی برام ننوشتی چرا هعی پنل پنل میکنی؟\n🥲حالا دلت و نمیشکنم بیا یه لیست کوچولو بدمت که میتونم انجام بدم \n**🔠✅ادد کردن کلمه برای پاسخگویی از طرف خود ربات با دستور :**\n-> add (kalame)|(javab)\n-> Add (kalame)|(javab)\n**📝📘لیست کلمه هایی که یاد دارم و نشون میدم به دستور سازنده📝📘**\n**💟ری اکشن میدم به کلمات و جملات خاص💟**\n**🗑حذف پیام ها به دستور پدرم🗑**\n**🆔تگ کاربران توسط سازنده🆔**\n**❌⛔️بن کاربران توسط سازنده❌⛔️**\n**🧷📌سنجاق کردن پیام توسط سازنده🧷📌**\n**♥️♦️خوشامد گویی به دوستان تازه وارد♥️♦️**\n**🙆🏻‍♂️فعلا همیناس ولی پدرم داره رشدم میده و در اینده نزدیک کاملم میکنه🙆🏻‍♂️**"""
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

async def find_message(text):
    file=open("defult_answer.text","r",encoding="UTF-8")
    for line in file:
        st=line.find(text)
        s=line.find("|")
        te=line[:s]
        if text == te:
            en=line.find("\n",st)
            tex=line[s+1:en]
            return tex
    return "n"
@app.on_message(filters.user(618260788) & filters.regex("^(d|D)el "))
async def delete_message(client,message):
    message_id=message.message_id
    chat_id=message.chat.id
    count=message.text[4:]
    if count=="all":
        count=message_id
    list_id=[]
    for i in range(int(message_id-1),int(message_id-1)-int(count),-1):
        list_id.append(i)
    client.delete_messages(chat_id,list_id)
    await message.reply("✅")

@app.on_message((filters.regex("لایک") | filters.regex("دوس") | filters.regex("عالیه") | filters.regex("حق") | filters.regex("👍")))
async def like(client,message):
    await message.reply("👍")

@app.on_message((filters.regex("نموخام") | filters.regex("مزخرف")  | filters.regex("👎")))
async def not_like(client,message):
    await message.reply("👎")

@app.on_message((filters.regex("عشق") | filters.regex("عاشق") | filters.regex("زندگیمی") | filters.regex("فداتشم") | filters.regex("❤️")))
async def love(client,message):
    await message.reply("❤️")

@app.on_message((filters.regex("هورا") | filters.regex("جشن") | filters.regex("مبارک") | filters.regex("🎉")))
async def hoppy(client,message):
    await message.reply("🎉")

@app.on_message((filters.regex("ریدم")| filters.regex("تف") | filters.regex("گوه") | filters.regex("💩")))
async def goh(client,message):
    await message.reply("💩")

@app.on_message((filters.regex("شیطون") | filters.regex("شیطونی") | filters.regex("😁")))
async def lusifer(client,message):
    await message.reply("😁")

@app.on_message((filters.regex("جووون") | filters.regex("خوشکله") | filters.regex("زیبا") | filters.regex("🤩")))
async def biutiful(client,message):
    await message.reply("🤩")

@app.on_message((filters.regex("اتیش") | filters.regex("اتیشپاره") | filters.regex("بخورمت") | filters.regex("اتیشی") | filters.regex("🔥")))
async def fire(client,message):
    await message.reply("🔥")

@app.on_message((filters.regex("مشکل") | filters.regex("نکن") | filters.regex("عجیبه") | filters.regex("😱")))
async def amazing(client,message):
    await message.reply("😱")

@app.on_message((filters.regex("مخم ترکید") | filters.regex("این چی بود") | filters.regex("وای خدا") | filters.regex("🤯")))
async def amazing(client,message):
    await message.reply("🤯")

@app.on_message((filters.regex("تشویق") | filters.regex("تکبیر") | filters.regex("افرین") | filters.regex("👏🏻")))
async def amazing(client,message):
    await message.reply("👏🏻")

@app.on_message((filters.regex("فوش") | filters.regex("چرت") | filters.regex("دعوا") | filters.regex("🤬")))
async def amazing(client,message):
    await message.reply("🤬")

@app.on_message((filters.regex("ببخشید") | filters.regex("ببشید") | filters.regex("اشتی") | filters.regex("😢")))
async def amazing(client,message):
    await message.reply("😢")

@app.on_message((filters.regex("حالم بهم خورد") | filters.regex("چه زشت") | filters.regex("حالت تهوع") | filters.regex("🤮")))
async def amazing(client,message):
    await message.reply("🤮")

@app.on_message(filters.command("start","/") & filters.private )
async def main(client, message):
    await client.send_message(chat_id=message.chat.id,text=START,reply_to_message_id=message.message_id)
    # chat_id=message.chat.id
    # user()
    # exis=fin(chat_id)
    # if exis==-1:
    #     client.send_message(chat_id=chat_id,text=NOTEXIS,reply_to_message_id=message.message_id)
    # else:
    #     main(client,message)

@app.on_message(filters.group & filters.new_chat_members)
async def new_member(client,message):
    name=message.from_user.first_name
    await message.reply(f" خوش امدی به جمع ما   [{name}](tg://openmessage?user_id={message.from_user.id})  عزیز \n اینجا قوانین خاصی نداره و از هفت دولت ازادی😁")

@app.on_message(filters.group & filters.regex("رضا"))
async def my_creater(client,message):
    await message.reply("باشه الان صداش میکنم ببینم کجاس این پدر من😁")
    await message.reply(f"[پدر نازنینم](tg://user?id=618260788) انلاین شدی بیا ببین [{message.from_user.first_name}](tg://user?id={message.from_user.id}) صدات کرده چیکار داره")

@app.on_message(filters.group & filters.regex("^(t|T)ag$") &filters.user(618260788))
async def tag_all(client,message):
    text=" بیدار شوید و از زیر اب خارج شوید \n همانا خداوند فرمود : زیر ابیان گنهکارند😁 \n"
    members=app.get_chat_members(f"{message.chat.id}")
    for member in members:
        text+=f"[{member.user.first_name}](tg://user?id={member.user.id}) , "
    await message.reply(text) 

@app.on_message(filters.group & filters.regex("^(p|P)in$") &filters.user(618260788))
async def pin_message(client,message):
    await client.pin_chat_message(chat_id=message.chat.id,message_id=message.reply_to_message.message_id)
    await message.reply("✅")

@app.on_message(filters.group & filters.regex("^(b|B)an$") &filters.user(618260788))
async def ban_user(client,message):
    id=message.reply_to_message.from_user.id
    await message.chat.kick_member(id)
    await message.reply("✅")

@app.on_message(filters.group  & filters.regex("^(p|P)anel$")&filters.user(618260788))
async def panel(client,message):
    await message.reply(PANEL)


@app.on_message(filters.group  & filters.regex("^(a|A)dd "))
async def add_text(client,message):
    txt=str(message.text)
    f=txt[:4]
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
    await message.reply("ممنونم ازت دوست عزیزم که بهم کلمه یاد میدیی😍😍❤️")

@app.on_message(filters.group&filters.regex("^(l|L)ist$")&filters.user(618260788))
async def list_kalamat(client,message):
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
    if len(text)<=4096:
        await message.reply(text)
    else:
        ffile=open("list_word.txt","a",encoding="UTF-8")
        ffile.write(text)
        pyminizip.compress("list_word.txt",None,"list_word.zip","reza0021",1)
        await message.reply_document("list_word.zip")
        ffile.close()
        await os.remove("list_word.txt")
        await os.remove("list_word.zip")

@app.on_message(filters.group&filters.text)
async def defulte_answer(client,message):
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
        await message.reply(ans)

app.run()
