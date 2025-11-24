from PyMovieDb import IMDB
import asyncio
import translation as trans
from g4f.client import AsyncClient

async def search_IMDb(promt):
    imdb = IMDB()
    client = AsyncClient()
    res = imdb.get_by_name(promt, tv=True)
    # print(res)
    try:
        res = eval(res.replace('null', 'None'))
        print(res['status'])
        return None
    # except NameError:
    #     return None
    except KeyError:
        URL_splitted = res['url'].split('/tt')
        URL = URL_splitted[0]+'/title/tt'+URL_splitted[1]
        # print({
        #     'name': res['name'],
        #     'date': res['datePublished'],
        #     'desc': res['description'],
        #     'image_url': res['poster'],
        #     'url': URL
        # })
        if not res['description']:
            response = await client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user",
                           "content": f'Привет можешь дать мне описание фильма под названием {res['name']},'
                                      f' без своего встуления, ставляя лишь только текст описания, лимит символов: 180'}],
                web_search=False
            )

            return {
                'name': res['name'],
                'date': res['datePublished'],
                'desc': response.choices[0].message.content,
                'image_url': res['poster'],
                'url': URL
            }
        else:
            return {
                'name': res['name'],
                'date': res['datePublished'],
                'desc': trans.translate(str(res['description'])),
                'image_url': res['poster'],
                'url': URL
            }
