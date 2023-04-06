import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import re
#Librería más importante:
import yfinance as yahoo_finance
###########################
pd.core.common.is_list_like = pd.api.types.is_list_like
pd.set_option('expand_frame_repr', False)  


#TICKER DE LA EMPRESA QUE QUEREMOS ANALIZAR
#ticker = 'GOOG'
ticker = 'NFLX'
#Fecha con la que empezamos a recolectar datos:
start_time = datetime.datetime(2021, 1, 1)
#Si quisieramos especificiar fecha final:
#end_time = datetime.datetime(2019, 1, 20)
end_time = datetime.datetime.now().date().isoformat()         # today
# yahoo comineza a descargar datos:
connected = False
while not connected:
    try:
        df = web.get_data_yahoo(ticker, start=start_time, end=end_time)
        connected = True
        print('connected to yahoo')
    except Exception as e:
        print("type error: " + str(e))
        time.sleep( 5 )
        pass   

# emplea integer
df = df.reset_index()
print(df.head(5))

def bollinger_bands(df, n, m):
    # n = longitud de alisado
    # m = num de desviaciones estandar lejos de MA
    
    #typical price
    TP = (df['High'] + df['Low'] + df['Close']) / 3
    data = TP
    #data = df['Adj Close']
    
    # toma una columna del marco de datos
    B_MA = pd.Series((data.rolling(n, min_periods=n).mean()), name='B_MA')
    sigma = data.rolling(n, min_periods=n).std() 
    
    BU = pd.Series((B_MA + m * sigma), name='BU')
    BL = pd.Series((B_MA - m * sigma), name='BL')
    
    df = df.join(B_MA)
    df = df.join(BU)
    df = df.join(BL)
    
    return df
#PARAMETROS PARA BOLLINGER BANDS
n = 20   # Parametro para linea central
m = 2    # Desviaciones
df = bollinger_bands(df, 20, 2)
print(df.head())
print(df.tail())



#### REMUESTREO SEMANAL PARA LIMPIAR DATOS

agg_dict = {'Open': 'first',
          'High': 'max',
          'Low': 'min',
          'Close': 'last',
          'Adj Close': 'last',
          'Volume': 'mean'}


# 'W' significa agregación semanal
df.set_index('Date', inplace=True)
df_agg = df.resample('W').agg(agg_dict)
df_agg = df_agg.reset_index()


n = 20   # datapoint movil de puntos de datos
m = 2    # sigma width
df_agg = bollinger_bands(df_agg, 20, 2)

def add_signal(df):
    # IMPORTANTE
    # Crea dos columnas para puntos de compra y venta.
    buy_list = []
    sell_list = []
    
    for i in range(len(df['Close'])):
        #if df['Close'][i] > df['BU'][i]:           # sell signal     daily
        if df['High'][i] > df['BU'][i]:             # sell signal     weekly
            buy_list.append(np.nan)
            sell_list.append(df['Close'][i])
        #elif df['Close'][i] < df['BL'][i]:         # buy signal      daily
        elif df['Low'][i] < df['BL'][i]:            # buy signal      weekly
            buy_list.append(df['Close'][i])
            sell_list.append(np.nan)  
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)
         
    buy_list = pd.Series(buy_list, name='Buy')
    sell_list = pd.Series(sell_list, name='Sell')
        
    df = df.join(buy_list)
    df = df.join(sell_list)
    #SACAMOS LOS PUNTOS DE VENTA:        
    new_df = df[['Date','Sell']].copy()
    #ELIMINAMOS FILAS VACIAS:
    new_df = new_df[new_df['Sell'].notna()]
    print(new_df)
    #Lo guardamos en csv:
    new_df.to_csv (r'databollingerventas.csv', index = None, header=True) 
    #Mostramos la ultima fila:
    print(new_df.tail(1))
    #Mostramos la ultima fecha:
    print("Ultima fecha de venta:")
    print(new_df['Date'].tail(1))
    fechafinal = new_df['Date'].tail(1).astype(str)
    #Lo pasamos a string:
        #Primero guardamos fecha en txt como objeto
    archi1=open("datos.txt","w") 
    archi1.write(str(fechafinal))  
    archi1.close() 
        #Ahora leemos el txt y pasamos a str
    with open('datos.txt') as f:
        first_line = f.readline()
        first_line = str(first_line)
    print(first_line)
        #Ahora lo limpiamos para sacar solo la fecha con regex
    from datetime import date
    from datetime import datetime
    from datetime import timedelta
    match = re.search(r'\d{4}-\d{2}-\d{2}', first_line)
    date = datetime.strptime(match.group(), '%Y-%m-%d').date()
    print("La ultima fecha de venta limpia:")
    fechalimpiada = str(date)
    print(date)
    print("Fecha de ayer:")
    today = date.today()
    yesterday = today - timedelta(days = 1)
    ayer = str(yesterday)
    print(ayer)
    #cambiar para test:
    #fechalimpiada = "2022-10-27"
    print(fechalimpiada)
    if str(fechalimpiada) == str(yesterday):
        print("Abrir orden de venta.")
    else:
        print("No hay novedades.")
    
    return df

def plot_signals(df, ticker):

    # creacion del grafico
    plt.figure(figsize=(15,5))
    plt.title('Bollinger Bands chart ' + str(ticker))
    plt.plot(df['Date'], df['Adj Close'], label='Adj Close')

    plt.plot(df['Date'], df['High'], label='High', alpha=0.3)
    plt.plot(df['Date'], df['Low'], label='Low', alpha=0.3)

    plt.plot(df['Date'], df['BU'], label='B_Upper', alpha=0.3)
    plt.plot(df['Date'], df['BL'], label='B_Lower', alpha=0.3)
    plt.plot(df['Date'], df['B_MA'], label='B_SMA', alpha=0.3)
    plt.fill_between(df['Date'], df['BU'], df['BL'], color='grey', alpha=0.1)

    plt.scatter(df['Date'], df['Buy'], label='Buy', marker='^')
    plt.scatter(df['Date'], df['Sell'], label='Sell', marker='v')

    plt.legend()

    plt.show()
    

df_agg = add_signal(df_agg)
plot_signals(df_agg, ticker)
