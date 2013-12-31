__author__ = 'tusharsappal'


## This program demonstrates the general example of list comprehension
## To demonstrate this we would be incrementing each item in the list by 25 considering a list of integer items
## credits python cook book solution 4.2

def list_comprehension(list_obj):
    the_new_list=[x+25 for x in list_obj]
    ## now printing each element of the new list
    for x in the_new_list:
        print x


## This is sample list to be edited
a=[2,5,6,7,8,9,10]

list_comprehension(a)
