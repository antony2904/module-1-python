#Implement a class hierarchy:Vehicle (base) with method start_engine().
#Car (derived) with additional method play_music().
#ElectricCar (derived from Car) with method charge_battery().
#Demonstrate creating objects and calling all relevant methods.


class Vehicle:

    def __init__(self,brand:str):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand}:Engine start")


class Car(Vehicle):

    def play_music(self):
        print(f"{self.brand}:Playing music via bluetooth.")

class ElectricCar(Car):

    def charge_battery(self):
        print(f"{self.brand}: Charging battery to 100%...")


print("--Manual car--")
manual = Car(brand = "LandCrusier")
manual.start_engine()
manual.play_music()

print("--EV.car--")
ev = ElectricCar(brand = "CyberTruck" )
ev.start_engine()
ev.play_music()
ev.charge_battery()
