"""
Что нужно сделать:
- Дописать функцию main()
- Собрать итоговый дашборд пользователя
- Измерить общее время выполнения программы через time.perf_counter()
- Вывести в консоль итоговый дашборд и время выполнения

Готовых функций менять не нужно.
❗️Важно: не все функции можно запускать одновременно. 
Некоторые шаги зависят от user_id, а одна из функций зависит уже не от user_id, а от списка бронирований. 
Сначала разберитесь, какие вызовы можно выполнять параллельно, а какие нет, 
и только потом собирайте итоговый дашборд. 

Ответ:  _ секунд для самого быстрого выполнения
"""

import asyncio
import time


async def login():
    print("Авторизуем пользователя...")
    await asyncio.sleep(1)
    print("Пользователь авторизован")
    return 42


async def get_user_profile(user_id):
    print(f"Получаем профиль пользователя {user_id}...")
    await asyncio.sleep(1)
    print("Профиль получен")
    return {"user_id": user_id, "name": "Алексей"}


async def get_user_bookings(user_id):
    print(f"Получаем бронирования пользователя {user_id}...")
    await asyncio.sleep(2)
    print("Бронирования получены")
    return [
        {"hotel": "AZIMUT Сити Отель Смоленская", "city": "Москва"},
        {"hotel": "Cosmos Saint-Petersburg Nevsky Hotel", "city": "Санкт-Петербург"}
    ]


async def get_popular_hotels():
    print("Получаем список популярных отелей...")
    await asyncio.sleep(3)
    print("Популярные отели получены")
    return [
        {"hotel": "Marins Park Hotel", "city": "Сочи"},
        {"hotel": "AZIMUT Отель", "city": "Казань"},
        {"hotel": "Cosmos Selection", "city": "Москва"}
    ]


async def get_recommendations(bookings):
    print("Получаем персональные рекомендации...")
    await asyncio.sleep(1)
    print("Рекомендации получены")
    return [
        {"hotel": "Гранд Отель Жемчужина", "city": "Сочи"},
        {"hotel": "AZIMUT Парк Отель", "city": "Переславль-Залесский"}
    ]


async def build_dashboard(profile, bookings, popular_hotels, recommendations):
    print("Собираем дашборд...")
    await asyncio.sleep(0.2)
    return {
        "profile": profile,
        "bookings": bookings,
        "popular_hotels": popular_hotels,
        "recommendations": recommendations
    }

async def get_bookings_and_recommendations(user_id):
    bookings = await get_user_bookings(user_id)
    recommenatons = await get_recommendations(bookings)
    return bookings, recommenatons


async def main():
    start_time = time.perf_counter()

    # Напишите здесь вашу логику
    user_id = await login()

    profile, popular_hotels, (bookings, recommendations) = await asyncio.gather(
        get_user_profile(user_id),
        get_popular_hotels(),
        get_bookings_and_recommendations(user_id)
    )

    await build_dashboard(profile=profile, 
                          bookings=bookings, 
                          popular_hotels=popular_hotels,
                          recommendations=recommendations)

    print("Времени прошло:", time.perf_counter() - start_time)


if __name__ == "__main__":
    asyncio.run(main())


"""
При использовании gather вы можете получить минимально 5.2 секунды на выполнение.
Код с решением:
Но если использовать асинхронность на максимум, можно добиться выполнения за 4.2 секунды!
В будущем в курсе вы познакомитесь с asyncio.create_task и сможете решить эту задачу более оптимально
"""