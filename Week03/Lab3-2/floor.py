# floor.py
#
# Enter a decimal number and round it down to its nearest whole number
#
# Author: Elaine Tynan

import math

num = float(input("Please enter a decimal number: "))
numFloored = math.floor(num)
print("{} floored is {}".format(num, numFloored))