
class Car:
    def __init__(self, speed, model, weight):
        self.speed = speed
        self.model = model
        self.weight = weight
        self.passangers = []

    def add_passanger(self, passanger):
        self.passangers.append(passanger)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Person('Bob', 23)
car = Car(360, 'Mercedes', 2000)
car.add_passanger(bob)
print(car.passangers)