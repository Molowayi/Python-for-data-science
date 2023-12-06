class Bike:
    def __init__(self) -> None:
        self.speed = 15
        self.distance = 0
    def ride(self, duration):
        self.distance += self.speed * duration

bike = Bike()
bike.ride(0.001)
bike.ride(10)
print(bike.distance)

class Car:
    def __init__(self) -> None:
        self.speed = 100
        self.distance = 0
    def ride(self, duration):
        self.distance += self.speed * duration

car = Car()     # comment renommer plusieurs occurrence d'un mot? D'une variable ou une méthode ?
car.ride(0.001)
car.ride(10)
print(car.distance)        

class Vehicule:
    def __init__(self, speed, duration) -> None:
        self.speed = 15
        self.distance = 0
    def ride(self, duration):
        self.distance += self.speed * duration
        