import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
 
companies = ['AAPL', 'MSFT', 'GE']
shares_multiple_df = pdr.DataReader(companies, 'yahoo', start='2021-01-01', end='2021-12-31')
print(shares_multiple_df)
 
def plot_timeseries_df(df, attrib, ticker_loc=1, title='Timeseries', legend=''):
    "General routine for plotting time series data"
    fig = plt.figure(figsize=(15,7))
    plt.plot(df[attrib], 'o-')
    _ = plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(ticker_loc))
    plt.title(title)
    plt.gca().legend(legend)
    plt.show()
 
plot_timeseries_df(shares_multiple_df.loc["2021-04-01":"2021-06-30"], "Close",
                   ticker_loc=3, title="Close price", legend=companies)
