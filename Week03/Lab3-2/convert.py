# convert.py
#
# Enter an amount in dollars and cent.
# Output the absolute value in cent.
# I am asol rounding the value in case a user puts in more than 2 decimal places.
#
# Author: Elaine Tynan


num = float(input("Please enter an amount in dollars and cent: $"))
# amtInCent = int(abs(num)*100)
amtInCent = int(round(abs(num))*100)
print("The amount in cent is {}".format(amtInCent))