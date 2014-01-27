__author__ = 'tusharsappal'

## This Script searches for files in  the directory listing in a directory and prints their name appending the complete path along with the parent directory

## Courtesy Python Cook Book Solution :-5.13



import os

def get_directory_structure_of_a_folder(path_to_be_fetched):
    for name in os.listdir(path_to_be_fetched):
        name = os.path.join(path_to_be_fetched,name)
        print name



## Replace the argument in the method call with the path to be searched (Try putting / or \\ in the path separators)


get_directory_structure_of_a_folder("path_to_be_searched")