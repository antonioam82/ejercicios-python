import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import itertools
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Configure Yahoo Finance data source
yf.pdr_override()

# Download historical stock data
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2021-01-01"
stock_data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)

# Select the closing prices
closing_prices = stock_data["Close"]

# Split the data into training and testing sets
train_data = closing_prices[:int(len(closing_prices) * 0.8)]
test_data = closing_prices[int(len(closing_prices) * 0.8):]

# Grid search to find the optimal ARIMA parameters
p_values = range(0, 5)
d_values = range(0, 5)
q_values = range(0, 5)
pdq_combinations = list(itertools.product(p_values, d_values, q_values))

best_aic = float("inf")
best_order = None
best_model = None
n = 1
for order in pdq_combinations:
    try:
        print("COMBINATION ",n)
        model = ARIMA(train_data, order=order)
        model_fit = model.fit()
        if model_fit.aic < best_aic:
            best_aic = model_fit.aic
            best_order = order
            best_model = model_fit
        n+=1
    except Exception as e:
        print(f"Error fitting ARIMA model with order {order}")

print(f"Best ARIMA order: {best_order}")
print("AIC: ", best_aic)
print("BIC: ", best_model.bic)

# Forecast the stock prices using the best ARIMA model
forecast = best_model.forecast(steps=len(test_data))

# Calculate the root mean squared error (RMSE)
rmse = sqrt(mean_squared_error(test_data, forecast))
print("RMSE: ", rmse)

# Plot the actual vs. predicted closing prices
plt.figure(figsize=(12, 6))
plt.plot(train_data, label="Training data")
plt.plot(test_data, label="Actual closing prices")
plt.plot(test_data.index, forecast, label="Predicted closing prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title(f"{ticker} Stock Closing Price Prediction using ARIMA")
plt.legend()
plt.show()
