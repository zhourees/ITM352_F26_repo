# Parse through the portions of an email address and print out the username and domain name
# Name: Reesa Zhou
# Date: September 18, 2026

emailAddress = input("Enter an email address: ")
parts = emailAddress.split("@")
username = parts[0]
domainName = parts[1]

print("Parts of the email address:", parts)
print("Username:", username)
print("Domain name:", domainName)

# Method 2: using index and slicing

atSignIndex = emailAddress.index("@")
username2 = emailAddress[:atSignIndex]
domainName2 = emailAddress[atSignIndex + 1:]

print("Username (method 2):", username2)
print("Domain name (method 2):", domainName2)
