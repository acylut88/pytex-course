"""
        Задание №2: Пагинация для отелей

Необходимо реализовать пагинацию для отелей.
Для этого необходимо добавить 2 query параметра 
page и per_page, оба параметра являются необязательными. 
Если пользователь не передает page, то используется значение по умолчанию 1 (то есть первая страница). 
Для per_page ситуация аналогичная — если параметр не передается, 
    то используется значение по умолчанию 3 (можете выбрать любое другое).                
"""


from fastapi import Body, Query, APIRouter
from schemas.hotels import Hotel, HotelPATCH
import time
import asyncio



router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "питер", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]

PATCH_HOTEL_CONFIG = {
    "summary": "Частичное обновление данных об отеле",
    "description": "Тут мы частично обновляем данные Отеля"
}

# === === === РЕШЕНИЕ === === ===
import math


hotels = [
    {"id": 1, "title": "Дубай", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Дубай", "name": "maldivi"},
    {"id": 4, "title": "Дубай", "name": "gelendzhik"},
    {"id": 5, "title": "Дубай", "name": "moscow"},
    {"id": 6, "title": "Дубай", "name": "kazan"},
    {"id": 7, "title": "Дубай", "name": "spb"},
]
# def get_hotels(
#     # id: int | None -> id либо ИНТ либо НЕТ
#     # Query(None,..) -> значение по умолчанию
#     id: int | None = Query(None, description="Айдишник"),  
#     title: str | None = Query(None, description="Название отеля", ),
#     page: int | None = Query(1, description="Страница отображения списка Отелей"),
#     per_page: int | None = Query(3, description="Кол-во Отелей на странице")
# ):   
#     hotels_ = []

    # for hotel in hotels:
    #     if id and hotel["id"] != id:
    #         continue  # если id отеля не равен айди из поиска -> пропускаем
    #     if title and hotel["title"] != title:
    #         continue
    #     hotels_.append(hotel)

    # return hotels_[(page-1)*per_page : page * per_page], {
    #     "Hotels": len(hotels_),
    #     "This page": page,
    #     "All pages": math.ceil((len(hotels_)/per_page))
    # }

# === === === КОНЕЦ РЕШЕНИЯ === === ===


# # === === === === РЕШЕНИЕ МЕНТОРА === === ===
# def get_hotels(
#     id: int | None = Query(None, description="Айдишник"),  
#     title: str | None = Query(None, description="Название отеля", ),
#     page: int | None = Query(None, description="Страница отображения списка Отелей", gt=1),
#     per_page: int | None = Query(None, description="Кол-во Отелей на странице", gt=1, lt=20)
# ):   
#     # gt - greiter then больше чем, lt - less than меньше чем
#     hotels_ = []

#     for hotel in hotels:
#         if id and hotel["id"] != id:
#             continue  # если id отеля не равен айди из поиска -> пропускаем
#         if title and hotel["title"] != title:
#             continue
#         hotels_.append(hotel)

#     if page and per_page:
#         return hotels_[(page-1)*per_page : page * per_page]
#     return hotels_
# # === === === КОНЕЦ РЕШЕНИЯ МЕНТОРА === === ===



# === === === === ВТОРОЕ РЕШЕНИЕ МЕНТОРА === === ===
from dependencies import PaginationDep

@router.get("", summary="Получение Отелей")
def get_hotels(
    pagination: PaginationDep,
    id: int | None = Query(None, description="Айдишник"),  
    title: str | None = Query(None, description="Название отеля", ),
):   
    # ge - greiter of equal больше чем или равно, lt - less than меньше чем
    hotels_ = []

    for hotel in hotels:
        if id and hotel["id"] != id:
            continue  # если id отеля не равен айди из поиска -> пропускаем
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)

    return hotels_[(pagination.page-1)*pagination.per_page : pagination.page * pagination.per_page]
    
# === === === КОНЕЦ РЕШЕНИЯ МЕНТОРА === === ===



@router.post("", summary="Добавление Отеля")
def create_hotel(hotel_data: Hotel = Body(openapi_examples={
    "1": {"summary": "Сочи", "value": {
        "title": "Отель Сочи 5 звезд", 
        "name": "Sochy_u_morya"
    }},
    "2": {"summary": "Питер", "value": {
            "title": "Отель Питер", 
            "name": "Piter_u_Avrory"
        }},

})):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": hotel_data.title,
        "name": hotel_data.name
    })
    return {"status": "OK"}


@router.put("/{hotel_id}", summary="Полное обновление данных об отеле")
def put_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel_data.title
            hotel["name"] = hotel_data.name
            return {"status": "OK"}
    return {"status": "Not ID"}


@router.patch("/{hotel_id}", **PATCH_HOTEL_CONFIG)
def patch_hotel(hotel_id: int, hotel_data: HotelPATCH):
    global hotels
    try:
        hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    except:
        return {"status": "ERROR. list index out of range"}
    if hotel_data.title:
        hotel["title"] = hotel_data.title
    if hotel_data.name:
        hotel["name"] = hotel_data.name
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