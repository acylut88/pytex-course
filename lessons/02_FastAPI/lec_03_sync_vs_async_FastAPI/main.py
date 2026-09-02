import time
import asyncio
from fastapi import FastAPI, Query, Body
import uvicorn
import threading



app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"}
]

# === === === ПРОВЕРКА РАБОТЫ СИНХРОННЫХ И АСИНХРОННЫХ РУЧЕК === === ===
# синхронная ручка
@app.get("/sync/{id}")
def sync_func(id: int):
    print(f"sync. Потоков: {threading.active_count()}")
    print (f"sync. Начал {id}: {time.time():.2f}")
    time.sleep(3)
    print (f"sync. Закончил {id}: {time.time():.2f}")


# асинхронная ручка
@app.get("/async/{id}")
async def async_func(id: int):
    print(f"async. Потоков: {threading.active_count()}")
    print (f"async. Начал {id}: {time.time():.2f}")
    await asyncio.sleep(3)
    print (f"async. Закончил {id}: {time.time():.2f}")

# === === === === === === === === === ===

@app.get("/hotels")
def get_hotels(
    # id: int | None -> id либо ИНТ либо НЕТ
    # Query(None,..) -> значение по умолчанию
    id: int | None = Query(None, description="Айдишник"),  
    title: str | None = Query(None, description="Название отеля")
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue  # если id отеля не равен айди из поиска -> пропускаем
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)

    return hotels_


@app.post("/hotels")
def create_hotel(
    title: str = Body(embed=True,)  # body, request body  -> тело запроса
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": title
    })
    return {"status", "OK"}


@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status", "OK"}



if __name__ == "__main__":
    uvicorn.run("02_main_stress_test_project:app", reload=True)

    # синхронные ручки работают в потоках (до 40-42 за раз), в отличие от асинхронных
    # для масштабирования синзронных ручек - увеличивают кол-во uvicorn (worker'ов - работников)
    # uvicorn.run("main:app", reload=False, workers=10)  ->  запускаем 10 воркеров
    # при этом, ОБЯЗАТЕЛЬНО -> reload=False! (не отслеживать изменения в файлах)