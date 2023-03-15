import pandas_datareader.data as web
import yfinance as yfin
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

start = dt.datetime(2022, 1, 1)
end = dt.datetime.today()

yfin.pdr_override()

ticker = 'AAPL'

df = web.DataReader(ticker, start, end)

#df.tail()
# Define the time period for calculating the ROC
n = 10

# Calculate the ROC indicator
df['ROC'] = df['Adj Close'].pct_change(periods=n)

# Generate buy signals when the ROC becomes above its signal line (0)
df['Buy'] = (df['ROC'] > 0) & (df['ROC'].shift(1) < 0)

# Generate sell signals when the ROC becomes below its signal line (0)
df['Sell'] = (df['ROC'] < 0) & (df['ROC'].shift(1) > 0)

# Buy securities when a buy signal is generated and sell them when a sell signal is generated
# 1 for Buy, -1 for Sell, 0 for Hold
df['Signal'] = np.where(df['Buy']==True, 1, np.where(df['Sell']==True,-1,0))

#print(df.tail(20))

# Calculate the daily returns of the strategy
df['Returns'] = df['Signal'].shift(1) * df['Adj Close'].pct_change()
df['Returns+1'] = 1 + df['Returns']

# Calculate the cumulative returns of the strategy
df['Cumulative_Returns'] = (1+df['Returns']).cumprod()

# Print the final cumulative return
print('Final Cumulative Return Over The Whole Period: ', df['Cumulative_Returns'][-1]-1)

df[['Returns+1','Cumulative_Returns']].plot(figsize=(8,4))
plt.title("Price Rate of Change (ROC)")
plt.show()

df[['Signal']].plot(figsize=(8,4))
plt.show()
