# Import packages.
from tradingview_ta import TA_Handler, Interval, Exchange
import time

# Instantiate TA_Handler.
handler = TA_Handler(
    symbol="META",
    exchange="NASDAQ",
    screener="america",
    interval=Interval.INTERVAL_1_MINUTE
)

start = handler.get_analysis().summary["RECOMMENDATION"]
if "BUY" in start:
    last_order = "buy"
else:
    last_order = "sell"

print("INITIAL RECOMMENDATION: ",last_order.upper())
time.sleep(60)

# Repeat forever.
count = 0
while True:
    # Retrieve recommendation.
    rec = handler.get_analysis().summary["RECOMMENDATION"]

    # Create a buy order if the recommendation is "BUY" or "STRONG_BUY" and the last order is "sell".
    # Create a sell order if the recommendation is "SELL" or "STRONG_SELL" and the last order is "buy".
    if "BUY" in rec and last_order == "sell":
        # REPLACE COMMENT: Create a buy order using your exchange's API.
        print("RECOMMENDATION: ",rec)

        last_order = "buy"
    elif "SELL" in rec and last_order == "buy":
        # REPLACE COMMENT: Create a buy order using your exchange's API.
        print("RECOMMENDATION: ",rec)

        last_order = "sell"
    else:
        print("NO NEWS")
    count += 1
    if count == 4:
        break

    # Wait for x seconds before retrieving new analysis.
    # The time should be the same as the interval.
    time.sleep(60)

'''Interval.INTERVAL_1_MINUTE: Representa un intervalo de 1 minuto.
Interval.INTERVAL_5_MINUTES: Representa un intervalo de 5 minutos.
Interval.INTERVAL_15_MINUTES: Representa un intervalo de 15 minutos.
Interval.INTERVAL_1_HOUR: Representa un intervalo de 1 hora.
Interval.INTERVAL_4_HOURS: Representa un intervalo de 4 horas.
Interval.INTERVAL_1_DAY: Representa un intervalo de 1 día.'''
