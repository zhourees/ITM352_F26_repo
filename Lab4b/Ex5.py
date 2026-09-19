# Ask the user for a sentence using input()
# Turn the sentence into a list of string using split()
# Reverse the list
# Join the list back into a string
# Name: Reesa Zhou
# Date: September 18, 2026

sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
reversedSentence = " ".join(words)

print("Reversed sentence:", reversedSentence)

joinedSentence = sentence + " " + reversedSentence
print("Joined sentence:", joinedSentence)
