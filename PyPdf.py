import PyPDF2

pdf_file = input("PDF file to read: ")

pdf_file_obj = open(pdf_file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

start = input("Starting page: ")
end = input("Ending page: ")
print("-" * 100)
print("PRESS CTRL+C TO STOP THE SCRIPT ANY TIME.")
print("-" * 100)

start = int(start)
end = int(end)

for page in range(start, end):
    page_obj = pdf_reader.getPage(page)


words = page_obj.extractText()
list_words = words.split()


