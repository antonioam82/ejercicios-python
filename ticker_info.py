import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector
from rpy2.robjects import pandas2ri
import argparse
import colorama
import pandas as pd

pandas2ri.activate()

'''# Importar las bibliotecas necesarias de R
alphavantager = importr('alphavantager')
quantmod = importr('quantmod')
ggplot2 = importr('ggplot2')

# Definir la clave de la API
api_key = 'tu_clave_api_aqui'
ro.r(f'av_api_key("{api_key}")')

# Definir el símbolo de la acción
ticker = 'hvhvhvhv'

try:
    # Obtener datos financieros clave utilizando la función `av_get`
    financial_data = ro.r(f'av_get(symbol = "{ticker}", datatype = "json", av_fun = "OVERVIEW")')

    # Mostrar todas las columnas disponibles en financial_data
    print(financial_data)
except Exception as e:
    print(str(e))'''

def get_info(args):
    try:
        alphavantager = importr('alphavantager')
        quantmod = importr('quantmod')
        #ggplot2 = importr('ggplot2')

        # Definir la clave de la API
        api_key = 'tu_clave_api_aqui'
        ro.r(f'av_api_key("{api_key}")')

        # Definir el símbolo de la acción
        ticker = args.ticker


        # Obtener datos financieros clave utilizando la función `av_get`
        financial_data = ro.r(f'av_get(symbol = "{ticker}", datatype = "json", av_fun = "OVERVIEW")')

        # Mostrar todas las columnas disponibles en financial_data
        #print(financial_data[1][0])
        #if args.information == "All":
        df = pandas2ri.rpy2py(ro.r('as.data.frame')(financial_data))
        print(df)
        #else:
            #print("ok")
            
    except Exception as e:
        print(str(e))
    

info_choices = ['Symbol','AssetType','Name','Description','CIK','Exchange','Currency',
                'Country','Sector','Industry','All']

def main():
    parser = argparse.ArgumentParser(prog="SYMBOL_INFO",conflict_handler='resolve',
                                     description="Get symbol info with R")
    parser.add_argument('-tick','--ticker',required=True,type=str,help="Ticker symbol")
    parser.add_argument('-info','--information',required=True,type=str,choices=info_choices,help="Ticker symbol")
    args = parser.parse_args()

    get_info(args)

    

if __name__=='__main__':
    main()
