# Define a list of survey response values (5, 7, 3, 8) and store them
# in a variable. Define a tuple of response ids (1012, 1035, 1021, and 1053)
# an add these to the list
# Name: Reesa Zhou
# Date: September 16, 2026

responseValues = [5, 7, 3, 8];
responseValues.sort();
responseIds = (1012, 1035, 1021, 1053);
responseValues.append(responseIds);

print("Combined response values and IDs:", responseValues);

responseValuesNew = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)];
print("Combined response values and IDs as tuples:", responseValuesNew);