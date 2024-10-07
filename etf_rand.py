from yahooquery import Screener
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s  = Screeners()
'''screeners = s.available_screeners

for i in screeners:
    is 'us' in i:
        print(i)'''

data =s.get_screeners('top_etfs_us',count=250)
etf_data = data['top_etfs_us']['quotes']
ticker_list = [etf['symbol'] for etf in etf_data]

df = yf.download(ticker_list,start='2018-01-01',progress=False)['Close']

returns = df.pct_change()[1:]

corr = returns.corr(method='pearson')
