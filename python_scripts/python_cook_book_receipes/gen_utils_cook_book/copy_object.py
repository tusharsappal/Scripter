__author__ = 'tusharsappal'


## This program demonstrates how to use the inbuilt copy method of the standard python library
## Credits Python Cook Book Solution 4.1
import copy

def copy_object(old_object):
    new_obj = copy.copy(old_object)
    ## For deep copying i.e copying all the items  and the attributes use the copy.deepcopy method
    print "Is Copy Successful (True/False)", new_obj is old_object



## Change the argument in the method call as required
copy_object("Tushar Sappal")


