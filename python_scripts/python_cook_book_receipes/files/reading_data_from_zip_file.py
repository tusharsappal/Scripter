__author__ = 'tusharsappal'
## Credits Python Cook Book Solution 2.9
## This program reads a zip file and lists the files that constitutes the zip file and also list the size of the each file present in it.

import zipfile

def read_from_a_zip_file(file_path):
    z=zipfile.ZipFile(file_path,"r")
    for filename in z.namelist():
        print 'File :', filename,
        bytes_read = z.read(filename)
        print 'has ', len(bytes_read) ,'bytes'




## Replace the argument with the path to the zip file
read_from_a_zip_file('Path to the zip file on the machine to be read')
