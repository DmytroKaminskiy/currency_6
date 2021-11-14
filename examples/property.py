# from datetime import date, datetime
#
#
# class Human:
#     def __init__(self, first_name, last_name, dob):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.dob = dob
#
#     def get_full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     @property
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     @property
#     def age(self):
#         days = (datetime.today().date() - self.dob).days
#         return int(days / 365)
#
#
# h1 = Human(
#     'Dmytro',
#     'Kaminskyi',
#     date(1992, 1, 23),
# )
# h2 = Human(
#     'Alex',
#     'R',
#     date(1993, 8, 8),
# )
#
# print(h1.get_full_name())
# print(h1.age)
# print(h2.get_full_name())
# print(h2.age)


########################

from datetime import date, datetime


class Human:
    def __init__(self, first_name):
        self.__first_name = first_name

    @property  # getter
    def first_name(self):
        print('first_name.getter')
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        print('first_name.setter')
        self.__first_name = value.strip().capitalize()

    @first_name.deleter
    def first_name(self):
        print('first_name.deleter')
        self.__first_name = None

h1 = Human('Dmytro')
h1.first_name = '   alex  '
print(h1._Human__first_name)
del h1.first_name
print(f'First name: {h1.first_name}')