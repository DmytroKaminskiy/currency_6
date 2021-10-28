lst = [1, 2, 3, 4, 5]

def foo():
    for num in lst:
        print(num)

# a = map(print, lst)

# if False:
#     print(list(a))

class Drobnuie:
    def __init__(self, c, z):
        self.c = c
        self.z = z

    def __gt__(self, other):
        return self.c > other.c

a1 = Drobnuie(1, 2)
a2 = Drobnuie(2, 3)

print(a1 > a2)
print(a1.__gt__(a2))

print(a2 > a1)
print(a2.__gt__(a1))
