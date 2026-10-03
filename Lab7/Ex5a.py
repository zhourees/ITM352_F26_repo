# Use a loop to append tuple elements to two lists, then combine them into a dictionary
# Name: Reesa Zhou
# Date: October 2, 2026

celebs = ("Ariana Grande", "Sabrina Carpenter", "Keyshia Cole", "Hayley Williams", "Laufey")
ages = (33, 27, 44, 37, 27)

celebList = []
celebList.append("Ariana Grande",)
celebList.append("Sabrina Carpenter",)
celebList.append("Keyshia Cole",)
celebList.append("Hayley Williams",)
celebList.append("Laufey",)

ageList = []
ageList.append(33,)
ageList.append(27,)
ageList.append(44,)
ageList.append(37,)
ageList.append(27,)
celebsDict = {"celebs": celebList,
              "ages": ageList}

print(celebsDict)
