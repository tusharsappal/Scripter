__author__ = 'tusharsappal'

## This script changes the basic data type of python into json  and the json back to the python data structure

import json
from pprint import  pprint

def convert_into_json_and_vice_versa():

   ## This is the part where the python data structure is converted in json data
    data= {'zoo_keeper':'Yes','name':'Tushar Sappal','age':'22'}
    json_str= json.dumps(data, sort_keys=True)
    print json_str
    print  type(json_str)
    print("Here we are converting the json_data back to the python data structure ")

    data_2= json.loads(json_str)
    pprint(data_2)
    print "The conversion is complete"


convert_into_json_and_vice_versa()

