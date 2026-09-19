# Simple dictionary example

countryCapitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "France": "Paris"
}

print("Country capitals:", countryCapitals)
print(countryCapitals["Canada"])

countryCapitals["England"] = "London"
print(countryCapitals["England"])

print("Germany" in countryCapitals)
print("Spain" not in countryCapitals)
