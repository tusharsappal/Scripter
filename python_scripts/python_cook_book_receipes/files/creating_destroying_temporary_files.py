__author__ = 'tusharsappal'

## This python scripts creates a temporary file at the place of execution puts some data in it reads the data
## inserted into the temporary file and then destroys it

## Courtesy :- Python Cook Book Solution 5.19


from tempfile import TemporaryFile
import  os


def create_destroy_temp_files():

    print "Temporay file creation starts"
    with TemporaryFile("w+t") as f:
        f.write("Hello World this is tempoary file")
        f.write("This is another piece of line in the temporaty file")
        f.seek(0)
        for line in f.read():
            print line


    print "Temporay file is destroyed"
    f.close();




create_destroy_temp_files()
