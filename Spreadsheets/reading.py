import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

print(wb.sheetnames)

sheet = wb['Sheet1']

for elt in sheet['A1':'C3']:
    for cell in elt:
        print(cell.coordinate, cell.value)
    print('end of row')