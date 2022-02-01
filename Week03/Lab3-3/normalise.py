# normalise.py
# 
# Reading in a string and strips any leading or trailing spaces and converts 
# all letters to lowercase.
# It also outputs the length of the input and output strings (before and 
# after stripping spaces)
#
# Author: Elaine Tynan

text = input("Please enter a string: ")
normalisedText = text.strip().lower()

inputLength = len(text)
outputLength = len(normalisedText)

print("The string normalied is: {}".format(normalisedText))
print("We reduced the input from {} to {}".format(inputLength, outputLength))