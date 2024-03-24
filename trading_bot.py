# Import packages.
from tradingview_ta import TA_Handler, Interval, Exchange
import time

# Store the last order.
last_order = "sell"

# Instantiate TA_Handler.
handler = TA_Handler(
    symbol="TSLA",
    exchange="NASDAQ",
    screener="america",
    interval=Interval.INTERVAL_1_MINUTE
)

# Repeat forever.
count = 0
while True:
    # Retrieve recommendation.
    rec = handler.get_analysis().summary["RECOMMENDATION"]

    # Create a buy order if the recommendation is "BUY" or "STRONG_BUY" and the last order is "sell".
    # Create a sell order if the recommendation is "SELL" or "STRONG_SELL" and the last order is "buy".
    if "BUY" in rec and last_order == "sell":
        # REPLACE COMMENT: Create a buy order using your exchange's API.
        print("TIME TO BUY")

        last_order = "buy"
    elif "SELL" in rec and last_order == "buy":
        # REPLACE COMMENT: Create a sell order using your exchange's API.
        print("TIME TO SELL")

        last_order = "sell"
    else:
        print(rec)
        print("NO NEWS")
    count += 1
    if count == 4:
        break

    # Wait for x seconds before retrieving new analysis.
    # The time should be the same as the interval.
    time.sleep(60)
