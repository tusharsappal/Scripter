__author__ = 'tusharsappal'

## This Script turns the dictionary into a xml document

## Courtesy Python Cook Book Solution  6.5
from xml.etree.ElementTree import Element

def turn_dict_into_xml(tag,d):
    elem = Element (tag)
    for key, val in d.items():
        child= Element(key)
        child.text= str(val)
        elem.append(child)

    return elem



turn_dict_into_xml("Tag to be created of ", "Dictionary Instance to be passed")

