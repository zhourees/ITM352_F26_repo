# Scrape data from the City of Chicago's data portal
# Print any line with a <title> tag
# Name: Reesa Zhou
# Date: November 18, 2026

import ssl
import urllib.request

ssl.create_default_https_context = ssl._create_unverified_context()

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
print("Retrieving", url)

response = urllib.request.urlopen(url, context=ssl.create_default_https_context)

for line in response:
    line = line.decode("utf-8").strip()
    if "<title>" in line:
        print(line)
