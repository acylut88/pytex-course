import time
import asyncio
from fastapi import FastAPI, Query, Body
import uvicorn
import threading

from hotels import router  as router_hotels  # импортируем из hotels.py, обзывая router_hotels

app = FastAPI()

# подключаем роутер
app.include_router(router=router_hotels)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

    # синхронные ручки работают в потоках (до 40-42 за раз), в отличие от асинхронных
    # для масштабирования синзронных ручек - увеличивают кол-во uvicorn (worker'ов - работников)
    # uvicorn.run("main:app", reload=False, workers=10)  ->  запускаем 10 воркеров
    # при этом, ОБЯЗАТЕЛЬНО -> reload=False! (не отслеживать изменения в файлах)