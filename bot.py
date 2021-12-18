import flask
from flask import request, jsonify
from telegram import Update, KeyboardButton
import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
from threading import Thread
import threading
import time

bot = telegram.Bot(token="2139822060:AAGtO70Y6D-gmxrhjOCp0WJBYA8xdMmRWbQ")
bot.send_message(chat_id="1797238855",text="https://iphimmoi.net/nguoi-yeu-chang-ky-su/")
