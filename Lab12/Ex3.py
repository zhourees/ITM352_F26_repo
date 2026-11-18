# Retrieve faculty member names from the ITM webpage and print them from a list
# Name: Reesa Zhou
# Date: November 18, 2026

import ssl, lxml
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

ssl.create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"
print("Retrieving", url)

itmPage = urllib.request.urlopen(url, context=ssl.create_default_https_context)
itmNames = []

soup = BeautifulSoup(itmPage, "html.parser")
faculty = soup.find_all("h2", class_="title")

