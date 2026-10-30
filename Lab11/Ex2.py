# Create a dataframe from a CSV file, create a pivot table that aggregates sales by order type/sales region
# Name: Reesa Zhou
# Date: October 30, 2026

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

try:
    df = pd.read_csv("sales_data.csv", engine="pyarrow", on_bad_lines="skip")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # print(df.head())

    df["sales"] = df["quantity"] * df["unit_price"]

    pivotTable = pd.pivot_table(df, values="sales", index="sales_region", columns="order_type", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
    print(pivotTable)
except Exception as e:
    print(F"Error occurred while reading the CSV file: {e}")

