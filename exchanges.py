import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse
from pprint import pprint

def get_exchange_list_xrates(currency, amount=1):
    #ACCEDER AL CONTENIDO DE LA PÁGINA.
    content = requests.get(f"https://www.x-rates.com/table/?from={currency}&amount={amount}").content
    #INICIAR 'BeautifulSoup'.
    soup = bs(content, "html.parser")
    #OBTENER PRECIOS ACTUALIZADOS.
    price_datetime = parse(soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text)
    #OBTENER TABLA DE CAMBIOS.
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate        
    return price_datetime, exchange_rates

#LLAMADA A FUNCIÓN.
if __name__ == "__main__":
    import sys
    source_currency = 'EUR'
    amount = 1
    price_datetime, exchange_rates = get_exchange_list_xrates(source_currency, amount)
    print("Last updated:", price_datetime)
    pprint(exchange_rates)
