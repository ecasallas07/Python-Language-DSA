import asyncio

# Learn to library asyncio ptyhon

async def process(id_process):
    print(f"Empieza el proceso {id_process}")
    await asyncio.sleep(10)
    print(f"Acaba proceso {id_process}")

async def main():
    await asyncio.gather(process(1),process(2),process(3))


asyncio.run(main())  # asyncio.run() is a new coroutine in Python 3.7+ and replaces asyncio.get_event_loop().run_until_complete()







