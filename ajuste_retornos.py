import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from fitter import Fitter, get_common_distributions, get_distributions

ticker = ['^IBEX']
returns = yf.download(ticker, '2015-01-01', progress=False)['Close'].pct_change()[1:].rename(ticker[0])
print(returns)

returns.plot(kind="hist",bins=150,title=f"Variación de los retornos de {str(ticker[0])}",
             xlabel="Retornos",ylabel="Frecuencia")
plt.axvline(returns.mean(),linestyle="--",linewidth=2,color="y")
plt.axvline(returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(-1*returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(-2*returns.std(),linestyle="--",linewidth=2,color="r")
plt.axvline(2*returns.std(),linestyle="--",linewidth=2,color="r")
plt.show()

# Distribucion normal
returns.plot(kind='hist',bins=200,density=True,alpha=0.6,color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, returns.mean(), returns.std())
plt.plot(x, p, linewidth=2, color='r', linestyle='--')
plt.show()

# Distribuciones posibles
print(get_common_distributions())
print(get_distributions())

f = Fitter(returns,distributions=['cauchy','norm','levy','laplace','johnsonsu',])
f.fit()
f.summary()
plt.show()
