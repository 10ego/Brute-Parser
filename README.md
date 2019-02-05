# Brute-Parser

Text parser script for various files, currently supporting .docx, .doc, and .pdf.

Place all the files that needs to be parsed into a single directory together with this script file.

This script will parse all supported file formats into .txt output and save it into a subdirectory "RAW_RESULTS" that will be automatically generated relative to where this script is ran from.

## Relies on the following:

.doc - [antiparse](http://www.winfield.demon.nl/)

.docx - [doc2txt](https://github.com/ankushshah89/python-docx2txt)

.pdf - [PyPDF2](https://github.com/mstamy2/PyPDF2)
