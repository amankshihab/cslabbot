from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from resources.secrets import TOKEN
from resources.tt import tt
from datetime import datetime, date
import json

#intro = 'Hey there! I am the CSLAbot. I am WIP bot. So wait for further features'

updater = Updater(token=TOKEN, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    update.message.reply_text('Hello World')

def intro(update, context):
	#context.bot.reply_text(chat_id=update.effective_chat.id, text='Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')
    update.message.reply_text('Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')

def timetable(update, context):
    today = datetime.today().strftime("%A")

    text = f"**{today}({date.today()})**\n\n"
    for period in tt[today]:
        text += "__"
        text += tt[today][period]
        text += "__"
        text += "\n"

    update.message.reply_text(text)

hello_handler = CommandHandler('hello', hello)
intro_handler = CommandHandler('who', intro)
tt_handler = CommandHandler('tt', timetable)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(tt_handler)


updater.start_polling()