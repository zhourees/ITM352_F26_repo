# Analyze an array of tuples using Numpy
# Name: Reesa Zhou
# Date: October 23, 2026

import numpy as np

hhIncome = [
    (10, 14629),
    (20, 25600),
    (30, 37002),
    (40, 50000),
    (50, 63179),
    (60, 79542),
    (70, 100162),
    (80, 130000),
    (90, 184292),
]

hhIncomeArray = np.array(hhIncome)

print(F"Dimensions of the array: {hhIncomeArray.ndim}")
print(F"Number of elements in the array: {hhIncomeArray.size}")

for i in range(hhIncomeArray.shape[0]):
    percentile, income = hhIncomeArray[i]
    print(F"Percentile: {percentile}, Income: {income}")

for i in range (hhIncomeArray.shape[0]):
    print(hhIncomeArray[i, 0], hhIncomeArray[i, 1])
