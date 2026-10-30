# 
# Name: Reesa Zhou
# Date: October 30, 2026

import pandas as pd

try:
    df = pd.read_csv("sales_data.csv", engine="pyarrow", on_bad_lines="skip")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    outFile = "sales_data_test.csv"
    df.head(10).to_csv(outFile, index=False)
    print(F"First 10 rows of sales_data.csv saved to {outFile}")
except:
    print("Error reading the CSV file:", 0)
