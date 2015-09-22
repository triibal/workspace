#!/usr/bin/env python
# import from cars
from cars import xcar

# create class extends cars

class Truck(xcar):
    def __init__(self, Make, Tonnage):
        # super
        self.Make = Make
        self.Tonnage = Tonnage

    def getMake(self):
        return self.Make

    def setMake(self, Make):
        if not Make:
            Make = raw_input("Please provide the truck make:")
        else:
            self.Make = Make

    def getTonnage(self):
        return self.Tonnage

    def setTonnage(self, Tonnage):
        if not Tonnage:
            Tonnage = raw_input("Please provide the tonnage:")
        else:
            self.Tonnage = Tonnage


# pass some values to object

# create instance

# get values for instance

# def main

def main():
    newTruck= Truck(Make="Ford", Tonnage="30.0")
    print newTruck.getMake()
    print newTruck.getTonnage()

# call main
if __name__ == "__main__":
    main()
