import PyPDF2
import os
# pip install PyPDF2
# Can extract text from PDF, and can't extract int, charts, medea
os.chdir('/Users/ionbota/Documents') # change directory to get PDF from another folder
pdfFile = open('Achieve_Resolution.pdf', 'rb') # RB is read binary file

# READ NUMBER ON PAGES
reared = PyPDF2.PdfReader(pdfFile)
read = len(reared.pages)
print(read)

# READ SPECIFIC PAGE
page = reared.pages[6]
print(page.extract_text())

# READ ALL PAGES
total_pages = len(reared.pages)
for pageNum in range(total_pages):
    page = reared.pages[pageNum]  # Access the page using the newer list-like access
    text = page.extract_text()  # Extract text using the updated method name
    print(f"Text from page {pageNum + 1}:", text)


#-------#-------#------#-------#-------#

# EDIT PDF - Create NEW PDF and ad there 2 PDF in one
with open('Achieve_Resolution 2.pdf', 'rb') as pdf2File, open('Achieve_Resolution 3.pdf', 'rb') as pdf3File:
    # Create PDF reader objects
    reader2 = PyPDF2.PdfReader(pdf2File)
    reader3 = PyPDF2.PdfReader(pdf3File)

    # Create a PDF writer object using the new PdfWriter class
    writer = PyPDF2.PdfWriter()

    # Add all pages from the first PDF
    for page in reader2.pages:
        writer.add_page(page)

    # Add all pages from the second PDF
    for page in reader3.pages:
        writer.add_page(page)

    # Open a new PDF file for the output
    with open('combineminutes.pdf', 'wb') as outputFile:
        # Write the combined content to the new PDF
        writer.write(outputFile)