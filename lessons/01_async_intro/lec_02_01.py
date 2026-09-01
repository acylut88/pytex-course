import asyncio
async def one():
    print("one")

async def two():
    print("two")

async def main():
    await one()
    await two()
    print("Hellow, async World!")


if __name__ == "__main__":
    asyncio.run(main())
