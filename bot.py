from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

from resources.secrets import TOKEN
from resources.tt import tt
import joke as jokes
import scraper as sc
import quote as quotess

from datetime import datetime, date
import json
#import logging
from time import sleep

"""logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)"""


updater = Updater(token=TOKEN, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update: Update, context: CallbackContext) -> None:
    #context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')
    user = update.message.from_user
    hello = f"Hello {user['first_name']}!, ssup?"
    update.message.reply_text(hello)

def intro(update: Update, context: CallbackContext) -> None:
	#context.bot.reply_text(chat_id=update.effective_chat.id, text='Hey there! I am the CSLAbot. I am WIP bot. So wait for further features')
    intro = """Hey there! I am the CSLAbot. 
    Developed by the great minds in CSA(19-23)
    To get a list of my commands type in "/help"
    """
    update.message.reply_text(intro)
    """update.send_message(chat_id=update.message.chat_id, 
    text="*bold* _italic_ `fixed width font` [link](http://google.com)\.", 
    parse_mode=telegram.ParseMode.MARKDOWN_V2)"""

def timetable(update: Update, context: CallbackContext) -> None:
    today = datetime.today().strftime("%A")

    if today != 'Saturday' and today != 'Sunday':
        text = f"{today} ({date.today()})\n\n"
        for period in tt[today]:
            text += tt[today][period]
            text += "\n"

        update.message.reply_text(text)
    else:
        text = f"Seriously? You want class on a {today}, It's {date.today()} btw."
        update.message.reply_text(text)

def syllabus(update: Update, context: CallbackContext) -> None:
    url = "https://ktu.edu.in/data/COMPUTER%20SCIENCE%20AND%20ENGINEERING.pdf?=VDaCKgpZgjYqdJnW9kytNcr8GyJ0W8J3GpN22zV%2BXbRYw1JL4VK3h6CLTkOVonWAyZ0GdFnXL%2B6tbY7irHrwzA%3D%3D"
    text = "Here you go, This is the syllabus"
    update.message.reply_text(text + "\n" + url)

def help(update: Update , context: CallbackContext) -> None:
    update.message.reply_text("""
    I am a constantly evolving bot, I get better with every features added by the great minds of CSA ;):
    1." /tt " - shows timetable
    2." /who " - shows info about me
    3." /hello " - self explanatory
    4." /syllabus " - gets the syllabus
    5." /webex " - to get links for class
    6." /ktu " - get latest notification from ktu, takes a while to get it
    7." /joke " - sends a random joke
    8." /quote " - send a random quote
    """)

def webex(update:Update , context: CallbackContext) -> None:
    url1 = "https://fisat.webex.com/meet/csecr1"
    url2 = "http://fisat.webex.com/meet/csecra2"
    text= "Here are the links for the Webex class. Don't be late!!"
    update.message.reply_text(text + "\n" + "csecr1 - \n" + url1 + "\ncsecra2 - \n" + url2)

def scraped_info(context):
    text, is_there = sc.get_info()
    job = context.job
    if(is_there == True):
       context.bot.send_message(chat_id=job.context, text=text)    
    else:
       pass
    
def if_job_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)

    if not current_jobs:
        return False
    
    for job in current_jobs:
        job.schedule_removal()
    
    return True

def scrape_timer(update: Update, context: CallbackContext) -> None:
    job_removed = if_job_exists(str(update.message.chat_id), context)
    context.job_queue.run_repeating(scraped_info, 300, context = update.message.chat_id, name = str(update.message.chat_id))

    text = "New notifications from KTU will pop up automatically here as they come."
    if job_removed:
        text += "\nOld job was removed"
    update.message.reply_text(text)

def stops(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    job_removed = if_job_exists(str(chat_id), context)
    update.message.reply_text("You wont receive automatic notifs from KTU anymore, /ktu can be used to get it manually.")

def ktu_notif(update: Update, context: CallbackContext) -> None:
    text, is_there = sc.get_info()
    if(is_there == False):
        text = text.replace("**New Notification**", "**Last Notification**")
    
    update.message.reply_text(text)

def joke(update: Update, context: CallbackContext) -> None:
    success,joke = jokes.get_joke()

    if success == True:
        reply = update.message.reply_text(joke)
        sleep(4)
        reply.delete()

    else:
        update.message.reply_text("Idk why, I'm not feeling funny at the moment.")

def quotes(update: Update, context: CallbackContext) -> None:
    success, quote_retreived = quotess.get_quotes()

    if(success == True):
        reply = update.message.reply_text(quote_retreived)
        sleep(6)
        reply.delete()
    else:
        update.message.reply_text("Error 404 while loading inspiration. Try later.")

hello_handler = CommandHandler('hello', hello)
intro_handler = CommandHandler('who', intro)
tt_handler = CommandHandler('tt', timetable)
help_handler = CommandHandler('help',help)
start_handler = CommandHandler('start', help)
syllabus_handler = CommandHandler('syllabus', syllabus)
webex_handler = CommandHandler('webex', webex)
ktu_handler = CommandHandler('ktu', ktu_notif)
joke_handler = CommandHandler('joke', joke)
quote_handler = CommandHandler('quote', quotes)
ktustart_handler = CommandHandler('ktustart', scrape_timer)
ktustop_handler = CommandHandler('ktustop', stops)

dispatcher.add_handler(hello_handler)
dispatcher.add_handler(intro_handler)
dispatcher.add_handler(tt_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(syllabus_handler)
dispatcher.add_handler(webex_handler)
dispatcher.add_handler(ktu_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(quote_handler)
dispatcher.add_handler(ktustart_handler)
dispatcher.add_handler(ktustop_handler)

updater.start_polling()

updater.idle()
