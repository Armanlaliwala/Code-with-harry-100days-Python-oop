import time
import threading
from concurrent.futures import ThreadPoolExecutor

def function (second):
    print(f"This function is sleeping for {second} \n")
    time.sleep(second)
    return second
    
#Normal_Code
# time1 = time.perf_counter()    
# function(5)
# function(3)
# function(1)
# time2 = time.perf_counter()    
# print(time2 - time1)

# Same Code Using Thread
# time1 = time.perf_counter()    
# t1 = threading.Thread(target=function, args=[4])
# t2 = threading.Thread(target=function, args=[4])
# t3 = threading.Thread(target=function, args=[4])
# t1.start()
# t2.start()
# t3.start()
# time2 = time.perf_counter()    
# print(time2 - time1)

#here we are joining the time using .joint
# time1 = time.perf_counter()    
# t1 = threading.Thread(target=function, args=[4])
# t2 = threading.Thread(target=function, args=[5])
# t3 = threading.Thread(target=function, args=[1])
# t1.start()
# t2.start()
# t3.start()

# t1.join() #we will get the slowest sec as a total 
# t2.join()
# t3.join()
# time2 = time.perf_counter()    
# print(time2 - time1)

#printing them one by one 
# def poolingdemo():
#     with ThreadPoolExecutor() as executor:
#         future = executor.submit(function, 3)
#         print(future.result())
#         future = executor.submit(function, 2)
#         print(future.result())
#         future = executor.submit(function, 4)
#         print(future.result())

# poolingdemo()

#printting them combining
# def poolingdemo():
#     with ThreadPoolExecutor() as executor:
#         future1 = executor.submit(function, 3)
#         future2 = executor.submit(function, 2)
#         future3 = executor.submit(function, 4)
#         print(future1.result())
#         print(future2.result())
#         print(future3.result())

# poolingdemo()

def poolingdemo():
    with ThreadPoolExecutor() as executor:
        l =[1,2,3,4,5]
        results = executor.map(function, l)
        for result in results:
            print(result)

poolingdemo()