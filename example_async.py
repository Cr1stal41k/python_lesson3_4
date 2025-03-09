import httpx
import asyncio
import time

# SYNC
time_start = time.time()

def fetch_post(post_id):
    with httpx.Client() as client:
        response = client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        print(f"Post {post_id}:", response.json())

def main():
    responses = []
    for i in range(1, 6):
        responses.append(fetch_post(i))
main()

time_finish = time.time() - time_start
print(f"Time SYNC {time_finish:.2f}")

# ASYNC
time_start = time.time()

async def fetch_post(post_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        print(f"Post {post_id}:", response.json())

async def main():
    responses = []
    for i in range(1, 6):
        responses.append(fetch_post(i))
    await asyncio.gather(*responses)
asyncio.run(main())

time_finish = time.time() - time_start
print(f"Time ASYNC {time_finish:.2f}")

