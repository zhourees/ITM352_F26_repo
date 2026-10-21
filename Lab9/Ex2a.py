# Open a CSV file and calculate the average, min, max for the Annual_Salary field
# Name: Reesa Zhou
# Date: October 21, 2026

import csv
csvFileName = "Untitled spreadsheet - Sheet1.csv"
salaries = []

with open(csvFileName, mode="r") as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)
    print(F"Headers: {headers}")
    salaryIndex = headers.index("Annual_Salary")
    for row in reader:
        salary = float(row[salaryIndex])
        salaries.append(salary)

    averageSalary = sum(salaries) / len(salaries)
    minSalary = min(salaries)
    maxSalary = max(salaries)

    print(F"Average salary: ${averageSalary:.2f}")
    print(F"Minimum salary: ${minSalary:.2f}")
    print(F"Maximum salary: ${maxSalary:.2f}")
