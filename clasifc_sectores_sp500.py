import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
#import pandas_ta as ta

# Ignorar todos los warnings
warnings.filterwarnings("ignore")

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0][['Symbol','GICS Sector',
                   'GICS Sub-Industry']].set_index(['Symbol'])

sectores = list(set(data['GICS Sector']))
#print(sectores)
sub_sectores = list(set(data['GICS Sub-Industry']))
#print(sub_sectores)

df = yf.download(list(data.index),start='2023-01-01',progress=False)['Close']
#print(df)

df = df.reindex(columns=data.index)
mean = df.rolling(150).mean()

df1 = pd.DataFrame(np.where(df.iloc[-1]>mean.iloc[-1],1,0), index=df.columns)
data['>mean(150)'] = df1[0]
print(data)

#clasificar
suma = pd.DataFrame()
for i in range(len(sectores)):
    x = pd.DataFrame(data['>mean(150)'][data['GICS Sector'] == str(sectores[i])]).sum()
    suma = pd.concat([suma,x],axis=1)

suma.columns = sectores
suma = suma.T
print(suma)

suma.plot(kind='bar',figsize=(15,10),title="Empresas del SP500 por encima de la media de los 150p",
          ylim=(0,len(data.index)), ylabel="Nª de empresas",
          xlabel="Sectores",legend=False,rot=30)

plt.show()
