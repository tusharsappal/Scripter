__author__ = 'tusharsappal'

## This script reads the file present on the given location and prints the metadata of that file
## Courtesy Python Cook Book :- Problem 5.12


import os
import time

def read_file_for_metadata():
    print(os.path.exists("/Users/tusharsappal/Desktop/com.zip"))
    print(os.path.isdir("/Users/tusharsappal/Desktop/com.zip"))
    print(os.path.getsize("/Users/tusharsappal/Desktop/com.zip"))
    print (time.ctime(os.path.getmtime("/Users/tusharsappal/Desktop/com.zip")))




read_file_for_metadata()
