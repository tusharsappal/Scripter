__author__ = 'tusharsappal'

## Credits Python Cook Book solution 2.24
## This script returns the number of the pages in the pdf document on Mac 10.3 or later versions

import CoreGraphics
def count_pages_in_pdf_document(path_to_the_pdf_doc_on_mac):
    pdf =CoreGraphics.CGPDFDocumentCreateWithProvider(
        CoreGraphics.CGDataProviderCreateWithFilename(path_to_the_pdf_doc_on_mac)
    )
    return pdf.getNumberOfPages()

## Replace the argument in the method call with the path of the pdf doc to be used
no_of_pages=count_pages_in_pdf_document('Path to the pdf document to be used')
print "The number of pages in the pdf document is ",no_of_pages