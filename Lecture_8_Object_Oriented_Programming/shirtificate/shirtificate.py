'''
Completion of the CS50P assignemnt without using OOP. Another alternative will be provided for using OOP to create a PDF class to use with the FPDF library
'''

from fpdf import FPDF

name = input("Name: ")

# Set orientation to portrait (P), unit in mm and size (format) as A4
pdf = FPDF(orientation = "P", unit = "mm", format = "A4")

# Add page with call to add-page from fpdf class
pdf.add_page()

# Set font with call to set_font module, and set font as Times New Roman, set bold and set size as 20
pdf.set_font('Times', "B", size=40)

# Import image and add to a few lines lower from heading
pdf.image('shirtificate.png', x= "C", y=65)


# Place CS50 Shirtificate text at the top of the page before inserting image
#pdf.cell(200, 35, txt="CS50 Shirtificate", align="C")
pdf.multi_cell(200,35, align="C", txt = "CS50 Shirtificate")

# Import image and add to a few lines lower from heading
#pdf.image('shirtificate.png', x= "C", y=65)

# Set font attributes and Place Name and text at the top of the image in white colour
pdf.set_font('helvetica', size = 28)
pdf.set_text_color(255,255,255)
pdf.text(55,140, txt = f"{name} took CS50")


# Output pdf file with shirtificate name
pdf.output("shirtificate.pdf")

