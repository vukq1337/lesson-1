
class Car:
    def __init__(self, speed, model, weight):
        self.speed = speed
        self.model = model
        self.weight = weight
        self.passagers = []

    def add_passager(self, passager):
        self.passagers.append(passager)

    def show_passagers(self):
        for i in self.passagers:
            print(i)


class Person:
    def __init__(self, name, age, happiness, gender):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.money = 100000
        self.gender = gender
        self.job = None
        self.house = None

bob = Person('Bob', 23, 100, 100000)
jack = Person('Jack', 24, 44)
tom = Person('Tom', 19)
car = Car(360, 'Mercedes', 2000)
car.add_passager(bob)
car.add_passager(jack)
car.add_passager(tom)
car.show_passagers()
print(car.passagers)


def buy_car(self, car):
    if self.money >= car.price:
        self.car = car
    else:
        print('not enough money')

class job:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

class home:
    def __init__(self, area):
        self.area = area
        self.people = []
        self