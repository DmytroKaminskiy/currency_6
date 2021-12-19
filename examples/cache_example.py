from time import sleep, time

# LEGB
'''
L - local
E - Enclosing
G - Global
B - builtins [int, str, bool, range, ]
'''

# CACHE = {}
#
# def slow(n, a):
#     global CACHE
#     key = f'slow::{n}::{a}'
#     if key in CACHE:
#         return CACHE[key]
#
#     sleep(n + a)
#     result = (n ** 2) + a
#     CACHE[key] = result
#     return result
#
# def slow2(n, a):
#     global CACHE
#     key = f'slow2::{n}::{a}'
#     if key in CACHE:
#         return CACHE[key]
#
#     sleep(n + a)
#     result = (n ** 2) - a
#     CACHE[key] = result
#     return result
#
# start = time()
# print(slow(2, 3))
# print(slow(3, 2))
# print(slow2(3, 2))
# print(slow2(3, 2))
# print(CACHE)
#
# print(f'Time: {time() - start}')
# def lru_cache(function):
#     CACHE = {}
#     def wrapper(*args, **kwargs):
#         key = f'{function.__name__}::{args}-{kwargs}'
#
#         print(CACHE)
#         if key in CACHE:
#             return CACHE[key]
#
#         from time import sleep
#         sleep(2)
#         result = function(*args, **kwargs)
#         CACHE[key] = result
#         return result
#     return wrapper
#
#
# @lru_cache
# def add(x, y):
#     return x + y
#
# print(add(2, 5))
# print(add(2, 5))