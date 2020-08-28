
import pandas as pd
import numpy as np
import datetime
import time
import configparser
import logging
from os import listdir
import os
from os.path import isfile, join

from flask import Flask, request
import telegram
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import requests
from datetime import datetime
import configparser

path = os.path.abspath('.')



app = Flask(__name__)

config = configparser.RawConfigParser()
config.read("./secret.ini")
Token = config["TELEGRAM"]["ACCESS_TOKEN"]

bot = telegram.Bot(token=Token)



@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'


def start_handler(bot, update):
    """Send a message when the command /start is issued."""
    
    update.message.reply_text("Hi 歡迎使用")

def help_handler(bot, update):
    """Send a message when the command /help is issued."""
    
    help_message = "收到請求幫助了"
    
    update.message.reply_text(help_message)
    
def reply_handler(bot, update):
    text = update.message.text
    update.message.reply_text(f"你剛剛說了 {text}")
    
def error_handler(bot, update, error):
    """Log Errors caused by Updates."""
    chat_id = update.message.chat.id
    print(update)
    print(error)
    update.haveSend = True
    update.message.reply_text(text = '對不起，系統錯誤\n歡迎回報，告訴開發者')


dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))
dispatcher.add_error_handler(error_handler)


#https://api.telegram.org/bot1101986164:AAHRD1hDy0ZVStaYn9vxt4kZxOyLfubbVVA/setWebhook?url=https://gcp-wp-0.tsraise.com/hook
#https://api.telegram.org/bot{TOKEN}/setWebhook?url=https://gcp-wp-0.tsraise.com/hook

if __name__ == "__main__":
    # Running server
    app.run(port = 13520)
