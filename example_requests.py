import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# GET-запрос
response = requests.get(url)
print(response.status_code)
print(response.json())

# POST-запрос
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)
print(response.json())

