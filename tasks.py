# task 1

def split(values, number):
    for i in range(number):
        for j in range(number):
           pass
    return []

assert split([1, 2, 3, 4], 2) == [
    [1, 2],
    [3, 4],
]
assert split([1, 2, 3, 4, 5, 6], 2) == [
    [1, 2],
    [3, 4],
    [5, 6],
]
assert split([1, 2, 3, 4, 5, 6], 3) == [
    [1, 2, 3],
    [4, 5, 6],
]
assert split([1, 2, 3, 4, 5], 3) == [
    [1, 2, 3],
    [4, 5],
]
assert split([1, 2, 3, 4, 5], 2) == [
    [1, 2],
    [3, 4],
    [5, ],
]
assert split([1, 2, 3, 4, 5], 10) == [
    [1, 2, 3, 4, 5],
]

# '''
# Rate
# C POST - create
# R GET - read
# U PUT/PATCH - update
# D DELETE - delete
# '''