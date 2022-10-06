# Weather App 
# Get Your Free API : http://openweathermap.org/appid
# pip install requests
import requests as req
from bs4 import BeautifulSoup as bs

def get_weather(loc):
    # Set API
    key = "Api key"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?"
    params = f"q={loc}&appid={key}"
    
    # Get the response from the API
    url = api_url + params
    response = req.get(url)
    weather = response.json()
    
# Fetch Weather
    print(f"Weather for {loc}:")
    temp = weather['main']['temp']
    print("Temperature:", temp - 273.15, "Celsius")
    humidity = weather['main']['humidity']
    print("Humidity:", humidity, "%")
    wind = weather['wind']['speed']
    print("Wind speed:", wind, "m/s")
    
    
# main
get_weather('London')
