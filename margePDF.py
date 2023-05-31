import fitz
import glob
import os

Dir = "G:\\My Drive\\Research\\LaTeX\\marge"

files = glob.glob(Dir + "/*.pdf")
sfiles = sorted(files)
doc = fitz.open()

for file in sfiles:
    infile = fitz.open(file)
    doc_lastPage = len(doc)
    infile_lastPage = len(infile)
    doc.insert_pdf(infile, from_page=0, to_page=infile_lastPage, start_at=doc_lastPage, rotate=0)
    infile.close()

doc.save(Dir + "/marge.pdf")