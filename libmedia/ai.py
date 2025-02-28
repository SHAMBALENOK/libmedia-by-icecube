from asyncio import WindowsSelectorEventLoopPolicy
import database as db
from g4f.client import Client
from g4f.client import AsyncClient
import json
import time
import asyncio

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

async def get_movie(promt):
    client = AsyncClient()

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Можешь ли ты мне дать список фильмов, с следующим описанием {promt}, в формате:\nТвое "
                              f"вступительное слово(Обязательно точка запятая, и после точки запятой не должно быть "
                              f"отступов, или какого либо другого текста кроме названий фильмов) далее 6 фильмов по описанию в одну строчку, а разделяй их точками. Названия пиши на английском языке"}],
        web_search=False
    )

    try:
        test = response.choices[0].message.content + ' _test'
    except Exception:
        await get_movie(promt)

    return response.choices[0].message.content.split('; ')[1].split('. ')

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
            messages=[{"role": "user", "content": f'Привет можешь дать мне описание фильма под названием {name}, лимит символов: 180'}],
            web_search=True
        )
        db.add_cinema(name, date, response.choices[0].message.content.replace('Конечно! ', ''))
        items.remove(item)
