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

def showEmployeesByRegion(data):
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())

def getUserSelection(options, prompt, required=False, single=False):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(F"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice, separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(",")]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(F"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))

        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected

def generate_custom_pivot_table(data):
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)


def show_average_sales_by_region(data):
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", displayInitialRows),
    ("Show the number of employees by region", showEmployeesByRegion),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Average sales by region, by state and sale type", show_average_sales_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")

def main():
    csvFile = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    salesData = loadCSV(csvFile)

    if salesData is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(salesData)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
