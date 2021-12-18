import json
import time
import flask
from flask import request, jsonify
import telegram
import requests
from bs4 import BeautifulSoup
from threading import Thread
import threading
import time
from flask import render_template

from flask_cors import CORS, cross_origin
CHATID = ["1797238855"]
# film de cu
def get_film_decu():
    list_film = []
    data = requests.get('https://ephimmoi.net/')
    soup = BeautifulSoup(data.text, 'html.parser')
    ul_film = soup.find("ul", {"id": "movie-carousel-top"})
    # for a in ul_film.find_all('a', href=True):
    #     if a.text:
    #         filmdict = {}
    #         filmdict["title"] = a['title']
    #         filmdict["link"] = a['href']
    #         list_film.append(filmdict)
    for a in ul_film.find_all('a', href=True):
        if a.text:

            filmdict = {}
            filmdict["title"] = a['title']
            filmdict["link"] = a['href']
            img_film = a.find("div", {"class": "movie-carousel-top-item rocket-lazyload"})
            if img_film.text:
                filmdict["img"] = img_film['data-bg']
                list_film.append(filmdict)
    return list_film

# film the loai chien tranh
def get_film_chientranh():
    list_film = []
    data = requests.get('https://iphimmoi.net/category/chien-tranh')
    soup = BeautifulSoup(data.text, 'html.parser')
    ul_film = soup.find("ul", {"class": "last-film-box"})
    for a in ul_film.find_all('a', href=True):
        if a.text:
            filmdict = {}
            filmdict["title"] = a['title']
            filmdict["link"] = a['href']
            div_film = a.find("div", {"class": "public-film-item-thumb ratio-content rocket-lazyload"})
            filmdict["img"] = div_film['data-bg']
            list_film.append(filmdict)
    return list_film
# film the loai co trang
def get_film_cotrang():
    list_film = []
    data = requests.get('https://iphimmoi.net/category/co-trang/')
    soup = BeautifulSoup(data.text, 'html.parser')
    ul_film = soup.find("ul", {"class": "last-film-box"})

    for a in ul_film.find_all('a', href=True):
        if a.text:
            filmdict = {}
            filmdict["title"] = a['title']
            filmdict["link"] = a['href']
            div_film = a.find("div", {"class": "public-film-item-thumb ratio-content rocket-lazyload"})
            filmdict["img"] = div_film['data-bg']
            list_film.append(filmdict)
    return list_film

# film the loai gia dinh
def get_film_giadinh():
    list_film = []
    data = requests.get('https://iphimmoi.net/category/gia-dinh/')
    soup = BeautifulSoup(data.text, 'html.parser')
    ul_film = soup.find("ul", {"class": "last-film-box"})

    for a in ul_film.find_all('a', href=True):
        if a.text:
            filmdict = {}
            filmdict["title"] = a['title']
            filmdict["link"] = a['href']
            div_film = a.find("div", {"class": "public-film-item-thumb ratio-content rocket-lazyload"})
            filmdict["img"] = div_film['data-bg']
            list_film.append(filmdict)
    return list_film

# film the loai hai huoc
def get_film_haihuoc():
    list_film = []
    data = requests.get('https://iphimmoi.net/category/hai-huoc/')
    soup = BeautifulSoup(data.text, 'html.parser')
    ul_film = soup.find("ul", {"class": "last-film-box"})

    for a in ul_film.find_all('a', href=True):
        if a.text:
            filmdict = {}
            filmdict["title"] = a['title']
            filmdict["link"] = a['href']
            div_film = a.find("div", {"class": "public-film-item-thumb ratio-content rocket-lazyload"})
            filmdict["img"] = div_film['data-bg']
            list_film.append(filmdict)
    return list_film

def film():
    return get_film_decu()
def chientranh():
    return get_film_chientranh()
def cotrang():
    return get_film_cotrang()
def giadinh():
    return get_film_giadinh()
def haihuoc():
    return get_film_haihuoc()
def send_message(bot,title,data):
    for chatId in CHATID:
        bot.send_message(chat_id =chatId, text=title)
        for item in data:
            bot.send_message(chat_id =chatId, text=f'{item["link"]}')
            time.sleep(2)
TOKEN = "2139822060:AAGtO70Y6D-gmxrhjOCp0WJBYA8xdMmRWbQ"
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from threading import Thread
import threading
BOT = telegram.Bot(token=TOKEN)
@app.route('/test', methods=['GET'])
@cross_origin()
def home():
    data = film()
    return data
@app.route('/myfilm', methods=['POST'])
def api_all():
    global BOT
    data = []
    title = ""
    film_type = request.form["film_type"]
    if film_type == None:
        film_type = "film"

    if film_type == "hài hước":
        data = haihuoc()
        title = "hài hước"
        
    if film_type == "film":
        data = film()
        title = "phim gợi ý"

    if film_type == "chiến tranh":
        data = chientranh()
        title = "chiến tranh"

    if film_type == "cổ trang":
        data = cotrang()
        title = "cổ trang"    

    if film_type == "gia đình":
        data = giadinh()
        title = "gia đình" 
    t1 = threading.Thread(target=send_message, args=(BOT,title,data,))
    t1.start()
    return jsonify(data)
# STARTadss
@app.route('/o')
def defmain():
    return render_template('index.html')

app.run(host='0.0.0.0', port=7699)