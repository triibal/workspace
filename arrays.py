#!/bin/env/python
# import any required libraries

# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html

# http://www.thegeekstuff.com/2013/11/linux-process-and-threads/

# http://www.thegeekstuff.com/2010/11/50-linux-commands/

# http://www.mulix.org/lectures/kernel_workshop_mar_2004/things.pdf

# think of idempotency and boundary conditions

#from subprocess import call
#call(["ls", "-l"])

#patrick = call(["ls"])

#print patrick

#print patrick

### Working with Arrays


xaa = [1,1,2,3,2,2,4,5,7]
xab = [1,2,3,4,5,6]

# for f in xaa:
#    print f

# Find the only element in an array that only occurs once.

def uniqueCount():
    for f in xaa:
        count = xaa.count(f)
        if count == 1:
            print "%d appears once in the array" % f
        else:
            print "value not unique"

uniqueCount()

# Find the most frequent integer in an array


def frequentCount():
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

# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

#!/bin/env/python
# import any required libraries

# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html

# http://www.thegeekstuff.com/2013/11/linux-process-and-threads/

# http://www.thegeekstuff.com/2010/11/50-linux-commands/

# http://www.mulix.org/lectures/kernel_workshop_mar_2004/things.pdf

# think of idempotency and boundary conditions

#from subprocess import call
#call(["ls", "-l"])

#patrick = call(["ls"])

#print patrick

#print patrick

### Working with Arrays


xaa = [1,1,2,3,2,2,4,5,7]
xab = [1,2,3,4,5,6]

# for f in xaa:
#    print f

# Find the only element in an array that only occurs once.

def uniqueCount():
    for f in xaa:
        count = xaa.count(f)
        if count == 1:
            print "%d appears once in the array" % f
        else:
            print "value not unique"

uniqueCount()

# Find the most frequent integer in an array


def frequentCount():
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

# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)

def findPairs():
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
    for f in xaa:
        for g in xab:
            if f == g:
                print "%d matches %d" % (f,g)

findCommon()

# strings
print xaa.pop()
xaa.append(1)
xaa.append(7)
xaa.pop()
print xaa
xaa.length()

# Write a function that prints out the binary form of an int
