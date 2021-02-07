from PIL import Image
from openpyxl import Workbook
from openpyxl.styles import PatternFill, colors

im = Image.open('coomer.jpg', 'r')

pix_val = list(im.getdata())

blue_background = PatternFill(fgColor = colors.BLUE, fill_type='solid')

workbook = Workbook()
sheet = workbook.active

for i in range(1, 7):
    for j in range(1, 7):
        cell = sheet.cell(column = j, row = i)
        cell.fill = blue_background

# for row in sheet.iter_rows(min_row = 1, max_row = 2, min_col = 1, max_col = 3):
#     print(row)

workbook.save(filename = 'hello_world.xlsx')