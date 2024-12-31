import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Note the specific resource ID at the end
data = {
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    'content-type': "application/json; charset=UTF-8"
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
