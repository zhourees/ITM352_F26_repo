# 
# Name: Reesa Zhou
# Date: November 4, 2026

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
        return df
    except:
        print("Error reading the CSV file:", 0)
        return None

def displayInitialRows(data):
    while True:
        response = input(F"How many initial rows would you like to see? {len(data)}, or all? ").strip().lower()

        if response == "all":
            print(data)
            return "All rows have been displayed."

        try:
            numRows = int(response)
        except:
            print(F"Invalid input. Please enter a whole number or 'all'.")
            continue

        if numRows < 1:
            print("Please enter a greater number than 0.")
            continue

        if numRows > len(data):
            print(F"Only {len(data)} rows available, or all.")
            continue

        print(data.head(numRows))
        return "Rows have been displayed."

def showEmployeesByRegion(data):
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("Number of employees by region:")
    print(counts.to_string())

def exitProgram(data=None):
    print("Exiting the program. Goodbye.")
    raise SystemExit(0)

menuOptions = (("Show the first n rows of sales data", displayInitialRows), ())

def main():
    csvFile = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download"
    salesData = loadCSV(csvFile)

    if salesData is None:
        return

    print("\nData types of the dataframe fields: ")
    print(salesData.dtypes)

