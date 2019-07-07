import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

googl = pdr.get_data_yahoo('GOOGL',start=datetime.datetime(2009,10,1))

column = googl['Close'][-10:]

print(column)

#VER GRAFICA.
column.plot(grid=True)
plt.show()
