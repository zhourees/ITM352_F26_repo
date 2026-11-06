# Create a dashboard with options to display a PivotTable in different configurations
# Name: Reesa Zhou
# Date: November 5, 2026

import pandas as pd
import time

def loadFile(file):
    print(F"Loading file from {file}")
    startTime = time.time()

    try:
        df = pd.read_csv(file)
        endTime = time.time()
        loadTime = endTime - startTime
        print(F"Loaded the file successfully! Load time: {loadTime}")
        return df
    except:
        print("Unable to load the file.", 0)
        return None

dashboard = {
    "Show the first n rows of sales data":showRows(),
    "Total sales by region and order type":totalSalesByRegionAndOrderType(),
    "Average sales by region with average sales by state and sale type":averageSales(),
    "Sales by customer type and order type by state":salesByCustomerType(),
    "Total sales quantity and price by region and product":totalSalesByRegion(),
    "Total sales quantity and price customer type":totalSalesByCustomer(),
    "Max and min sales price of sales by category":maxMinSalesByCategory(),
    "Number of unique employees by region":employeesByRegion(),
    "Create a custom pivot table":pivotTable(),
    "Exit":exit()
}

def displayDashboard():
    while True:
        print("\nSales Data Menu:")
