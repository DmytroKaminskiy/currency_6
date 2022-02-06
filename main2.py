import os


def google_analytics():
    print('google_analytics')


def yahoo_analytics():
    print('yahoo_analytics')


# def call_analytics():
#     if 'google_analytics' in os.getenv('CALLBACKS'):
#         google_analytics()
#
#     if 'yahoo_analytics' in os.getenv('CALLBACKS'):
#         yahoo_analytics()


def parse_privatbank(callbacks=None):
    if callbacks:
        for callback in callbacks:
            callback()

    # call_analytics()


callback_functions = [lambda: print('LAMBDA')]
if 'google_analytics' in os.getenv('CALLBACKS'):
    callback_functions.append(google_analytics)

if 'yahoo_analytics' in os.getenv('CALLBACKS'):
    callback_functions.append(yahoo_analytics)

parse_privatbank(callback_functions)
##################
def foo(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)

foo(*(1, 2), **{'3': 4})
# foo(1, 2, '3'=4)

foo((1, 2), {'3': 4})
# foo((1, 2), {'3': 4})

gen = (i for i in range(10_000))
print(sum(1 for _ in gen))


a = [1, 2, 3]
a2 = [1, 2, [3, 4]]

class User:
    __slots__ = ()

    def foo(self):
        print('FOO')

print(User.__mro__)
# user = User()
# print(dir(user))
