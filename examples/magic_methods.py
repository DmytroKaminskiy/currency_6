print(1 + 1)
print(int(1).__add__(1))

print('1' + '1')
print('1'.__add__('1'))

print([1, 2].__add__([3, 4]))
print([1, 2] + [3, 4])


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __add__(self, other):
        import random

        return self.__class__(name='', color=random.choice((self.color, other.color)))

    def __enter__(self):
        print('HELLO ENTER')
        return 'aaa'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('HELLO EXIT')


cat1 = Cat('A', 'black')
cat2 = Cat('B', 'white')
cat3 = Cat('C', 'red')
cat4 = Cat('D', 'grey')

cat_new = cat1 + cat2 + cat3 + cat4 + cat1
cat_new2 = cat1.__add__(
    cat2.__add__(
        cat3.__add__(
            cat4.__add__(cat1)
        )
    )
)
print(cat_new.color)


with cat1 as aaa:
    print(aaa)
