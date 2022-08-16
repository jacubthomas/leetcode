"""
Just familiarizing with some OOP for Python3
"""
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
import string

class Vehicle:
    def __init__ (self,
                make: string = "BMW",
                model: string = "M4",
                year: int = "2022", 
                fast: bool = True):
        self.make = make
        self.model = model
        self.year = year
        self.fast = fast

    def __str__ (self) -> str:
        canitgo = "Hell yeah!" if self.fast else "Nope." 
        txt = f"My car is a {self.year} {self.make} {self.model}. Is it fast? {canitgo}"
        return txt
    
    def __lt__(self, other) -> bool:
        if self.make == other.make:
            return self.model < other.model
        else:
            return self.make < other.make
        
    def __eq__(self, other) -> bool:
        return self.make == other.make

class Car(Vehicle):
    def __init__ (self,
                make: string = "BMW",
                model: string = "M4",
                year: int = "2022", 
                fast: bool = True,
                seats: int = 4, 
                doors: int = 4, 
                fuel_type: string = "Gas"):
        super().__init__(make, model, year, fast)
        self.seats = seats
        self.doors = doors
        self.fuel_type = fuel_type
        
    def __str__ (self) -> str:
        canitgo = "Hell yeah!" if self.fast else "Nope." 
        green = "Nope. It's a gas guzzler." if self.fuel_type == "Gas" else f"Yep, it's {self.fuel_type}."
        canwecome = "No room" if self.seats < 4 else "Sure, climb in!"
        txt = f"My car is a {self.year} {self.make} {self.model}. Is it fast? {canitgo}"
        txt += f" Is it green? {green} Can we come? {canwecome}"
        return txt


BMW = Vehicle()
print (BMW)

Honda = Vehicle ("Honda", "Civic", 2011, False)
print (Honda)

Hummer = Car("Hummer", "H2", 2001, False, 6, 4, "Gas")
print (Hummer)

eHummer = Car("Hummer", "EV Pickup", 2001, True, 6, 4, "Electric")
print (eHummer)

Rivian = Car("Rivian", "R1T", 2022, True, 5, 4, "Electric")
print (Rivian)

Toyota = Car("Toyota", "Prius", 2015, False, 5, 4, "Hybrid")
print (Toyota)
print ()
Garage = [eHummer, Toyota, Rivian, Hummer, BMW, Honda]

print ("Garage: ", end='')
for x in Garage:
    print (f"{x.make} {x.model}, ", end='')
print ()

print ("Sorted Garage: ", end='')
for x in sorted(Garage):
    print (f"{x.make} {x.model}, ", end='')
print ()
print ()

print("Is BMW == Honda: ", BMW.__eq__(Honda))
print("Is Hummer == eHummer: ", Hummer.__eq__(eHummer))