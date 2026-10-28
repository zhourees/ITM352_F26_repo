# Create a Pandas dataframe from individual lists, then do simple stats on the data
# Name: Reesa Zhou
# Date: October 23, 2026

import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]


rawData = zip (ages, gender)
df = pd.DataFrame(data=rawData, index=names, columns=["Age", "Gender"])

summary = df.describe()
print(summary)

averageAgeByGender = df.groupby("Gender")["Age"].mean()
print(averageAgeByGender)
