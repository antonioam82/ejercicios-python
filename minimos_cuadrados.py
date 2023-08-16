import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

tickers = ['PCEC', 'GDP']
data = wb.DataReader(tickers, 'fred', '2010-1-1')

plt.plot(data.index,data,lw=1.5)
plt.legend(data.columns)
plt.show()


plt.scatter(data['PCEC'],data['GDP'])
plt.show()

mod = smf.ols('PCEC ~ GDP', np.log(data)).fit()
print(mod.summary(), mod.params)

plt.plot(data.index, data.diff(), lw=1.5)
plt.legend(data.columns)
plt.show()
