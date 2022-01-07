import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def get_rolling_mean(values, window):
    return pd.Series(pd.Series.rolling(values,window).mean())#,name='Rolling Mean')

def get_rolling_std(values,window):
    return pd.Series(pd.Series.rolling(values,window).std())#,name='Std Dev')

def get_bollinger_bands(rm,rstd):
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band

def test_run():
    spy = yf.Ticker("BTC-USD")
    df = spy.history(start='2021-01-01',end='2022-1-6')["Close"]

    rm_SPY = get_rolling_mean(df,window=20)
    rstd_SPY = get_rolling_std(df,window=20)

    upper_band, lower_band = get_bollinger_bands(rm_SPY,rstd_SPY)

    ax = df.plot()
    ax.set_ylabel("PRICE")
    rm_SPY.plot(label='Rolling mean',ax=ax).legend()
    upper_band.plot(label='Upper band',ax=ax).legend()
    lower_band.plot(label='Lower band',ax=ax).legend()
    plt.grid()

    plt.show()

test_run()
