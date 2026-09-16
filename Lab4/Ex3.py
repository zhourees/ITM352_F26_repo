# Manipulates a list in various tricky ways
# Name: Reesa Zhou
# Date: September 16, 2026

responseValues = [5, 7, 3, 8];
responseValues.append(6);
print("Response values after appending 6:", responseValues);

responseValues.insert(2, 6);

print("Response values after inserting 6 at index 2:", responseValues);

responseValues = responseValues[:2] + [6] + responseValues[2:];
print("Response values after inserting 6 at index 2:", responseValues);
