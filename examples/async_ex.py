import time


def foo():
    print('One')
    time.sleep(1)
    print('Two')


# start = time.time()
#
# for _ in range(3):
#     foo()
#
# print(f'Took: {time.time() - start}')
# import asyncio
#
# async def foo_async():
#     print('One')
#     await asyncio.sleep(1)
#     print('Two')
#
# async def main():
#     await asyncio.gather(foo_async(), foo_async(), foo_async())
#
# start = time.time()
# asyncio.run(main())  # event loop
# print(f'Took: {time.time() - start}')

# def foo_generator():
#     for i in range(3):
#         print('1')
#         yield i
#
# for j in foo_generator():
#     print('2')
#     # print(j)


# URLS = [
#            'https://pythontutor.com/visualize.html#mode=display',
#            'https://pythontutor.com/',
#            'https://pythontutor.com/visualize.html#mode=display',
#            'https://pythontutor.com/',
#        ] * 20

# start = time.time()
import requests


def fetch_sync(url: str) -> None:
    response = requests.get(url)
    print(response.status_code)


# for url in URLS:
#     fetch_sync(url)
#
# print(f'Took: {time.time() - start}')


# start = time.time()
# from threading import Thread
# threads = []
# for url in URLS:
#     th = Thread(target=fetch_sync, args=[url])
#     th.start()
#     threads.append(th)
#
# for th in threads:
#     th.join()
#
# print(f'Took: {time.time() - start}')
import httpx
import asyncio

URLS = [
           'http://localhost:8000',
       ] * 20

async def fetch_async(url: str) -> None:
    print('1')
    async with httpx.AsyncClient() as client:
        r = await client.get(url, timeout=30.0)
        print('2')

async def main():
    tasks = []
    for url in URLS:
        tasks.append(fetch_async(url))
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())  # event loop
print(f'Took: {time.time() - start}')