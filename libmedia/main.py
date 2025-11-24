from os import fstat

from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel
import ai

app = FastAPI()

listy = None

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
async def index():
    return Response(open("public/index.html", encoding="utf-8").read(), media_type="text/html")


class TextInput(BaseModel):
    text: str


@app.post('/process-text')
async def process_text(input_data: TextInput):
    return await ai.main(input_data.text)












    # movie_data = await ai.get_movie(str(input_data.text))
    # # print(movie_data)
    # info_list = []
    # cards = 0
    # for i in movie_data:
    #     print(movie_data.index(i), i)
    #     info = await db.get_movie_from_db(i)
    #     info_list.append(info)
    #     # print(info)
    #     # if info is not None:
    #         # cards += 1
    #         # info_list.append(info)
    #     # if cards == 6:
    #     #     break
    #
    # for i in info_list:
    #     if i is None:
    #         info_list[info_list.index(i)] = {'name': movie_data[info_list.index(i)],
    #                                          'date': 'Извините, но мы не смогли найти дату',
    #                                          'desc': await ai.get_desc(movie_data[info_list.index(i)]),
    #                                          'image_url': 'https://images.pexels.com/photos/705425/pexels-photo-705425.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
    #                                          'url': 'http://127.0.0.1:8000'
    #                                          }
    #
    # processed_text = []
    # for i in info_list:
    #     try:
    #         processed_text.append(i.name)
    #     except AttributeError:
    #         processed_text.append(i['name'])
    #
    # processed_desc = []
    # for i in info_list:
    #     try:
    #         processed_desc.append(trans.translate(i.desc))
    #     except AttributeError:
    #         processed_desc.append(i['desc'])
    #
    # img_src = []
    # for i in info_list:
    #     try:
    #         img_src.append(i.image_url)
    #     except AttributeError:
    #         img_src.append(i['image_url'])
    #
    # return {
    #     "processed_text1": processed_text[0],
    #     "processed_text2": processed_text[1],
    #     "processed_text3": processed_text[2],
    #     "processed_text4": processed_text[3],
    #     "processed_text5": processed_text[4],
    #     "processed_text6": processed_text[5],
    #     "processed_desc1": processed_desc[0],
    #     "processed_desc2": processed_desc[1],
    #     "processed_desc3": processed_desc[2],
    #     "processed_desc4": processed_desc[3],
    #     "processed_desc5": processed_desc[4],
    #     "processed_desc6": processed_desc[5],
    #     "img_src1": img_src[0],
    #     "img_src2": img_src[1],
    #     "img_src3": img_src[2],
    #     "img_src4": img_src[3],
    #     "img_src5": img_src[4],
    #     "img_src6": img_src[5]
    # }
