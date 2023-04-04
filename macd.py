import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import numpy as np
from os import system
df = yf.download("AMZN", start = "2021-12-31")

#We work with the close data:
df["EMA12"] = df.Close.ewm(span=12).mean()
df["EMA26"] = df.Close.ewm(span=26).mean()
df["MACD"] = df.EMA12-df.EMA26
df["Senal"] = df.MACD.ewm(span = 9).mean()

print(df.MACD)

plt.subplot(2,1,2)
plt.plot(df.Senal, color="red")
plt.plot(df.MACD)
Buy, Sell = [], []
for i in range(2, len(df)):
    if df.MACD.iloc[i] > df.Senal.iloc[i] and df.MACD.iloc[i-1] < df.Senal.iloc[i-1]:
        Buy.append(i)
    elif df.MACD.iloc[i] < df.Senal.iloc[i] and df.MACD.iloc[i-1] > df.Senal.iloc[i-1]:
        Sell.append(i)

print("Dates sales:")
print(df.iloc[Sell].index, df.iloc[Sell].Close)
sellinfo = df.iloc[Sell].index, df.iloc[Sell].Close
print("Bullish dates:")
print(df.iloc[Buy].index, df.iloc[Buy].Close)
buyinfo = df.iloc[Buy].index, df.iloc[Buy].Close


#Get data from bullish
df1 = pd.DataFrame.from_records(buyinfo)
print(df1)
#Dataframe to dict:
diccionario = df1.to_dict()
#counting the data for get the last date for buy:
keys = list(diccionario.keys())
contarkeys = keys[-1]
print("count:",contarkeys)
print("Last info for buy:")
print(diccionario[contarkeys])
print("Last date for buy:")
date1 = diccionario[contarkeys][0]
dateforbuy = date1.strftime("%d/%m/%Y")
print(dateforbuy)
print("########")
print("Today date:")
now = datetime.now()
datetoday = now.strftime("%d/%m/%Y")
print(datetoday)
print("Yesterday date:")
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print(yesterday)

print("Final decision:")
if str(dateforbuy) == str(yesterday):
    print("MACD = BUY")
else:
    print("Not news")



#Show chart with data:
plt.subplot(2,1,1)
plt.scatter(df.iloc[Buy].index, df.iloc[Buy].Close, marker="o", color="green")
plt.scatter(df.iloc[Sell].index, df.iloc[Sell].Close, marker="o", color="red")
plt.plot(df.Close, color="black")

plt.show()
