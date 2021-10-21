# Inheritance

class Human:
    def __init__(self, fn, age):
        self.fn = fn
        self.age = age


class Student(Human):  # Student is Human
    def __init__(self, fn, age, grade):
        self.grade = grade
        super().__init__(fn, age)


class Teacher(Human):  # Teacher is Human
    def __init__(self, fn, age, exp):
        self.exp = exp
        super().__init__(fn, age)


s1 = Student('Dima', 29, 3)
t1 = Teacher('Alex', 27, 7)

# print(s1.grade, s1.age)
# print(t1.exp, t1.age)


######################
'''
has
Car has engine
Aggregation/composition
'''

class Car:
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine


class EngineBase:
    pass

class EngineGas(EngineBase):
    def __init__(self, volume, power):
        self.volume = volume
        self.power = power

    def info(self):
        return f'Volume: {self.volume}, Power: {self.power}'


class EngineElectro(EngineBase):
    def __init__(self, power, capacity):
        self.power = power
        self.capaci9ty = capacity

    def info(self):
        return f'Power: {self.power}, Capacity: {self.capacity}'

import sys

engine_type = sys.argv[1]

if engine_type == 'gas':
    engine = EngineGas(volume='2.4', power='134')
elif engine_type == 'electro':
    engine = EngineElectro(power='200W', capacity='500P')

car1 = Car(
    color='red',
    engine=engine,
)

print(car1.color, car1.engine.info())

'''
is - Inheritance
has - aggregation
'''

###########################
class A:
    def __init__(self):
        self.foo = 1
