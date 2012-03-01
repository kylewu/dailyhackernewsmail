#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Wenbin Wu <wwu@mozilla.com>'
__date__ = '2012-02-28'


from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
#input1 = PdfFileReader(file("document1.pdf", "rb"))
outputStream = file("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
