import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

ticker = "AAPL"

# Descarga de datos
data = yf.download(ticker, start="2024-01-01",
                   end="2024-12-31", auto_adjust=False)

#print(data) # muestra datos

# Calcular retornos logarítmicos
data['Retorno_Log'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
print(data['Retorno_Log'])

# Graficar
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Retorno_Log'], label=f"Retornos logarítmicos de {ticker}")
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.grid()
plt.title(f"Retornos logarítmicos de {ticker}")
plt.xlabel("Fecha")
plt.ylabel("Retorno logarítmico")
plt.legend()
plt.show()
