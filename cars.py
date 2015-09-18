#!/usr/bin/python
# python cars file for uber

# if there are 1000 drivers who want to earn 200 and they must complete 35 trips
# and there are 25000 trips in a given day and 600 drivers earn 200
# calculate the average earnings of the other drivers
# and the surge pricing required for the other drivers to earn 200

drivers = 1000
riders = 25000

def remainingTrips():
    remainder = riders - (drivers*.6)*35
    avgEarnings = 200.00/35.00
    print remainder
    print avgEarnings
    surgeTarget = 400 * 200
    lowTarget = remainder * avgEarnings
    deltaTarget = surgeTarget - lowTarget
    print deltaTarget
    surgePrice = surgeTarget / lowTarget
    print surgePrice

remainingTrips()

# supply and demand for surge pricing on Uber
# work out when the surge price should take effect
# given a current number of drivers and riders, what if riders suddenly spikes at certain times

# 500 drivers
# 500 riders every 6 minutes
# 2000 riders peak
# avg wait time of 3 minutes
# avg trip time of 5 minutes
# work out how many trips cab be completed within 1 hour
# work out surge pricing


class xcar(object):
    def __init__(self):
        self.passengers = 0
        self.location = [14.11, 13.11]
        direction = ['NW']
        driverOnline = 1
        hoursLoggedIn = 3
        lastFare = 0.25
        lastFareValue = 8.50

# define setter and getter for remote_addr_w_port
    def getPassengers(self):
        print self.passengers
        return self.passengers

    def setPassengers(self):
        print "enter a value for the passengers"
        tempPassengers = raw_input()
        self.passengers = int(tempPassengers)

# route optimization and other cool stuff
