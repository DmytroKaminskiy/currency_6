class FullName:

    def __get__(self, obj, type=None):
        return f'{obj.first_name} {obj.last_name}'


class Human:
    full_name = FullName()

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


h1 = Human('Dima', 'Kaminskyi')
print(h1.full_name)
