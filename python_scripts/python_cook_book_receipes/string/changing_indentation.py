__author__ = 'tusharsappal'

##Credits Python Cook Book solution no 1.14
## This script changes the indentation of the text to a fixed number of indentations


def changeIndentation(indexCount,s):
    leadingspaces=indexCount*" "
    lines= [leadingspaces + line.strip()
           for line in s.splitlines()]
    return '\n'.join(lines)


print changeIndentation(4,""" line one
line two
     and line three""")

