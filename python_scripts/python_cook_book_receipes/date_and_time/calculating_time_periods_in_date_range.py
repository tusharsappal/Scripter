__author__ = 'tusharsappal'

## Credits Python Cook Book Solution 3.3
## This program finds the time period in weeks between the given date range

from dateutil import rrule
import datetime

def weeks_between(start_date, end_date):
    weeks=rrule.rrule(rrule.WEEKLY,dtstart=start_date,until=end_date)
    print "The number of weeks  in the given time duration are ", weeks.count()


## Replace the arguments in the method call with the start date and the end date

weeks_between(datetime.date(2005,01,04),datetime.date(2005,01,15))