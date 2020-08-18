
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
pd.options.mode.chained_assignment = None  # default='warn'
ISOTIMEFORMAT = '%Y%m%d_%H%M%S'

path = os.path.abspath('.')



app = Flask(__name__)

"""config = configparser.RawConfigParser()
config.read("./secret.ini")
Token = config["Secret"]["BotToken"]"""

Token = ""
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

dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('help', help_handler))

if __name__ == "__main__":
    # Running server
    app.run(port = 8787)
