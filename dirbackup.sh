#!/bin/bash

# Script to make back-up copies
# of files in current directory

TIME=`date + "%F"`
CURDIR=`pwd`
ORIGFILES=`ls`
UNWANTED="bak"
BACKUPFILE="backup-$TIME.tar.bz2"
DESDIR="/home/root/backups"

echo "Getting ready to back up $CURDIR"

if[[ $ORIGFILES =~ $UNWANTED ]] #matched
  then
  echo "Already backed up - what now?"; exit 1
else
  for f in $ORIGFILES
  do
    cp $f $f.bak
  done
fi
