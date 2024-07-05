from PyPDF2 import PdfReader, PdfWriter

file = './sheets/memorial_descritivo.pdf'

reader = PdfReader(file)
info = reader.metadata


