import asyncio as asn

async def worker():
    print("Start")
    await asn.sleep(1)
    print("Worker done after sleeping")

async def main():
    task = asn.create_task(worker())
    print("Task created")


if __name__ == "__main__":
    asn.run(main())