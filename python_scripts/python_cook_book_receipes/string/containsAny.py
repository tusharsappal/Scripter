__author__ = 'tusharsappal'

## This script searches for a particular string in some bigger string
def containsAny(str,sequence):
    if sequence in str:
        return True
    else:
        return  False



## Replace the first parameter to pass the string and the second parameter to send the sequence to be searched in the string
res = containsAny("EveryBody Loves Python","EveryBody")
print res


