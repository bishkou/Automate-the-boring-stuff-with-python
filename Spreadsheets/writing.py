import openpyxl


wb = openpyxl.Workbook()
sheet = wb.active
i = 0
titles = ['Gender', 'Category', 'Name', 'Price', 'Link', 'ImageLink']


for i in range(len(titles)):
    sheet.cell(row=1, column=i+1).value = titles[i]


wb.save('ex.xlsx')