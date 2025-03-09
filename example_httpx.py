import httpx

url = "https://jsonplaceholder.typicode.com/posts/1"

# GET-запрос
with httpx.Client() as client:
    response = client.get(url)
    print(response.status_code)
    print(response.json())

# POST-запрос
data = {"title": "foo", "body": "bar", "userId": 1}
with httpx.Client() as client:
    response = client.post("https://jsonplaceholder.typicode.com/posts", json=data)
    print(response.status_code)
    print(response.json())