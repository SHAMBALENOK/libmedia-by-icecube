from asyncio import WindowsSelectorEventLoopPolicy

import database as db
from g4f.client import Client
import json
import time
import asyncio

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())


def get_movie(promt):
    client = Client()
    response = client.chat.completions.create(
        model="qwen-2.5-coder-32b",
        messages=[{"role": "user",
                   "content": f"Можешь ли ты мне дать список фильмов и сериалов, с следующим описанием {promt}, "
                              f"когда будешь выписывать фильмы оставь лишь названия, и выпиши их в "
                              f"строку"}],
        web_search=False
    )
    # print(response.choices[0].message.content)

    return response.choices[0].message.content


def get_desc(path):
    file = open(path, 'r+')
    items = json.load(file)
    for item in items:
        url = item['url']
        name = item['title']
        date = item['release_date'].replace('Released', '')
        client = Client()
        response = client.chat.completions.create(
            model="qwen-2.5-coder-32b",
            messages=[{"role": "user", "content": f'Привет можешь дать мне описание фильма под названием {name}, '
                                                  f'вышедшего в {date}, лимит символов: 180'}],
            web_search=False
        )
        db.add_cinema(name, date, response.choices[0].message.content.replace('Конечно! ', ''))
        items.remove(item)

get_desc('movie_info.json')