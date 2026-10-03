# Create a function for the things in Ex 4, then write test cases
# Name: Reesa Zhou
# Date: October 2, 2026

recentPurchases = [36.13, 23.87, 183.35, 22.93, 11.62]
passCheck = [6.13, 3.87, 3.35, 2.93, 1.62]
failCheck = [86.13, 3.87, 3.35, 2.93, 1.62]
budgetLimit = 60
totalSpent = 0

def budgetCheck(purchase, budget):
    global totalSpent
    for price in purchase:
        totalSpent += price
        if totalSpent > budget:
            print(F"This recent purchase of {price} exceeds the budget.")
            totalSpent = 0
            break
        else:
            print(F"This recent purchase of {price} is within the budget.");

budgetCheck(recentPurchases, budgetLimit)
budgetCheck(passCheck, budgetLimit)
budgetCheck(failCheck, budgetLimit)
