# Get a URL from the user, clean it, and extraft the domain name and TLD (top-level domain)
# Name: Reesa Zhou
# Date: September 18, 2026

url = input("Enter a URL: ")

cleanUrl = url.replace("https://", "")
cleanUrl = cleanUrl.replace("/", "")
print("Clean URL:", cleanUrl)

parts = cleanUrl.split(".")
print("The parts are:", parts)

domainName = parts[1]
tlb = parts[2]
print("Domain name:", domainName)
print("TLB:", tlb)
