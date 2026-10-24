# Create messages if the csv file does not exist or is unreadable
# Name: Reesa Zhou
# Date: October 23, 2026

import csv
import os

if not os.path.exists("Untitled spreadsheet - Sheet1.csv"):
    print("Error: File Untitled spreadsheet - Sheet1.csv not found.")
    exit()

if not os.access("Untitled spreadsheet - Sheet1.csv", os.EX_OK):
    print("Error: File is not readable.")
    exit()
else:
    fileSize = os.path.getsize("Untitled spreadsheet - Sheet1.csv")
    print(F"File exists and is readable. Size: {fileSize} bytes.")

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
