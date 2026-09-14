from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
# .ext.asyncio - ext - расширение
# async_sessionmaker - для создания сессий
# create_async_engine - создание асинхронного движка
from src.config import settings



# создаем асинхронный движок
engine = create_async_engine(settings.DB_URL)


# СЫРОЙ ЗАПРОС В БД
"""
from sqlalchemy import text
import asyncio
async def func():
    async with engine.begin() as conn: 
        # conn - connection
        # показать вверсию БД
        res = await conn.execute(text("SELECT version()"))  # execute - выполнить запрос
        print(res.fetchone())  # fetchone() - просим вывести 1 строку

asyncio.run(func())

в main.py для вывода добавить:
from src.database import *
в том месте где нужна инфа по версии БД
"""

