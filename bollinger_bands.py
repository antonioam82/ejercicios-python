import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def get_rolling_mean(values, window):
    return pd.Series(pd.Series.rolling(values,window).mean(),name='Rolling Mean')

def get_rolling_std(values,window):
    return pd.Series(pd.Series.rolling(values,window).std(),name='Std Dev')

def get_bollinger_bands(rm,rstd):
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band

def test_run():
    #dates = pd.date_range('2012-01-01','2012-12-31')
    #symbol = ['SPY']
    spy = yf.Ticker("SPY")
    df = spy.history(start='2012-01-01',end='2012-12-31')["Close"]

    rm_SPY = get_rolling_mean(df,window=20)
    rstd_SPY = get_rolling_std(df,window=20)

    upper_band, lower_band = get_bollinger_bands(rm_SPY,rstd_SPY)

    ax = df.plot(label='SPY')
    rm_SPY.plot(label='Rolling mean',ax=ax)
    upper_band.plot(label='upper band',ax=ax)
    lower_band.plot(label='lower band',ax=ax)
    plt.grid()

    plt.show()

test_run()
