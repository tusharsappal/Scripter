__author__ = 'tusharsappal'
## Credits Python Cook Book solution 3.2

## This program finds the date of the last friday , if today is friday it simply prints out today
## You can modify the program to find last any day of the week be it monday , tuesday etc
import datetime,calendar

def find_last_friday():
    lastFriday=datetime.date.today()
    one_day=datetime.timedelta(days=1)
    while lastFriday.weekday() != calendar.FRIDAY:
        lastFriday= lastFriday-one_day
    print "Last Friday was :", lastFriday.strftime('%A, %d-%b-%Y')



find_last_friday()

