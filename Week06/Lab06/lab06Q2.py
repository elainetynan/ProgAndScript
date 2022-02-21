# lab01Q2.py
#
# Menu driven app to manage Student details
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