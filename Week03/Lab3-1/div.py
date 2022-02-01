# div.py
#
# Divide 2 numbers and print the answer in an aesthetically pleasing way
#
# Author: Elaine Tynan

num1 = int(input("Please enter a whole number: "))
num2 = int(input("Please enter the number you want to divide by: "))
answer = num1 // num2
remainder = num1 % num2
print("{} divided by {} is {} with remainder {}".format(num1, num2, answer, remainder))