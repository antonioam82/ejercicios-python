import ta
#import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

df = yf.Ticker("BTC-USD").history(period="max").reset_index()[["Date","Close"]]
print(df.head())

bol = ta.volatility.BollingerBands(df["Close"], window=20)#14

df['M-AVG'] = bol.bollinger_mavg()#banda media movil
df['Low Band'] = bol.bollinger_lband()#banda inferior
#df['hband'] = bol.bollinger_hband()#banda superior
df['High Band'] = bol.bollinger_hband()#banda superior

plt.grid()
plt.title("BTC-USD")
plt.plot(df["Date"],df["Close"])
plt.plot(df["Date"],df["M-AVG"], color="red")
plt.plot(df["Date"],df["Low Band"], color="orange")
plt.plot(df["Date"],df["High Band"], color="orange")
plt.fill_between(df["Date"],df["Low Band"],df["High Band"], alpha=0.2, color="orange")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(loc="best")

plt.show()
