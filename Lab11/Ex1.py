# Read a csv file, skip bad lines, and convert order_date column to standard date representation
# Name: Reesa Zhou
# Date: October 28, 2026

import pandas as pd

try:
    df = pd.read_csv("sales_data.csv", engine="pyarrow", on_bad_lines="skip")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    print(df.head())
except:
    print("Error reading the CSV file:", 0)
