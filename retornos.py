import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"

# Descarga con rango específico
data = yf.download(ticker, start="2024-01-01", end="2024-08-01", auto_adjust=False)

# Calcular retornos diarios
data['Retorno'] = data['Adj Close'].pct_change()

# Graficar
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Retorno'], label=f"Retornos diarios de {ticker}")
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.title(f"Retornos diarios de {ticker}")
plt.xlabel("Fecha")
plt.ylabel("Retorno diario (%)")
plt.legend()
plt.show()
