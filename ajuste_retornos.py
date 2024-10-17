import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker = ['AAPL']
returns = yf.download(ticker, '2015-01-01', progress=False)['Close'].pct_change()[1:].rename(ticker[0])
print(returns)

returns.plot(kind="hist",bins=150,title=f"Variación de los retornos de {str(ticker[0])}",
             xlabel="Retornos",ylabel="Frecuancia")
plt.axvline(returns.mean(),linestyle="--",linewidth=2,color="y")
plt.axvline(returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(-1*returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(-2*returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(2*returns.std(),linestyle="--",linewidth=2,color="r")
plt.show()
