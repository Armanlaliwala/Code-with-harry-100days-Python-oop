import requests

url = "https://jsonplaceholder.typicode.com/posts"  # Corrected URL
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    'content-type': "application/json; charset=UTF-8"
}

response = requests.post(url, headers=headers, json=data)

print(response.text)     #this both will print the dict
# print(response.json()) #this both will print the dict
