__author__ = 'tusharsappal'

## Credits the Python Cook book solution 2.15
## This program converts the file like object to the file object
import types,tempfile
CHUNK_SIZE=16*1024
def adapt_file_like_to_true(file_like_object):
    if isinstance(file_like_object,file):
        return file_like_object
    tmpfileObj =tempfile.TemporaryFile
    while True:
        data = file_like_object.read(CHUNK_SIZE)
        if not data :break
        tmpfileObj.write(data)
    file_like_object.close()
    tmpfileObj.seek(0)
    return tmpfileObj

## Replace the parameter in the method call to the object to be tested

adapt_file_like_to_true('the File like object to be tested and converted to file object')





