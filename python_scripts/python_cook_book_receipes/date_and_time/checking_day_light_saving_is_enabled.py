__author__ = 'tusharsappal'

## Credits Python Cook Book solution 3.8

## This program checks for whether the day light saving is enabled or not on your local time zone


import time
def is_day_light_enabled():
    return bool(time.localtime().tm_isdst)



print "Day light Saving is enabled  (True/False) :", is_day_light_enabled()
