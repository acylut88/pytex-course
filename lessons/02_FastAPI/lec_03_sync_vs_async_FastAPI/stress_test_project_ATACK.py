import asyncio
import aiohttp
import threading


# имитируем запрос на наш апи от другого разработчика
async def get_data(id: int, endpoint: str):
    url = f"http://127.0.0.1:8000/{endpoint}/{id}"  # адрес куда будем стучаться
    print(f"Начал выполнение: {id}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            print(f"Закончил выполнение: {id}")


async def main():
    await asyncio.gather(
        *[get_data(i, "async") for i in range(200)]  # асинхронная функция
        # *[get_data(i, "sync") for i in range(200)]  # синхронная функция
    )

if __name__ == "__main__":
    # проверяем, что все работает
    # asyncio.run(get_data(1, "async"))
    # asyncio.run(get_data(1, "sync"))
    asyncio.run(main())