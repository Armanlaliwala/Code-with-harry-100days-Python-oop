import time
from functools import lru_cache

@lru_cache(maxsize = None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")

print(fx(50))
print("Done for 50")

print(fx(2))
print("Done for 2")
#second time this will happen instantly as it is stored in the cache memory
print(fx(20))
print("Done for 20")

print(fx(50))
print("Done for 50")

print(fx(2))
print("Done for 2")