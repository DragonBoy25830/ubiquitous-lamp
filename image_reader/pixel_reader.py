from PIL import Image
from openpyxl import Workbook
from openpyxl.styles import PatternFill, colors

base_width = 225
im = Image.open('coomer.png', 'r')

wpercent = (base_width / float(im.size[0]))
hsize = int((float(im.size[1]) * float(wpercent)))
img = im.resize((base_width, hsize), Image.ANTIALIAS)
img.save('coomer_resized.jpg')

width, height = img.size
pix_val = img.getdata()

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


workbook = Workbook()
sheet = workbook.active

counter = 0

for i in range(1, height + 1):
    for j in range(1, width + 1):
        color = pix_val[counter]
        counter += 1
        background = PatternFill(fgColor = '00' + rgb_to_hex(color)[1:], fill_type='solid')
        cell = sheet.cell(column = j, row = i)
        cell.fill = background

# background = PatternFill(fgColor = '00' + rgb_to_hex((122, 104, 119))[1:], fill_type='solid')
# cell = sheet.cell(column = 1, row = 1)
# cell.fill = background

workbook.save(filename = 'hello_world.xlsx')