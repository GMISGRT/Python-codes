#Example 1 - Vertical Bar Charts

import openpyxl

from openpyxl.chart import BarChart, Reference

wb = openpyxl.load_workbook('D:\Book1.xlsx')

sheet = wb.active

values = Reference(
    sheet,
    min_col=4,
    max_col=4,
    min_row=1,
    max_row=11
)

cats = Reference(sheet, min_col=2,max_col=2,min_row=2,max_row=11)

#create a object of BarChart

chart = BarChart()

chart.add_data(values, titles_from_data=True) 

chart.set_categories(cats)

chart.x_axis.title="Products"

chart.y_axis.title="Inventory Per Product"

sheet.add_chart(chart,"F2")

wb.save('D:\qwerty.xlsx')