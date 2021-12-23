from time import sleep, time
import threading

import requests


def slow(n):
    sleep(n)

# urls = [
#     'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
#     'https://wikimediafoundation.org/',
#     'https://wikimediafoundation.org/technology/',
# ]
# start = time()
#
# def foo(url_):
#     print(threading.current_thread())
#     response = requests.get(url_)
#     # print(response.status_code)
# print(threading.current_thread())
# threads = []
# for url in urls:
#     th = threading.Thread(target=foo, args=[url])
#     th.start()
#     threads.append(th)
#
# for th in threads:
#     th.join()
#
# print(f'Execute: {time() - start}')
# start = time()
# for url in urls:
#     response = requests.get(url)
#     print(response.status_code)
# print(f'Execute: {time() - start}')
# start = time()
# threads = []
# for t in range(1, 11):
#     th1 = threading.Thread(target=slow, args=[t])  # slow(4)
#     threads.append(th1)
#     th1.start()
#
# for th in threads:
#     th.join()
# print(f'Execute: {time() - start}')

# start = time()
# slow()
# slow()
# slow()
# print(f'Execute: {time() - start}')
# GIL - global Interpreter Lock
# from multiprocessing import Process, current_process
# def countdown(n):
#     print(current_process())
#     while n:
#         n -= 1
#
# start = time()
# print(current_process())
# th1 = Process(target=countdown, args=[250_000_000])
# th11 = Process(target=countdown, args=[250_000_000])
# th2 = Process(target=countdown, args=[250_000_000])
# th22 = Process(target=countdown, args=[250_000_000])
#
# th1.start()
# th11.start()
# th2.start()
# th22.start()
#
# th1.join()
# th11.join()
# th2.join()
# th22.join()
# print(f'Execute: {time() - start}')
# from multiprocessing import Pool
# urls = [
#     'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
#     'https://wikimediafoundation.org/',
#     'https://wikimediafoundation.org/technology/',
# ] * 100
# def foo(url_):
#     response = requests.get(url_)
#
# start = time()
# with Pool(20) as p:
#     print(p.map(foo, urls))
# print(f'Execute: {time() - start}')

# from multiprocessing import Process, Queue
# from time import sleep
# urls = [
#     'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
#     'https://wikimediafoundation.org/',
#     'https://wikimediafoundation.org/technology/',
# ] * 100
# que = Queue()
#
# import requests
#
# def foo(queue):
#     while True:
#         u = queue.get()
#         if u is None:
#             break
#         print(f'foo: {u}')
#         requests.get(u)
#
# pr = Process(target=foo, args=[que])
# pr2 = Process(target=foo, args=[que])
# pr.start()
# pr2.start()
#
# for url in urls:
#     print(f'send to foo: {url}')
#     que.put(url)
# que.put(None)
# que.put(None)
#
# def f(q):
#     q.put([42, None, 'hello'])
#
# p = Process(target=f, args=(q,))
# p.start()
# print(q.get())    # prints "[42, None, 'hello']"
# p.join()

import sys
from threading import Thread
from multiprocessing import Process

def slow(n):
    sleep(n)

worker_type = sys.argv[1]
if worker_type == 'fork':
    concurrency_class = Process
elif worker_type == 'thread':
    concurrency_class = Thread


urls = [
    'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0',
    'https://wikimediafoundation.org/',
    'https://wikimediafoundation.org/technology/',
] * 100
start = time()

def foo(url_):
    response = requests.get(url_)

threads = []
print(concurrency_class)
for url in urls:
    th = concurrency_class(target=foo, args=[url])
    th.start()
    threads.append(th)

for th in threads:
    th.join()
