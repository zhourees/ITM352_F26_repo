# Check if a list of expenses goes over the user's set budget
# Name: Reesa Zhou
# Date: October 2, 2026

recentPurchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 60
totalSpent = 0

for purchase in recentPurchases:
    totalSpent += purchase
    if totalSpent > budget:
        print(F"This purchase of {purchase} exceeds our budget.")
        break
    else:
        print(F"This purchase of {purchase} is within budget.")
