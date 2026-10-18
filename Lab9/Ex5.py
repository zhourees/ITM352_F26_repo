# Program to remove any scores from a list that are below 50.
# Name: Reesa Zhou
# Date: October 17, 2026

scores = [60, 45, 30, 85, 10, 90]
newScores = []

for score in scores: 
    if score >= 50: 
        newScores.append(score) 

print(newScores)
