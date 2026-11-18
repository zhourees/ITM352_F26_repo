# Grab one month interest rate from the US Treasury website
# Name: Reesa Zhou
# Date: November 18, 2026

import ssl, lxml
import pandas as pd
import urllib.request

ssl.create_default_https_context = ssl._create_unverified_context

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"
print("Retrieving", url)

webpage = urllib.request.urlopen(url, context=ssl.create_default_https_context)
df = pd.read_html(webpage)

print("Columns", df[0].columns)

intRateTable = df[0]

print("1 Month Interest Rates:")

for index, row in intRateTable.iterrows():
    print(F"Date: {row["Date"]}, 1 Month Rate: {row["1 Mo"]}")

