import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data as wb

# Define los símbolos de las acciones de las compañías
symbol1 = 'NVDA'  # NVDA.

# Define el rango de fechas para los datos históricos
start_date = '2020-01-01'
end_date = datetime.today().strftime('%Y-%m-%d') # Fecha actual

# Descarga los datos históricos de las acciones usando yfinance
data1 = yf.download(symbol1, start=start_date, end=end_date)

# Calculo retornos
returns = data1['Adj Close'].pct_change()

print(returns.tail())

# Graficar la evolución del precio de las acciones
plt.figure(figsize=(14, 7))
plt.plot(data1.index, returns, label=symbol1, linewidth=1.0)

# Añadir títulos y etiquetas
plt.title(f'Evolución de los retornos de {symbol1} ({start_date} - {end_date})')
plt.grid()
plt.xlabel('Fecha')
plt.ylabel('Retornos')
plt.legend()

# Mostrar la gráfica
plt.show()
