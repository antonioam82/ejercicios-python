import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define los símbolos de las acciones de las compañías
symbol1 = 'NVDA'  # Apple Inc.
symbol2 = 'MSFT'  # Microsoft Corporation

# Define el rango de fechas para los datos históricos
start_date = '2022-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Descarga los datos históricos de las acciones usando yfinance
data1 = yf.download(symbol1, start=start_date, end=end_date)
data2 = yf.download(symbol2, start=start_date, end=end_date)

# Graficar la evolución del precio de las acciones
plt.figure(figsize=(14, 7))
plt.plot(data1.index, data1['Adj Close'], label=symbol1)
plt.plot(data2.index, data2['Adj Close'], label=symbol2)

# Añadir títulos y etiquetas
plt.title(f'Evolución del Precio de las Acciones de {symbol1} y {symbol2}')
plt.grid()
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre Ajustado')
plt.legend()

# Mostrar la gráfica
plt.show()
