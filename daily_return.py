import ta
import matplotlib.pyplot as plt
import yfinance as yf
from ta.utils import dropna
import warnings
warnings.filterwarnings("ignore")

ticker = "GOGL"

df = yf.Ticker(ticker).history(period="max").reset_index()[["Date","Close"]]

df = dropna(df)
print(df.head())

#bol = ta.volatility.BollingerBands(df["Close"], window=20)#14

df['dlr'] = ta.others.DailyLogReturnIndicator(df["Close"]).daily_log_return()

print(df["dlr"].head())

plt.grid()
plt.title(ticker+ " DAILY RETURN" )
plt.plot(df["Date"],df["dlr"], color="green")

#plt.fill_between(df["Date"],df["Low Band"],df["High Band"], alpha=0.2, color="orange")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(loc="best")

plt.show()
