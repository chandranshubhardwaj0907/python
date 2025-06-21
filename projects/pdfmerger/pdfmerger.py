from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("Enter the number of PDFs to merge: "))

for i in range(n):
    pdf = input(f"Enter the name of PDF {i + 1}: ")
    pdfs.append(pdf)  # ✅ Corrected from 'name' to 'pdf'

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
