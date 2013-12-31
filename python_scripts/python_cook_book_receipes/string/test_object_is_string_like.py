__author__ = 'tusharsappal'

## Credits :- Python Cook Book Solution 1.3

## This script just checks whether the given string is an instance of the basestring , you can change the arguments to the isinstance method as desired to check the likability

## Replace the argument in the method call to one which you want to check
def isAStringType(str):
    if isinstance(str,basestring):
        return True
    else:
        return False





res=isAStringType("Replace for what you want to check")
print "The result of the string comparison is ", res
