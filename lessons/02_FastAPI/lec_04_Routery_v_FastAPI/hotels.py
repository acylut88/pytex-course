from fastapi import Query, Body, APIRouter
import time
import asyncio


router = APIRouter(prefix="/hotels", tags=["Отели"])


hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"}
]



@router.get("", summary="Получение Отелей")
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


@router.post("", summary="Добавление Отеля")
def create_hotel(
    title: str = Body(embed=True,)  # body, request body  -> тело запроса
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": title
    })
    return {"status", "OK"}


@router.put("/hotels/{hotel_id}", summary="Полное обновление данных об отеле")
def put_hotel(
    hotel_id: int,  
    title: str = Body(description="Местоположение Отеля"),
    name: str = Body(description="Название Отеля")
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            return {"status": "OK"}
    return {"status": "Not ID"}


@router.patch(
        "/hotels/{hotel_id}", 
        summary="Частичное обновление данных об отеле",
        description="Тут мы частично обновляем данные Отеля")
def patch_hotel(
    hotel_id: int,
    title: str | None = Body(None, embed=True, description="Местоположение Отеля"),
    name: str | None = Body(None, embed=True, description="Наименование Отеля")
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if title:
        hotel["title"] = title
    if name:
        hotel["name"] = name
    return {"status": "OK"}


@router.delete("/{hotel_id}", summary="Удление Отеля")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status", "OK"}



# === === === ПРОВЕРКА РАБОТЫ СИНХРОННЫХ И АСИНХРОННЫХ РУЧЕК === === ===
# синхронная ручка
@router.get(
        "/sync/{id}", 
        summary="Синхронная ручка, с таймером в 3 сек",
        description="Для проверки нагрузки на сервер и понятия о том, как работают Синхронные ручки")
def sync_func(id: int):
    # print(f"sync. Потоков: {threading.active_count()}")
    print (f"sync. Начал {id}: {time.time():.2f}")
    time.sleep(3)
    print (f"sync. Закончил {id}: {time.time():.2f}")


# асинхронная ручка
@router.get(
        "/async/{id}", 
        summary="Асинхронная ручка, с таймером в 3 сек",
        description="Для проверки нагрузки на сервер и понятия о том, как работают АСинхронные ручки")
async def async_func(id: int):
    # print(f"async. Потоков: {threading.active_count()}")
    print (f"async. Начал {id}: {time.time():.2f}")
    await asyncio.sleep(3)
    print (f"async. Закончил {id}: {time.time():.2f}")

# === === === === === === === === === ===