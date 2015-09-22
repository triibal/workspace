#!/bin/env/python
# import any required libraries
# none required

### Working with Arrays

xaa = [1,1,2,3,2,2,4,5,7]
xab = [1,2,3,4,5,6]

# Find the only element in an array that only occurs once.

def uniqueCount():
    """ Find the elements in an array that occur once"""
    for f in xaa:
        count = xaa.count(f)
        if count == 1:
            print "%d appears once in the array" % f
        else:
            print "value not unique"

uniqueCount()
print uniqueCount.__doc__

# Find the most frequent integer in an array

def frequentCount():
    """ Find the most frequent integer in an array"""
    fCount = 0
    fIndex = 0
    for f in xaa:
        count = xaa.count(f)
        if count >= fCount:
            print "value for %d, %d" % (count, fCount)
            fIndex = f
            print "% is the most frequent" % f
            fCount = xaa.count(f)
        else:
            print "not most frequent"
    print "%d is the most frequent" % fIndex


frequentCount()

# Find pairs in an integer array whose sum is equal to 10

def findPairs():
    """ Find pairs in an integer array whose sum is equal to 10
    returns the pair
    """
    for f in xaa:
        for g in xaa:
            #print "values %d %d" % (f, g)
            if f + g == 10:
                print "result is %d %d" % (f, g)
            else:
                print "no match"

print "Find pairs"
findPairs()

# Find the common elements of 2 int arrays

def findCommon():
    """ Find the common elements of 2 int arrays
    returns the pair
    """
    for f in xaa:
        for g in xab:
            if f == g:
                print "%d matches %d" % (f,g)

findCommon()

# write a program that will remove elements from an array recursively

print "xaa is {}".format(xaa)
def removeRecurse():
    """ a function that will remove elements from an array recursively
    function does not return any values
    """
    if xaa != []:
        xaa.pop()
        removeRecurse()

removeRecurse()
print "xaa is {}".format(xaa)

# Write a function that prints out the binary form of an int
