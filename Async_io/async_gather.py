import asyncio

async def function1():
    await asyncio.sleep(1)
    print("function1")

async def function2():
    await asyncio.sleep(2)
    print("function2")

async def function3():
    await asyncio.sleep(4)
    print("function3")

async def main():
    task = asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(task)
    await task  # Wait for all tasks to complete

asyncio.run(main())
