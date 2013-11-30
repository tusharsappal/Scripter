
__author__ = 'tusharsappal'


## This script fetches the email addresses from the string provided , the script only fetches the email addresses of the format anynumberofnonwhitespacecharacters_@_anynumberofnonwhitespacecharcters

import re
def fetch_email_address(str):
    fetcher=re.findall('\S+@\S+',str)
    print fetcher


## Replace the method argument with the string to be parsed


fetch_email_address("HELLO THERE SAPPAL.TUSHAR@GMAIl.COM from sappal.tushar@hotmail.com we will be meeting at around @2pm andl aslo @4pm")





