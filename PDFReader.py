# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 05:36:53 2021

@author: dell
"""

import PyPDF2

with open('Meeting.pdf','rb') as my_file:
    print(my_file)
    reader = PyPDF2.PdfFileReader(my_file)
    print(reader.numPages)
    #print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as file:
        writer.write(file)