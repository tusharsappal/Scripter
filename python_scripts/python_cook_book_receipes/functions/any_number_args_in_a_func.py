__author__ = 'tusharsappal'

## Courtesy Python cook Book  7.1
## This script accepts  any number of arguments and prints the average of the values
## The type of arguments should be similar 



def any_num_args(first, *rest):
    avg = (first+sum(rest))/(1+len(rest))
    print avg



## Example Call number 1
any_num_args(1,2,3,4,5)

## Example Call number 2
any_num_args(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)



