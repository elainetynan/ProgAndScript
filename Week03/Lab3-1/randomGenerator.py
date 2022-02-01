# randomGenerator.py
#
# Get a random number between 2 values selected by the user.
#
# Author: Elaine Tynan

import random

num1 = int(input("Please enter a whole number for the bottom value: "))
num2 = int(input("Please enter another whole number for the top value: "))
num = random.randint(num1,num2)
print("Here is a random number {}".format(num))