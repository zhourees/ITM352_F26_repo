# Read a json file of taxi trip data and create a dataframe and some simple statistics
# Name: Reesa Zhou
# Date: October 28, 2026

import pandas as pd

results_df = pd.read_json("Taxi_Trips.json")

print(results_df.head(6))
print(results_df.describe())

median = results_df["fare"].median()
print("The median fare valie is:", median)
