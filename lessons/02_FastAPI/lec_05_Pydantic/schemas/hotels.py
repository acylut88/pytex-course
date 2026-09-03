from pydantic import BaseModel, Field


# pydantic схема
class Hotel(BaseModel):
    title: str = Field(description="Местоположение Отеля")
    name: str = Field(description="Название Отеля")


class HotelPATCH(BaseModel):
    title: str | None = Field(None, description="Местоположение Отеля")
    name: str | None = Field(None, description="Наименование Отеля")