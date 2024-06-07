import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector

# Importar las bibliotecas necesarias de R
alphavantager = importr('alphavantager')
quantmod = importr('quantmod')
ggplot2 = importr('ggplot2')

# Definir la clave de la API
api_key = 'tu_clave_api_aqui'
ro.r(f'av_api_key("{api_key}")')

# Definir el símbolo de la acción
ticker = 'META'

# Obtener datos financieros clave utilizando la función `av_get`
financial_data = ro.r(f'av_get(symbol = "{ticker}", datatype = "json", av_fun = "OVERVIEW")')

# Mostrar todas las columnas disponibles en financial_data
print(financial_data)
