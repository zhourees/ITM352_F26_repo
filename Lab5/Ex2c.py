# Store trip data in tuple and list, then print information according to user input
# Name: Reesa Zhou
# Date: September 23, 2026

tripDurations = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = dict(zip(tripDurations, tripFares))

print(trips)

tripNum = int(input("Enter the trip number you want: "))

print("The duration of the trip is:", tripDurations[tripNum-1], "miles")
print("The fare of the trip is:", tripFares[tripNum-1])
