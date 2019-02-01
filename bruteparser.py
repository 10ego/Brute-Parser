from PyPDF2 import PdfFileReader
import docx2txt
from docx import *
import csv
import subprocess
import os

subprocess.run("ls > filelist.csv", shell=True) #subprocess to create a list of files to parse in folder
script_dir = os.path.dirname(__file__)
output_dir = "RAW_RESULTS" #This is the subdirectory where the output raw .txt files will be saved
try:
        subprocess.run("mkdir {}".format(output_dir), shell=True)
except:
        pass
counter = 0

with open("filelist.csv") as flist:
        l = csv.reader(flist)
        filelist = [row[0] for row in l]
        docxlist = [files for files in filelist if files[-5:] == ".docx"] #array of .docx files
        doclist = [files for files in filelist if files[-4:] == ".doc"] #array of .doc files
        pdflist = [files for files in filelist if files[-4:] == ".pdf"] #array of .pdf files

def parsedocx(filename):
        global counter
        doc = docx2txt.process(filename)
        with open(os.path.join(script_dir, output_dir + "/" + filename[:-5] + ".txt"), 'w') as save:
                save.write(doc)
        counter+=1

def parsedoc(filename):
        global counter
        cmd = "antiword '{}' > '{}/{}.txt'".format(filename, output_dir, filename[:-4])
        subprocess.run(cmd, shell=True)
        counter+=1

def parsepdf(filename):
        global counter
        p = PdfFileReader(filename)
        total_pages = p.getNumPages()
        for page in range(total_pages):
                page_content = "\nPage {}/{}".format(page, total_pages)+str(p.getPage(page).extractText())
                with open(os.path.join(script_dir, output_dir + "/" + filename[:-4] + ".txt"), "a+") as save:
                        save.write(page_content)
        counter+=1


for docx in docxlist:
        print("Parsing {} of {} files: docx file {}...".format(counter+1, len(filelist), docx))
        parsedocx(docx)
        print("Completed processing file {}".format(docx))

for doc in doclist:
        print("Parsing {} of {} files: doc file {}...".format(counter+1, len(filelist), doc))
        parsedoc(doc)
        print("Completed processing file {}".format(doc))

for pdf in pdflist:
        print("Parsing {} of {} files: pdf file {}...".format(counter+1, len(filelist), pdf))
        parsepdf(pdf)
        print("Completed processing file {}".format(pdf))

print("Completed parsing total of {} files".format(len(filelist)))
