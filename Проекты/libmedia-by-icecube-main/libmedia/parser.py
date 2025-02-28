import requests
from bs4 import BeautifulSoup as BS
import json
import database as db

def get_desc(path):
    class_ = 'synopsis-wrap'
    file = open(path, 'r+')
    items = json.load(file)
    for item in items:
        try:
            url = item['url']
            r = requests.get(url)
            html = BS(r.text, 'html.parser')
            t = html.find('div', class_)
            name = item['title']
            date = item['release_date']
            images =  html.find_all('img')
            image_urls = []
            for image in images:
                image_urls.append(image.get('src'))
            db.add_cinema(name, date, t.text.replace('Synopsis', ''), url, image_urls[10])
        except AttributeError:
            url = item['url']
            r = requests.get(url)
            html = BS(r.text, 'html.parser')
            name = item['title']
            date = item['release_date']
            images =  html.find_all('img')
            image_urls = []
            for image in images:
                image_urls.append(image.get('src'))
            db.add_cinema(name, date, 'К сожалению мы не смогли найти описание.', url, image_urls[10])


get_desc('movie_info.json')