# lab01Q3.py
#
# Menu driven app to manage Student details repeatedly
# 
# Author: Elaine Tynan
import studentUtil as su
#from studentUtil import *

# Call functions to run menu
students = []
choice = su.displayMenu()
while choice != "q":
    if choice == "a":
        su.doAdd(students)
    elif choice == "v":
        su.doView(students)
    elif choice == "q":
        break
    else:
        print("Incorrect option, try again")
    choice = su.displayMenu()