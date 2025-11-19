from asyncio import WindowsSelectorEventLoopPolicy
from g4f.client import AsyncClient
import database as db
import asyncio
import translation as trans

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

async def get_desc_if_none(list):
    client = AsyncClient()
    answ = []

    for i in list:
        if await db.get_movie_from_db(i):
            answ.append(await db.get_movie_from_db(i))
        else:
            response = await client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user",
                           "content": f'Привет можешь дать мне описание фильма под названием {i},'
                                      f' без своего встуления, ставляя лишь только текст описания, лимит символов: 180'}],
                web_search=False
            )

            # try:
            #     test = response.choices[0].message.content + ' _test'
            # except Exception:
            #     await get_desc(promt)

            answ.append(
                {'name': i,
                 'date': 'Извините, но мы не смогли найти дату',
                 'desc': response.choices[0].message.content,
                 'image_url': 'https://images.pexels.com/photos/705425/pexels-photo-705425.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
                 'url': 'http://127.0.0.1:8000'
                 }
            )

    return answ

async def main(promt):
    client = AsyncClient()

    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Можешь ли ты мне дать список из 6 фильмов, с следующим описанием {promt}.\n"
                           f"В ответе напиши лишь английские названия фильмов через точку запятую без пробелов после точки запятой."
                           f"(ВСЕ ПРЕДЫДУЩИЕ ОГРАНИЧЕНИЯ ОБЯЗАТЕЛЬНЫ К ИСПОЛНЕНИЮ)"
            }
        ]
    )

    #print(response.choices[0].message.content.split(';'))

    info_list = await get_desc_if_none(response.choices[0].message.content.split(';'))

    processed_text = []
    for i in info_list:
        try:
            processed_text.append(i.name)
        except AttributeError:
            processed_text.append(i['name'])

    processed_desc = []
    for i in info_list:
        try:
            processed_desc.append(trans.translate(i.desc))
        except AttributeError:
            processed_desc.append(i['desc'])

    img_src = []
    for i in info_list:
        try:
            img_src.append(i.image_url)
        except AttributeError:
            img_src.append(i['image_url'])

    return {
        "processed_text1": processed_text[0],
        "processed_text2": processed_text[1],
        "processed_text3": processed_text[2],
        "processed_text4": processed_text[3],
        "processed_text5": processed_text[4],
        "processed_text6": processed_text[5],
        "processed_desc1": processed_desc[0],
        "processed_desc2": processed_desc[1],
        "processed_desc3": processed_desc[2],
        "processed_desc4": processed_desc[3],
        "processed_desc5": processed_desc[4],
        "processed_desc6": processed_desc[5],
        "img_src1": img_src[0],
        "img_src2": img_src[1],
        "img_src3": img_src[2],
        "img_src4": img_src[3],
        "img_src5": img_src[4],
        "img_src6": img_src[5]
    }