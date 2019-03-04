import docx2txt
from docx import *
import re
import subprocess

class docparse:

        def __init__(self, filename):
                self.filename = filename
                self.filetype = re.search(r'\.{1}\w+', filename).group(0)[1:]
                self.acceptedType = ['doc', 'docx']
                if self.filetype in self.acceptedType:
                        self.status = True
                else:
                        self.status = False

        def parsedocx(self):
                docx = docx2txt.process(self.filename)
                return docx

        def parsedoc(self):
                cmd = "antiword '{}'".format(self.filename)
                doc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
                return doc.stdout.decode('utf-8')


        def parsepdf(filename):
                p = PdfFileReader(filename)
                total_pages = p.getNumPages()
                for page in range(total_pages):
#                       page_content = "\n(Page {}/{})\n".format(page, total_pages)+str(p.getPage(page).extractText())
                        page_content += str(p.getPage(page).extractTest()) + '\n'
                return page_content

        def parse(self):
                if self.status == True:
                        if self.filetype == 'doc':
                                result = self.parsedoc()
                        elif self.filetype == 'docx':
                                result = self.parsedocx()
                        elif self.filetype == 'pdf':
                                result = self.parsepdf()
                        return result
                else:
                        return "The uploaded file ({}) is not a valid filetype ({})".format(self.filename, str(self.acceptedType))
