# Import homes data and create a dataframe
# Name: Reesa Zhou
# Date: October 28, 2026

import pandas as pd

homes_df = pd.read_csv("homes_data.csv")
print(homes_df.head(10))

shape = homes_df.shape
print("The dimensions of the dataframe are:", shape)

dfBig = homes_df[homes_df["units"] >= 500]
dfBig = dfBig.drop(columns=["easement"])
print(dfBig.head(10))

print(dfBig.info())

dfBig["land_sqft"] = pd.to_numeric(dfBig["land_sqft"], errors="coerce")
dfBig["gross_sqft"] = pd.to_numeric(dfBig["gross_sqft"], errors="coerce")
dfBig["sale_price"] = pd.to_numeric(dfBig["sale_price"], errors="coerce")

print("After cleaning...")
print(dfBig.info())
print(dfBig.head(10))

dfBig = dfBig.dropna()

dfBig = dfBig.drop_duplicates()
print("After removing duplicates...")
print(dfBig.info())
print(dfBig.head(10))

dfBig = dfBig[dfBig["sale_price"] > 0]
print("After filtering out 0 sales...")
print(dfBig.info())
print(dfBig.head(10))
