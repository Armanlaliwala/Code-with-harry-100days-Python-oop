import  time
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
    task = asyncio.create_task(function1())
    await function1()  
    
    await function2()  
    
    await function3()
    
asyncio.run(main())    