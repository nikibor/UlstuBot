import feedparser
import urllib
import urllib.request, json
import requests
from PIL import Image

def Parse_scv():
    data_parsed = feedparser.parse('https://news.yandex.ru/Ulyanovsk/index.rss')
    result = []
    for news in data_parsed['entries']:
        result.append(news['title'])
    return result

def TraficJam():
    url = 'https://static-maps.yandex.ru/1.x/?ll=48.371407,54.305344&spn=0.3,0.3&l=map,trf'
    im = Image.open(urllib.request.urlopen(url))
    f = open('traffic.jpg', 'wb')
    f.write(requests.get(url).content)
    f.close()
    return im
