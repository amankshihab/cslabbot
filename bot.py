from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from resources.secrets import TOKEN
from resources.tt import tt
from datetime import datetime, date
import json

updater = Updater(token=TOKEN, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    user = update.message.from_user
    hello = f"Hello {user['firstname']}!"
    update.message.reply_text(hello)

def intro(update, context):
	#context.bot.reply_text(chat_id=update.effective_chat.id, text='Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')
    intro = """Hey there! I am the CSLAbot. 
    I am a WIP bot. 
    So stay tuned for more features. 
    Send /help to know my features"""
    update.message.reply_text(intro)
    """update.send_message(chat_id=update.message.chat_id, 
    text="*bold* _italic_ `fixed width font` [link](http://google.com)\.", 
    parse_mode=telegram.ParseMode.MARKDOWN_V2)"""

def timetable(update, context):
    today = datetime.today().strftime("%A")

    text = f"{today} ({date.today()})\n\n"
    for period in tt[today]:
        text += tt[today][period]
        text += "\n"

    update.message.reply_text(text)

def syllabus(update, context):
    url = "https://ktu.edu.in/data/COMPUTER%20SCIENCE%20AND%20ENGINEERING.pdf?=VDaCKgpZgjYqdJnW9kytNcr8GyJ0W8J3GpN22zV%2BXbRYw1JL4VK3h6CLTkOVonWAyZ0GdFnXL%2B6tbY7irHrwzA%3D%3D"
    text = "Here you go, This is the syllabus"
    update.message.reply_text(text + "\n" + url)

def help(update , context):
    update.message.reply_text("""
    I am still under dev so I can only do the following features:
    1." /tt " - shows timetable
    2." /who " - shows info about me
    3." /hello " - self explanatory
    4." /syllabus " - get's the syllabus
    5." /webex " - to get links for class
    """)

def webex(update , context):
    url1 = "https://fisat.webex.com/meet/csecr1"
    url2 = "http://fisat.webex.com/meet/csecra2"
    text= "Here are the links for the Webex class. Don't be late!!"
    update.message.reply_text(text + "\n" + "csecr1 - \n" + url1 + "\ncsecra2 - \n" + url2)

hello_handler = CommandHandler('hello', hello)
intro_handler = CommandHandler('who', intro)
tt_handler = CommandHandler('tt', timetable)
help_handler = CommandHandler('help',help)
start_handler = CommandHandler('start', help)
syllabus_handler = CommandHandler('syllabus', syllabus)
webex_handler = CommandHandler('webex', webex)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(tt_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(syllabus_handler)
dispatcher.add_handler(webex_handler)

updater.start_polling()