# Create a dashboard with options to display a PivotTable in different configurations
# Name: Reesa Zhou
# Date: November 5, 2026

import pandas as pd
import numpy as np
import time

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:.2f}".format)

def loadFile(file):
    print(F"Loading file from {file}")
    startTime = time.time()

    try:
        df = pd.read_csv("sales_data.csv", engine="pyarrow", on_bad_lines="skip")
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        endTime = time.time()
        loadTime = round(endTime - startTime, 2)
        print(F"\nLoaded the file successfully! Load time: {loadTime}")
        return df
    except:
        print("Unable to load the file.", 0)
        return None

# Option 1

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

# Option 2

def totalSalesByRegion(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index="sales_region", columns="order_type", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 3

def averageSales(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index="sales_region", columns=["order_type", "customer_state"], aggfunc="mean", margins = True, margins_name="Average_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 4

def salesByCustomerType(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index=["order_type", "customer_type"], columns="customer_state", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 5

def totalSalesQByRegion(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="sales_region", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 6

def totalSalesQByCustomer(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="customer_type", aggfunc=np.sum, margins = True, margins_name="Total_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 7

def maxMinSalesByCategory(data):
    try:
        data["sales"] = data["quantity"] * data["unit_price"]
        pivotTable = pd.pivot_table(data, values="sales", index="order_type", columns="product_category", aggfunc=["min", "max"], margins = True, margins_name="MinMax_Sales")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 8 (FIX)

def employeesByRegion(data):
    try:
        data["numEmployees"] = data("sales_region")["employee_id"].nunique()
        pivotTable = pd.pivot_table(data, values="numEmployees", index="sales_region", aggfunc=np.sum, margins = True, margins_name="Employee")
        print(F"\n{pivotTable}")
    except:
         print("\nAn error has occurred.")

# Option 9 (DO)

# def createPT(data):


# Option 10 (FIX)

def exit():
    print("Exiting the program...Goodbye!")
    raise SystemExit(0)


csvFile = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
data = loadFile(csvFile)

dashboard = {
    "Show the first n rows of sales data":showRows,
    "Total sales by region and order type":totalSalesByRegion,
    "Average sales by region with average sales by state and sale type":averageSales,
    "Sales by customer type and order type by state":salesByCustomerType,
    "Total sales quantity and price by region and product":totalSalesQByRegion,
    "Total sales quantity and price customer type":totalSalesQByCustomer,
    "Max and min sales price of sales by category":maxMinSalesByCategory,
    "Number of unique employees by region":employeesByRegion,
    "Create a custom pivot table":"createPT",
    "Exit":"Would you like to display the dashboard again? "
}

def displayDashboard(data):
    while True:
        print("\nDashboard:\n")
        for label, (option) in enumerate(dashboard, start=1):
            print(F"{label}. {option}")
        choice = int(input("\nPlease choose an action: "))
        try:
            output = list(dashboard.keys())[choice-1]
            return dashboard[output](data)
        except:
            print("\nThis does not work. Try again.")
            continue

displayDashboard(data)

