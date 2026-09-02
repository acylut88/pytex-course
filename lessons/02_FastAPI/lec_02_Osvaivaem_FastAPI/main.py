from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"}
]

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
    uvicorn.run("main:app", reload=True)