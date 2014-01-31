__author__ = 'tusharsappal'


## courtesy Python Cook Book 7.6


## This script simply demonstrates the use of inline methods in python programing language using the concept of addition

## In LIne methods are small methods to perform one line computation, use of lambda

def inline_computation():
    addition = lambda x,y: x+y
    p=addition(2,3)
    print p



inline_computation()



