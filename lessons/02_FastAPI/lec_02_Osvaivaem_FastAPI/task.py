"""
Задание №1: PUT и PATCH ручки отелей
Необходимо реализовать 2 ручки:
    1. Ручка PUT на изменение отеля
    2. Ручка PATCH на изменения отеля
Обе ручки позволяют видоизменить конкретный отель. 
Однако, в ручке PUT мы обязаны передать оба параметра title и name, 
    а в PATCH ручке можем передать: 
        либо только title, 
        либо только name, 
        либо оба параметра сразу (тогда PATCH ничем не отличается от PUT ручки).


Как будут выглядеть ручки:

    @app.put("/hotels/{hotel_id}")
    def ...
    @app.patch("/hotels/{hotel_id}")
    def ...
"""


from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"}
]

@app.get("/hotels", summary="Список Отелей")
def get_hotels():
    return hotels


@app.put("/hotels/{hotel_id}", summary="Полное обновление данных об отеле")
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


@app.patch(
        "/hotels/{hotel_id}", 
        summary="Частичное обновление данных об отеле",
        description="Тут мы частично обновляем данные Отеля")
def patch_hotel(
    hotel_id: int,
    title: str | None = Body(None, embed=True, description="Местоположение Отеля"),
    name: str | None = Body(None, embed=True, description="Наименование Отеля")
):
    global hotels

    """ мое решение"""
    # for hotel in hotels:
    #     if hotel["id"] == hotel_id:
    #         if title is not None and title != "string":
    #             hotel["title"] = title
    #         if name is not None and name != "string":
    #             hotel["name"] = name
    #         return {"status": "OK"}
    # return {"status": "Not ID"}


    """ решение от ментора"""
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if title:
        hotel["title"] = title
    if name:
        hotel["name"] = name
    return {"status": "OK"}
            
                


if __name__ == "__main__":
    uvicorn.run("task:app", reload=True)