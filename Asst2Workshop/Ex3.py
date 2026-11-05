# Load CSV file and ask how many rows to display
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

def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    salesData = loadCSV(csv_file)

    if salesData is None:
        return

    # describe the dataframe field data types
    print("\nData types of the dataframe fields:")
    print(salesData.dtypes)

    try:
        while True:
            displayInitialRows(salesData)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
