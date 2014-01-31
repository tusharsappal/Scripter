__author__ = 'tusharsappal'

import webbrowser

## courtesy Python Cook Book Solution 13.15
## This script launches the web browser and opens the url http://google.com


def launch_web_browser(url):

    webbrowser.open_new(url)



## Replace the url to be opened through the web browser
launch_web_browser("http://www.google.com")