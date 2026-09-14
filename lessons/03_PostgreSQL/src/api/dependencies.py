from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, description="Страница отображения списка Отелей", ge=1)] 
    per_page: Annotated[int | None, Query(3, description="Кол-во Отелей на странице", ge=3, lt=20)]


PaginationDep = Annotated[PaginationParams, Depends()]
