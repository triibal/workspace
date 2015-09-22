#!/bin/bash
# find the location with the largest number of files, usually taking a lot of inodes
find / -xdev -printf '%h\n' | sort | uniq -c | sort -k 1 -n
