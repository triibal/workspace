#!/usr/bin/env python

# this is a shameful comment
# another shameful comment
# working on workspace beta

#import needed libraries
import zipfile
import sys
import os
import logging

logging.basicConfig(filename="file_ex.log", level = logging.DEBUG)

logging.info("checking to see if the backup.zip file exists")

if os.path.exists("backups.zip"):
    logging.info("it exists!")
    try:
        # use zipfile to open file instead of os.file
        zip_file = zipfile.ZipFile("backup.zip",'a')
    except:
        err = sys.exe_info()
        logging.error("Unable to open backup.zip in append mode")
        logging.error("Error Num:" + str(err[1].args[0]))
        logging.error("Error Msg: " + err[1].args[1])
        sys.exit()
else:
    logging.info("creating backup.zip")
    try:
        zip_file = zipfile.ZipFile("backup.zip", "w")
    except:
        err = sys.exe_info()
        logging.error("Unable to create backup.zip in write mode")
        logging.error("Error Num:" + str(err[1].args[0]))
        logging.error("Error Msg: " + err[1].args[1])
        sys.exit()

logging.info("adding text.txt to backup.zip")

try:
    zip_file.write('test.txt','test', zipfile.ZIP_DEFLATED)

except:
    err = sys.exe_info()
    logging.error("Unable to add test to backups.zip")
    logging.error("Error Num:" + str(err[1].args[0]))
    logging.error("Error Msg: " + err[1].args[1])

zip_file.close()
