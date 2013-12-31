__author__ = 'tusharsappal'


## This script returns an element present at a specific index in a list
## credits python cook book 4.3

def return_element_at_a_specific_index_of_list(lis_to_be_searched,index):
    v=None
    if -len(lis_to_be_searched)<=index<len(lis_to_be_searched):
        return lis_to_be_searched[index]
    else:
        return  v




## Replace the method call  parameters with the list and the index to be searched
a=[2,3,4,5,6,7,8,9,10,11,12]
index=-3
res=return_element_at_a_specific_index_of_list(a,index)
print res