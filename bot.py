from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from resources.secrets import TOKEN
from resources.tt import tt
from datetime import datetime, date
import json

intro = """Hey there! I am the CSLAbot. \nI am a WIP bot. \nSo stay tuned for more features\n send /help to know my features"""

updater = Updater(token=TOKEN, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    user = update.message.from_user
    hello = f"Hello {user['username']}!"
    update.message.reply_text(hello)

def intro(update, context):
	#context.bot.reply_text(chat_id=update.effective_chat.id, text='Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')
    update.message.reply_text(intro)

def timetable(update, context):
    today = datetime.today().strftime("%A")

    text = f"{today}({date.today()})\n\n"
    for period in tt[today]:
        text += tt[today][period]
        text += "\n"

    update.message.reply_text(text)

def help(update , context):
    update.message.reply_text("""
    I am still under dev so I can only do the following features:
    1."/tt" - shows timetable
    2."/who" - shows info about me
    3./hello - self explanatory
    """)

hello_handler = CommandHandler('hello', hello)
intro_handler = CommandHandler('who', intro)
tt_handler = CommandHandler('tt', timetable)
help_handler = CommandHandler('help',help)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(tt_handler)
dispatcher.add_handler(help_handler)


updater.start_polling()