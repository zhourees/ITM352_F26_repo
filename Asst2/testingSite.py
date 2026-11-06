def addNum(num1, num2):
    while True:
        try:
            return num1 + num2
        except:
            print("This is an invalid operation. Try again.")
            continue

def subtractNum(num1, num2):
    while True:
        try:
            return num1 - num2
        except:
            print("This is an invalid operation. Try again.")
            continue

numbers = (1,2)

dashboard = {
    "Add":addNum(*numbers),
    "Subtract":subtractNum(*numbers)
}

def selectOperator():
    while True:
        print("\nDashboard:")
        for label, (operator) in enumerate(dashboard, start=1):
            print(F"{label}. {operator}")
        selection = int(input("\nPlease choose operator: "))
        try:
            output = list(dashboard.keys())[selection-1]
            return dashboard[output]
        except:
            print("\nThis does not work. Try again.")
            continue

retry = True

while retry == True:
    print(selectOperator())
    retry = input("Do you want to retry? Y/N: ")
    if retry == "Y":
        retry = True
    elif retry == "N":
        retry == False

    if retry == True:
        continue
    elif retry == False:
        break
