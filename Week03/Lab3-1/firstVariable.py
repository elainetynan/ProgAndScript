# firstVariable.py
#
# A program to investigate variable types
#
# Author: Elaine Tynan

ageOfPatient = {}
age = '3'

# We need to convert type to str so we can concatenate it to the message
print("Type of ageOfPatient is : "+ str(type(ageOfPatient)))
print("Type of age is: "+str(type(age)))

# Show how to convert a str to int and an int to str
print("You are " + str(age))
nextYear = int(age) +1
print("Next year you will be "+ str(nextYear))