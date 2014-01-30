__author__ = 'tusharsappal'


from urllib import urlopen
from xml.etree.ElementTree import parse

## This script fetches the xml data from the given link and displays the data

## Courtesy Python Cook Book 6.3




def parse_xml_data():
    u =urlopen('http://planet.python.org/rss20.xml')

    ## Replace the url with the actual url to be fetched

    doc=parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')


        print(title)
        print(date)
        print(link)




parse_xml_data()

