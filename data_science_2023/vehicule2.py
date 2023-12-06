class Vehicule:
    def __init__(self, speed) -> None:
        self.speed = speed
        self.distance = 0
    def ride(self, duration):
        self.distance += self.speed * duration
        
class Bike(Vehicule):
    def __init__(self) -> None:
        super().__init__(15)
        self.fuel = 100
        self.consumption = 0.05
    def ride(self, duration):
        super().ride(duration)
        self.fuel -= self.consumption +self.speed * duration
        