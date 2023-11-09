from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

class Plane(Vehicle):
    def __init__(self, make, model, year, military):
        super().__init__(make, model, year)
        self.military = military

class Boat(Vehicle):
    def __init__(self, make, model, year, porter):
        super().__init__(make, model, year)
        self.porter = porter

class RaceCar(Car):
    def __init__(self, make, model, year, doors, max_speed):
        super().__init__(make, model, year, doors)
        self.max_speed = max_speed

bmw_e39 = Car("BMW", "E39", 2004, "Black")
su30 = Plane("Su", "30", 2021, "Yes")
hanse_505 = Boat("Hanse", "505", 2014, "No")
mclaren_p1 = RaceCar("Mclaren", "P1", 2020, 2, 480)

print(bmw_e39)
print(su30)
print(hanse_505)
print(mclaren_p1)