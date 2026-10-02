# 
# Name: Reesa Zhou
# Date: October 2, 2026

celebs = ("Ariana Grande", "Sabrina Carpenter", "Keyshia Cole", "Hayley Williams", "Laufey")
ages = (33, 27, 44, 37, 27)

celebList = []
for celeb in celebs:
    celebList.append(celeb)

ageList = [age for age in ages]

celebsDict = {"celebs": celebList,
              "ages": ageList}
print(celebsDict)
