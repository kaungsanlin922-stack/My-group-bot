import telebot
import random

# မိမိ Bot Token ကို ဤနေရာတွင် အစားထိုးပါ
TOKEN = '8648085262:AAEguk_mD7zmaYCTNFImS9qAjNRkvOvGkE0'
bot = telebot.TeleBot(TOKEN)

# ၁။ Member အသစ်ဝင်လာလျှင် နှုတ်ဆက်ရန်
@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for member in message.new_chat_members:
        replies = [
            f"မင်္ဂလာပါ {member.first_name} ရေ...Group ထဲ ကြိုဆိုပါတယ်ဗျာ။ စကားတွေ အများကြီး လာပြောနော်! 🥳",
            f"ဟော... {member.first_name} တော့ ရောက်လာပြီ။ မပျင်းရအောင် အားလုံး ဝိုင်းနှုတ်ဆက်လိုက်ကြဦး။ 😎"
        ]
        bot.reply_to(message, random.choice(replies))

# ၂။ Member များ မပျင်းရအောင် စာသားအလိုက် အလိုအလျောက် ပြန်ရန်
@bot.message_handler(func=lambda message: True)
def reply_to_members(message):
    text = message.text.lower()
    
    if "ပျင်းတယ်" in text:
        replies = [
            "မပျင်းနဲ့လေ... သီချင်းဆိုပြရမလား? ဒါမှမဟုတ် ဂိမ်းဆော့မလား? 🤪",
            "ပျင်းရင်လည်း အိပ်လိုက်တော့လေနော်... ဟီးးး 😴",
            "မပျင်းနဲ့လာလို့ပေး! 💬"
        ]
        bot.reply_to(message, random.choice(replies))
        
    elif "လွမ်းတယ်" in text:
        bot.reply_to(message, "ဘယ်သူ့ကို လွမ်းနေတာလဲဟင်... 👀 အဖွဲ့ထဲက တစ်ယောက်ယောက်ကိုလား?")

    elif "ဟိုင်း" in text or "hi" in text:
        bot.reply_to(message, f"ဟိုင်း... {message.from_user.first_name}! စားပြီးပြီလား ဘာလုပ်နေလဲ?")

# Bot ကို စတင်ပတ်မည့် Command
bot.infinity_polling()
