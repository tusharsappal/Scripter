__author__ = 'tusharsappal'

## Credits Python Cook Book Solution 2.4


## This script reads a particular line from the text file
## Replace the first parameter with the path to the file and the second parameter with the line number to be fetched
import linecache
def read_specific_line(path_to_file,line_number):
    theLine=linecache.getline(path_to_file,line_number)
    print theLine


read_specific_line('The Path to the text file including the file it self ',"The value of the line number to be fetched in numeral form")




