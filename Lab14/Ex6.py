# Retrieve mortgage rate info from the Hawaii Board of Realtors and output the rates of each bank
# Name: Reesa Zhou
# Date: November 18, 2026

import pandas as pd
import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
print("Retrieving", url)

webpage = requests.get(url)
mortgageRate = pd.read_html(webpage)

print("Banks and Mortgage Rates:")
for index, row in mortgageRate.iterrows():
    print(f"{row['Lender']}: {row['Interest Rate']}%")
