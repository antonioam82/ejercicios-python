import pandas_datareader.wb as wb
import pandas as pd
import matplotlib.pyplot as plt
 
# Get a list of 2-letter country code excluding aggregates
countries = wb.get_countries()
countries = list(countries[countries.region != "Aggregates"]["iso2c"])
 
# Read countries' total population data (SP.POP.TOTL) in year 2020
population_df = wb.download(indicator="SP.POP.TOTL", country=countries, start=2020, end=2020)
 
# Sort by population, then take top 25 countries, and make the index (i.e., countries) as a column
population_df = (population_df.dropna()
                              .sort_values("SP.POP.TOTL")
                              .iloc[-25:]
                              .reset_index())
 
# Plot the population, in millions
fig = plt.figure(figsize=(15,7))
plt.bar(population_df["country"], population_df["SP.POP.TOTL"]/1e6)
plt.xticks(rotation=90)
plt.ylabel("Million Population")
plt.title("Population")
plt.show()
