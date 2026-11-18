# Get a JSON file from City of Chicago data portal and analyze driver types
# Name: Reesa Zhou
# Date: November 18, 2026

import pandas as pd
import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

responseJSON = response.json()

print("Driver types and counts:")

responseDF = pd.DataFrame.from_records(responseJSON)
responseDF.columns = ["driver_type", "count"]
responseDF = responseDF.set_index("driver_type")

print(responseDF)
