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

from flask_cors import CORS, cross_origin


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
            print(filmdict["img"])
            list_film.append(filmdict)

print(list_film)