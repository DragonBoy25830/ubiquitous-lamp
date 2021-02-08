from PIL import Image
from openpyxl import Workbook
from openpyxl.styles import PatternFill, colors

im = Image.open('coomer.jpg', 'r')

width, height = im.size

pix_val = list(im.getdata())

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

print(pix_val[0])
print(rgb_to_hex(pix_val[0]))

workbook = Workbook()
sheet = workbook.active

for i in range(1, width + 1):
    for j in range(1, height + 1):
        for k in pix_val:
            background = PatternFill(fgColor = '00' + rgb_to_hex(k), fill_type='solid')
            break
        cell = sheet.cell(column = j, row = i)
        cell.fill = background



# workbook.save(filename = 'hello_world.xlsx')