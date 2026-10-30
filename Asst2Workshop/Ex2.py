# 
# Name: Reesa Zhou
# Date: October 30, 2026

import pandas as pd
import time

def loadCSV(filepath):
    print(F"Loading CSV file from: {filepath}")
    startTime = time.time()

    try:
        df = pd.read_csv(filepath, engine="pyarrow", on_bad_lines="skip")
        endTime = time.time()
        loadTime = endTime - startTime
        print(F"CSV file loaded successfully in {loadTime:.2f} seconds")
        print(F"Number of rows: {len(df)}")
    except:
        print("Error reading the CSV file:", 0)

    return df

csvFile = "sales_data.csv"
salesData = loadCSV(csvFile)

if salesData is not None:
    print(salesData.head(10))

