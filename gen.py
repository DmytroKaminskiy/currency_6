


students = 'STRING'  # iterable
students_iterator = students.__iter__()  # iterate object

# print(id(students))
# print(id(students_iterator))

# while True:
#     try:
#         print(students_iterator.__next__())
#     except StopIteration:
#         break

# print(students_iterator.__next__())
# print(students_iterator.__next__())
# print(students_iterator.__next__())
# print(students_iterator.__next__())
# print(students_iterator.__next__())

# for student in students:
#     print(student)

# gen = [i for i in 'STRING']
# gen = {i for i in 'STRING'}
# gen = {i: i for i in 'STRING'}
# gen = (i for i in 'STRING')
# print(id(gen))
# print(id(gen.__iter__()))
# while True:
#     try:
#         print(gen.__next__())
#     except StopIteration:
#         break

# def square():
#     counter = 0
#     while True:
#         print('GEN')
#         yield counter ** 2
#         # yield counter ** 2
#         # yield counter ** 2
#         counter += 1
#         yield counter ** 3
#
#
# print(type(square))
# s = square()
# while True:
#     try:
#         print(s.__next__())
#     except StopIteration:
#         break
# for i in s:
#     print(i)
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())


# class Browser:
#     # 250 MB in memory
#     def __init__(self, param):
#         self.param = param
#
#     def start(self):
#         pass
#
# # 1Gb, browser = 10
# browsers = (Browser(i) for i in range(10))
#
# for br in browsers:
#     br.start()

# with open('Dockerfile') as file:
#     print(file.__next__())
#     print(file.__next__())
#     print(file.__next__())

# + is __add___
# == is __eq__

'''
with as
__enter__
__exit__
'''

class Connection:
    def open(self):
        print('OPEN')
        return 'CONNECTION'

    def close(self):
        print('CLOSE')

    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# try:
#     c = Connection()
#     obj = c.open()
#     print(obj)
#     1 + '1'
# finally:
#     c.close()
#
# with Connection() as obj:
#     print(obj)
# close
# from contextlib import suppress
# class Suppress:
#     def __init__(self, exc_type):
#         self.exc_type = exc_type
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exctype, excinst, exctb):
#         return exctype is not None and issubclass(exctype, self.exc_type)

# with Suppress(ZeroDivisionError):
#     1 + '1'


# from contextlib import contextmanager
#
# @contextmanager
# def Suppress2(exc_type):
#     try:
#         yield 111
#     except exc_type:
#         pass
#
# with Suppress2(TypeError) as obj:
#     print(obj)
#     1 + '1'
# from time import sleep, time

# def deco(func):
#     def wrapper():
#         return func()
#     return wrapper

def timenew(param):
    print(param)
    def timeit(func):
        def wrapper(*args, **kwargs):
            print('Before')
            result = func(*args, **kwargs)
            print('After')
            return result

        return wrapper
    return timeit


@timenew(3)
def foo(a, b):
    1 + '1'
    result = 1
    return result

# foo = timenew(3)(foo)
foo(1, 2)

def bar():
    result = 2
    return result

# bar = timeit(bar)
# bar()
# bar()
# foo()
# # bar()
# # bar()
