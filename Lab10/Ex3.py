# Create a Pandas dataframe from data, then print
# Name: Reesa Zhou
# Date: October 28, 2026

import pandas as pd

data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

df = pd.DataFrame(data)
print(df)
