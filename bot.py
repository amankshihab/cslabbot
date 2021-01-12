import telebot
import os
from secrets import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def print_message(message):
    bot.reply_to(message, "Hey there!")