# Get public license data from City of Chicago data portal
# Name: Reesa Zhou
# Date: November 18, 2026

import pandas as pd
import urllib.request
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

jsonFile = "rr23-ymwb"

results = client.get(jsonFile, limit=500)

resultsDF = pd.DataFrame.from_records(results)
resultsDF.head()

vehicles = resultsDF[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public vehicles and fuel sources:")

vehicles.info()
vehiclesByFuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehiclesByFuel)
