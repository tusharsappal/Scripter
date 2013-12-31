__author__ = 'tusharsappal'


# Credits Python Cook Book Solution 3.1

# This program finds Yesterday and tomorrow using the python standard date and time module

## A general mistake that programmers do is to try subtracting and adding 1 directly to the date and time fetched by python which results in type error
## try using the datetime.timedelta method for that purpose

import datetime

def find_yesterday_tomorrow():
    today = datetime.date.today()
    yesterday= today-datetime.timedelta(days=1)
    tomorrow = today+datetime.timedelta(days=1)
    print "Yesterday was :", yesterday
    print "-------------------------"
    print "Tomorrow will be :", tomorrow


find_yesterday_tomorrow()
