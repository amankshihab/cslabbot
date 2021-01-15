from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from resources.secrets import TOKEN
from resources.tt import tt
from resources.joke import joke
import scraper as sc

from datetime import datetime, date
import json


updater = Updater(token=TOKEN, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    user = update.message.from_user
    hello = f"Hello {user['first_name']}!, ssup?"
    update.message.reply_text(hello)

def intro(update, context):
	#context.bot.reply_text(chat_id=update.effective_chat.id, text='Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')
    intro = """Hey there! I am the CSLAbot. 
    Developed by the great minds in CSA(19-23)
    To get a list of my commands type in "/help"
    """
    update.message.reply_text(intro)
    """update.send_message(chat_id=update.message.chat_id, 
    text="*bold* _italic_ `fixed width font` [link](http://google.com)\.", 
    parse_mode=telegram.ParseMode.MARKDOWN_V2)"""

def timetable(update, context):
    today = datetime.today().strftime("%A")

    if today != "Saturday" or today != "Sunday":
        text = f"{today} ({date.today()})\n\n"
        for period in tt[today]:
            text += tt[today][period]
            text += "\n"

        update.message.reply_text(text)
    else:
        text = f"Seriously? You want class on a {today}, It's {date.today()} btw."
        update.message.reply_text(text)

def syllabus(update, context):
    url = "https://ktu.edu.in/data/COMPUTER%20SCIENCE%20AND%20ENGINEERING.pdf?=VDaCKgpZgjYqdJnW9kytNcr8GyJ0W8J3GpN22zV%2BXbRYw1JL4VK3h6CLTkOVonWAyZ0GdFnXL%2B6tbY7irHrwzA%3D%3D"
    text = "Here you go, This is the syllabus"
    update.message.reply_text(text + "\n" + url)

def help(update , context):
    update.message.reply_text("""
    I am a constantly evolving bot, I get better with every features added by the great minds of CSA ;):
    1." /tt " - shows timetable
    2." /who " - shows info about me
    3." /hello " - self explanatory
    4." /syllabus " - gets the syllabus
    5." /webex " - to get links for class
    6." /ktu " - get latest notification from ktu, takes a while to get it
    """)

def webex(update , context):
    url1 = "https://fisat.webex.com/meet/csecr1"
    url2 = "http://fisat.webex.com/meet/csecra2"
    text= "Here are the links for the Webex class. Don't be late!!"
    update.message.reply_text(text + "\n" + "csecr1 - \n" + url1 + "\ncsecra2 - \n" + url2)

def scraped_info(update, context, job):
    #text, is_there = sc.get_info()
    #if(is_there == True):
     #   context.bot.send_message(chat_id=job.context, text=text)    
    #else:
     #   pass
    context.bot.send_message(chat_id=job.context, text="Hello") 

def scrape_timer(update, job_queue):
    job_queue.run_repeating(scraped_info, 10, context = update.message.chat_id)

def stops(update, job_queue):
    job_queue.stop()

def ktu_notif(update, context):
    text, is_there = sc.get_info()
    if(is_there == False):
        text = text.replace("**New Notification**", "**Latest Notification**")
    
    update.message.reply_text(text)

def joke(update, context):
    update.message.reply_text(joke)

hello_handler = CommandHandler('hello', hello)
intro_handler = CommandHandler('who', intro)
tt_handler = CommandHandler('tt', timetable)
help_handler = CommandHandler('help',help)
start_handler = CommandHandler('start', help)
syllabus_handler = CommandHandler('syllabus', syllabus)
webex_handler = CommandHandler('webex', webex)
ktu_handler = CommandHandler('ktu', ktu_notif)
daily_handler = CommandHandler('daily', scrape_timer, pass_job_queue=True)
stop_handler = CommandHandler('stop', stops, pass_job_queue=True)
joke_handler = CommandHandler('joke', joke)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(tt_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(syllabus_handler)
dispatcher.add_handler(webex_handler)
dispatcher.add_handler(ktu_handler)
dispatcher.add_handler(daily_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(joke_handler)

updater.start_polling()