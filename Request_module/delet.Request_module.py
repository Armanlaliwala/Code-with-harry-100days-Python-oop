import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Note the specific resource ID at the end

response = requests.delete(url)

print(response.status_code)
