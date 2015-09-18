#!/bin/bash

# route class should compare drivers with passengers classes to determine closest radius
# should dispatch driver to passengers

import cars

class route(object):
    def __init__(self):
        self.id = 0
        #latitude longtitude pair
        self.pair = [0, 0]
        self.radius = 5
        self.driverOnline = 1
        self.passengerOnline = 1
        self.orderStatus = 0.25

# define setter and getter for remote_addr_w_port
    def getRadius(self):
        print self.radius
        return self.radius

    def setRadius(self):
        print "enter a value for the new radius"
        tempRadius = raw_input()
        self.radius = int(tempRadius)

newRoute = route()
newRoute.getRadius()
newRoute.setRadius()

newCar = cars.xcar()

newCar.getPassengers()
newCar.setPassengers()
newCar.getPassengers()
