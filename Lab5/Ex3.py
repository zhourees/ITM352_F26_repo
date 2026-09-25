# Zip together trip information and print keys, and values
# Name: Reesa Zhou
# Date: September 23, 2026

respondentIds = (1012, 1035, 1021, 1053)
responses = [5, 7, 3, 8]

surveyDict = dict(zip(respondentIds, responses))

print("Survey dictionary:", surveyDict)
print("Dictionary keys:", surveyDict.keys())
print("Dictionary values:", surveyDict.values())

