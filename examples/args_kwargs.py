def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo((1, 2, 3), {'a': 'b'})
foo(*(1, 2, 3), **{'a': 'b'}, **{'b': 'c'})  # -> foo(1, 2, 3, a='b')
