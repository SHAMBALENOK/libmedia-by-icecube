from asyncio import WindowsSelectorEventLoopPolicy

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
    listy = []
    file = open(path, 'r')
    items = json.load(file)
    for item in items:
        info = {'name': item['title'], 'date': item['release_date']}
        listy.append(info)

    movies = []
    for item in listy:
        name = item['name']
        date = item['date'].replace('Released', '')
        client = Client()
        response = client.chat.completions.create(
            model="qwen-2.5-coder-32b",
            messages=[{"role": "user", "content": f'Привет можешь дать мне описание фильма под названием {name}, '
                                                  f'вышедшего в {date}, лимит символов: 200'}],
            web_search=False
        )
        info = {'name': name, 'date': date, 'description': response.choices[0].message.content.replace('Конечно! ', '')}
        movies.append(info)
        print(info)
    # print(response.choices[0].message.content)
    return movies


data = get_desc('movie_info.json')
print(data)
with open("db.txt", "w") as file:
    file.write(data)
