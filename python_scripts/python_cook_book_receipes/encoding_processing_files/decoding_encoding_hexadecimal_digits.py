__author__ = 'tusharsappal'

## This Script encodes and decodes the hexadecimal digits

# courtesy Python Cook Book Solution 6.9

import binascii
import base64

def  encode_decode_hexadecimal():
    ## Initial Byte String
    s=b'Hello'
    h= binascii.b2a_hex(s)

    print "The data is converted into hexadecimal values"
    print h

    print "The data is again converted back to string bytes"

    ss= binascii.a2b_hex(h)
    print ss



