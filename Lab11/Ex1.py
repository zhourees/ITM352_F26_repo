# 
# Name: Reesa Zhou
# Date: October 28, 2026

import pandas as pd

try:
    df = pd.read_csv("sales_data.csv", engine="pyarrow", on_bad_lines="skip")
    print(df.head())
except:
    print("Error reading the CSV file:", 0)
