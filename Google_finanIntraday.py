from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='YOUR_API_KEY')
data, meta_data = ts.get_intraday('GOOGL')

print(data)
print(meta_data)
