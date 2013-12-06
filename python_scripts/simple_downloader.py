__author__ = 'tusharsappal'

import urllib
def simple_downloader():
    img = urllib.urlopen('http://www.py4inf.com/cover.jpg')
    fhand=open('/Users/tusharsappal/Desktop/cover.jpg','w')
    size=0
    while True:
        info=img.read(10000)
        if len(info)<1:
            break
        else :
            size=size+len(info)
        fhand.write(info)

    print "Size copied",size
    fhand.close()



simple_downloader()


