# Read taxi_1000.csv and calculate:
# the total of all fares
# average fare
# max trip distance
# Name: Reesa Zhou
# Date: October 23, 2026

import csv

fileName = "taxi_1000.csv"

with open(fileName, "r") as file:
    csvReader = csv.reader(file)

    totalFare = 0.0
    maxDistance = 0.0
    averageFare = 0.0
    numRows = 0

    for row in csvReader:
        if numRows == 0:
            fareIndex = row.index("Fare")
            distanceIndex = row.index("Trip Miles")
            numRows += 1
            continue

        if numRows > 0:
            fare = float(row[fareIndex])
            distance = float(row[distanceIndex])
            if fare > 10:
                totalFare += fare
                if distance > maxDistance:
                    maxDistance = distance

        numRows += 1

averageFare = totalFare / (numRows - 1)

print(F"Total Fare: ${round(totalFare)}")
print(F"Average Fare: ${round(averageFare, 2)}")
print(F"Max Trip Distance: {maxDistance} mi")
