from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
# .ext.asyncio - ext - расширение
# async_sessionmaker - для создания сессий
# create_async_engine - создание асинхронного движка
from src.config import settings



# создаем асинхронный движок
engine = create_async_engine(settings.DB_URL)


async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

session = async_session_maker()

# пример sql скрипта.
# создаем временные 2 таблиццы
# открываем транзакцию
# выполняем 2 указания (задать значеиня)
# закрываем транзакцию
# смотрим что находится в таблицах
"""
create temporary table test1(
	id int
);
create temporary table test2(
	id int
);


start transaction;
insert into test1 (id) values (35);
insert into test2 (id) values (250);
end transaction;


select * from test1;
select * from test2;
"""
# в случае, если чтото пойдет ни так на этапе присвоения значений одной или др таблице
# произойдет откат до состояния таблицы в которой находилась до начала транзакции