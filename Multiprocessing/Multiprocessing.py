import multiprocessing
import requests

def downloadfile(url, name):
    response = requests.get(url)
    
    open(f"files/multi_heavy_file{name}.jpg", "wb").write(response.content) #to store in folder 
    open(f"msingle_heavy_file{name}.jpg", "wb").write(response.content) #to store 
    
url = "https://picsum.photos/200/300"    
for i in range(5):
    downloadfile(url, i)

