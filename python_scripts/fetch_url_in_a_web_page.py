import urllib
import re

def find_hyper_links_in_page():
    url = raw_input("Enter the url to be searched--")
    html =urllib.urlopen(url).read()
    links =re.findall('href="(http://.*?)"', html)
    for link in links:
        print link





find_hyper_links_in_page()