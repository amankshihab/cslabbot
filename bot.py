import telebot
import os
from secrets import TOKEN

bot = telebot.TeleBot(TOKEN, parse_mode = None)

@bot.message_handler(commands=['start', 'help'])
def print_message(message):
    bot.reply_to(message, "Hey there!")