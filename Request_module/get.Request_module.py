import requests
respond = requests.get("http://google.com/")
print(respond.text)