# Create a dashboard with options to display a PivotTable in different configurations
# Name: Reesa Zhou
# Date: November 9, 2026

# import pandas and numpy to create pivot tables

import pandas as pd
import numpy as np
import time
import sys

# round all decimals in data to 2 points

pd.set_option("display.float_format", "{:.2f}".format)

# reads csv file and turns it into a dataframe, prints load time, and makes dates into consistent format

def loadFile(file):
    print(F"Loading file from {file}")
    startTime = time.time()

    try:
        df = pd.read_csv(csvFileChoice, engine="pyarrow", on_bad_lines="skip")
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        endTime = time.time()
        loadTime = round(endTime - startTime, 2)
        print(F"\nLoaded the file successfully! Load time: {loadTime}")
        return df
    except:
        print("Unable to load the file.")
        return None

# filters data to a range of years from 2019 through 2021, generated with the AI agent

def filterByYearRange(data):
    while True:
        try:
            startYear = int(input("\nEnter the first year to include (2019-2021): "))
            endYear = int(input("Enter the last year to include (2019-2021): "))
        except ValueError:
            print("Please enter valid whole-number years.")
            continue

        if not (2019 <= startYear <= 2021 and 2019 <= endYear <= 2021):
            print("Both years must be between 2019 and 2021.")
            continue

        if startYear > endYear:
            print("The first year must not be later than the last year.")
            continue

        filteredData = data.loc[
            data["order_date"].dt.year.between(startYear, endYear)
        ].copy()
        print(
            F"\nIncluding {startYear}-{endYear}: "
            F"{len(filteredData)} of {len(data)} rows match."
        )
        return filteredData

# Option 1, displays user-specified number of rows

def showRows(data):
    while True:
        userInput = input(F"\nHow many rows out of {len(data)} would you like to display? ")

        try:
            numRows = int(userInput)
        except:
            print("\nPlease enter a valid number.")
            continue

        if numRows < 1:
                    print("Please enter a greater number than 0.")
                    continue
        
        if numRows > len(data):
                    print(F"Only {len(data)} rows available. Please try again.")
                    continue
        
        print(F"\n{data.head(numRows)}")
        return F"\n{numRows} rows have been displayed."

# Option 2, displays total sales in each region

def totalSalesByRegion(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index="sales_region", columns="order_type", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            displayDashboard(data)

# Option 3, displays average sales of each region

def averageSales(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index="sales_region", columns=["order_type", "customer_state"], aggfunc="mean", margins = True, margins_name="Average_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# Option 4, displays sales by customer type

def salesByCustomerType(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index=["order_type", "customer_type"], columns="customer_state", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# Option 5, displays total sales in each region

def totalSalesQByRegion(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="sales_region", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# Option 6, displays totals sales by type of customer

def totalSalesQByCustomer(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="customer_type", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# Option 7, displays min and max of sales by product category

def maxMinSalesByCategory(data):
    while True:
        try:
            data["sales"] = data["quantity"] * data["unit_price"]
            pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="product_category", aggfunc=["min", "max"], margins = True, margins_name="MinMax_Sales")
            print(F"\n{pivotTable}")
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# Option 8, displays number of employees in each region

def employeesByRegion(data):
    while True:
        try:
            numEmployees = data.groupby("sales_region")["employee_id"].nunique()
            print("\nNumber of employees by region:")
            print(numEmployees.to_string())
            break
        except:
            print("\nAn error has occurred. Try again.")
            break

# available fields and functions for option 9, custom pivot table

rowsPT = ["employee_name", "sales_region", "product_category"]
columnsPT = ["order_type", "customer_type"]
valuesPT = ["quantity", "unit_price"]
aggregationPT = ["sum", "mean", "count"]

# Option 9, allows user to create custom pivot table (rows, columns, values, aggregation formula)

def createPT(data):
    print("\nAvailable fields to group in rows: ")

# prompts user to select row field

    while True:
        try:
            for label, option in enumerate(rowsPT, start=1):
                print(F"{label}. {option}")
            userRows = int(input("\nSelect field for row: "))
            rows = rowsPT[userRows-1]
            break
        except:
            print("\nInvalid choice. Please try again.")
            continue

# prompts user to select column field

    while True:
        try:
            for label, option in enumerate(columnsPT, start=1):
                print(F"{label}. {option}")
            userColumns = int(input("\nSelect field for column: "))
            columns = columnsPT[userColumns-1]
            break
        except:
            print("\nInvalid choice. Please try again.")
            continue

# prompts user to select values

    while True:
        try:
            for label, option in enumerate(valuesPT, start=1):
                print(F"{label}. {option}")
            userValues = int(input("\nSelect value: "))
            values = valuesPT[userValues-1]
            break
        except:
            print("\nInvalid choice. Please try again.")
            continue

# prompts user to select aggregation function

    while True:
        try:
            for label, option in enumerate(aggregationPT, start=1):
                print(F"{label}. {option}")
            userAggregate = int(input("\nSelect aggregation function: "))
            aggregation = aggregationPT[userAggregate-1]
            break
        except:
            print("\nInvalid choice. Please try again.")
            continue

# displays different margins name according to user-selected aggregation function

    if userAggregate == 1:
        pivotTable = pd.pivot_table(data, values=values, index=rows, columns=columns, aggfunc=aggregation, margins = True, margins_name="Sum")
    elif userAggregate == 2:
        pivotTable = pd.pivot_table(data, values=values, index=rows, columns=columns, aggfunc=aggregation, margins = True, margins_name="Mean")
    else:
        pivotTable = pd.pivot_table(data, values=values, index=rows, columns=columns, aggfunc=aggregation, margins = True, margins_name="Count")

    print(pivotTable)

# Option 10, exits program

def exit():
    print("\nExiting the program...Goodbye!")

# prepares two csv files and loads data for analysis, lets user choose which one to analyze
# names and products are the same, but quantity, unit price, state, and region are all slightly different

csvFile1 = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
csvFile2 = "sales_data_other.csv"

while True:
    try:
        csvFileChoice = int(input("Choose which CSV file to analyze (1 - 2): "))

        if csvFileChoice > 2:
            print("Select a valid file choice. Try again.")
            continue

        if csvFileChoice == 1:
            csvFileChoice = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download"
            data = loadFile(csvFile1)
            data = filterByYearRange(data)

        if csvFileChoice == 2:
            csvFileChoice = "sales_data_other.csv"
            data = loadFile(csvFile2)
            data = filterByYearRange(data)

        break
    except:
        print("Invalid choice. Try again.")
        continue

# dashboard display options that correspond to different pivot table configurations

dashboard = {
    "Show the first n rows of sales data":showRows,
    "Total sales by region and order type":totalSalesByRegion,
    "Average sales by region with average sales by state and sale type":averageSales,
    "Sales by customer type and order type by state":salesByCustomerType,
    "Total sales quantity and price by region and product":totalSalesQByRegion,
    "Total sales quantity and price customer type":totalSalesQByCustomer,
    "Max and min sales price of sales by category":maxMinSalesByCategory,
    "Number of unique employees by region":employeesByRegion,
    "Create a custom pivot table":createPT,
    "Exit":exit
}

# numbers dashboard options and selects option based on user-inputted number (uses index number)

def displayDashboard(data):
    while True:
        print("\nDashboard:\n")
        for label, (option) in enumerate(dashboard, start=1):
            print(F"{label}. {option}")
        try:
            choice = int(input("\nPlease choose an action (1 - 10): "))
            output = list(dashboard.keys())[choice-1]
            if choice == 10:
                dashboard[output]()
                return
            else:
                dashboard[output](data)
        except:
            print("\nThis does not work. Try again.")
            continue

# program creates pivot table, then displays dashboard again (except when choosing to exit)
# will have to scroll up to view pivot table

displayDashboard(data)
