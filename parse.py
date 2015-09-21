#!/usr/bin/env python
import os
current_dir = os.getcwd()
print current_dir


# open a csv and append a simple value to end of CSV
print os.stat('data.csv')
f = open('data.csv', 'r+a')
print f.readlines()
f.readline()
f.write(',test')
f.close()

#

print os.listdir(current_dir)
print os.listdir('/tmp/')
