# Retrieve faculty member names from the ITM webpage and print them from a list
# Name: Reesa Zhou
# Date: November 18, 2026

import ssl
import urllib.request
from bs4 import BeautifulSoup

url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", url)

ssl.create_default_https_context = ssl._create_unverified_context()

itmPage = urllib.request.urlopen(url, context=ssl.create_default_https_context)
itmNames = []

soup = BeautifulSoup(itmPage, "html.parser")
prettySoup = soup.prettify()

print(prettySoup)

faculty = soup.find_all("h2", class_="title")

for person in faculty:
    itmNames.append(person.text)
    print("Faculty:", person.text)

print("Total Faculty:", len(faculty))
