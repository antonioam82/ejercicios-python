import pandas as pd

#CREAR DATAFRAME
data = {'col_A':[1, 2, 3], 'col_B':[1, 2, 3], 'col_c':[1, 2, 3], 'col_D':[1, 2, 3], 'col_E':[1, 2, 3]}
df = pd.DataFrame(data)
print(df)

#INICIALIZAR WRITER
writer = pd.ExcelWriter('Example.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Example Sheet', index = False)

#INICIALIZAR FORMATO.
workbook = writer.book

#REOP
worksheet = writer.sheets['Example Sheet']

#HEADER FORMAT
header_format = workbook.add_format()
header_format.set_center_across(True)
header_format.set_bold(True)
header_format.set_font('Courier New')

#FORMATO DE CELDA
cell_format = workbook.add_format()
cell_format.set_font('Courier New')

#ANCHO DE 15 PARA COLUMNS A - C Y 20 PARA 20 PARA D.
worksheet.set_column('A:C', 15, cell_format)
worksheet.set_column('D:D', 20, cell_format)

for col in ['A', 'E']:
    worksheet.set_column(f'{col}:{col}', 5, cell_format)

#GUARDAR CAMBIOS.
writer.save()
