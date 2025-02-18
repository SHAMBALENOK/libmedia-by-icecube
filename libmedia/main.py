from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse

app = FastAPI()

app.mount('/public', StaticFiles(directory='public'))


@app.get("/")
async def root():
    return FileResponse("public/index.html")


@app.post("/api/search")
async def search1(text=Body()):
    t = text['text']
    return t


# @app.post("/button_click")
# async def button_click(request: Request):
#     print("Кнопка нажата!")
#
#
# @app.post("/submit_text")
# async def submit_text(text: str):
#     print(f"Текст из input: {text}")
#     return {"message": f"Текст '{text}' успешно передан!"}
