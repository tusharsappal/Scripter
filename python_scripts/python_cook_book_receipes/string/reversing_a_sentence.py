__author__ = 'tusharsappal'

## Credits Python Cook Book Solution 1.7
## This script just reverses the order of the occurrence of the words in the string


def reverse_a_sentence(str):


    revwords = str.split()    ## stirng --> list of words
    revwords.reverse()        ## reversing the list
    revwords= ' '.join(revwords)  ## joining the list of reversed list of strings
    print revwords


## Replace the string with spaces to reverse the order of the string
reverse_a_sentence("Every body just loves PYTHON")
