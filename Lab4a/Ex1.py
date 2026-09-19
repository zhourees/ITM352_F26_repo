# Creates outputs of the user's full name using different string formatting + lists
# Name: Reesa Zhou
# Date: September 16, 2026

first = input("Enter your first name: ");
middleInitial = input("Enter your middle initial: ");
last = input("Enter your last name: ");

fullName = first + " " + middleInitial + ". " + last;
print("Your full name is:", fullName);

print(F"Your full name using an F string is: {first} {middleInitial}. {last}");
print("Your full name using percent s is %s %s. %s" % (first, middleInitial, last));
print("Your full name using format method is: {} {}. {}".format(first, middleInitial, last));
print("Your full name using list joins is: " + " ".join([first, middleInitial + ".", last]));

fullNameList = [first, middleInitial, last];
print("Your full name using the unpacking method is: {} {}. {}".format(*fullNameList));