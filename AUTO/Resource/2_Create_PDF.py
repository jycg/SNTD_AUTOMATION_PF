from reportlab.pdfgen import canvas

# create a new PDF File
pdf_file = canvas.Canvas("example.pdf")
text = "una variable más"

# add text to the file PDF file
pdf_file.drawString(72, 800, "Hello, World!" + text)
pdf_file.drawString(72, 700, "Fire PDF Document")
pdf_file.drawString(72, 680, "Like | Share")
pdf_file.drawString(72, 660, "Subscribe")
pdf_file.drawString(72, 640, "ejemplo más")

# save the PDF file
pdf_file.save()
