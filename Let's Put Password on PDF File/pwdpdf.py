import PyPDF2

file_name = "test.pdf" #enter PDF File name.

file = open(file_name,'rb')

pdf_read = PyPDF2.PdfFileReader(file)
pdf_write = PyPDF2.PdfFileWriter()

for page in range(pdf_read.numPages):
	pdf_write.addPage(pdf_read.getPage(page))

pdf_write.encrypt("PutPassword")

final_pdf = open('passwordprotected.pdf','wb')
pdf_write.write(final_pdf)

final_pdf.close()