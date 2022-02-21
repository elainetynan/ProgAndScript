# studentUtil.py
#
# Functions for menu driven app to manage Student details
# 
# Author: Elaine Tynan

def displayMenu():
    print("\n\n")
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    return input("Type one letter (a/v/q):").strip()

def doAdd(students):
    curStudent = {}
    curStudent["name"] = input("Please enter a name: ")
    curStudent["modules"] = readModules()
    students.append(curStudent)

def readModules():
    goOn = "y"
    moduleList = []
    while(goOn == "y"):
        curDict = {}
        curDict["module name"] = input("Please enter a module: ")
        curDict["grade"] = int(input("please enter a grade: "))
        moduleList.append(curDict)
        goOn = input("Would you like to add another module: y (for yes), n (for no) ")
    return moduleList

def doView(students):
    print("\n~~~~~~~~~~~~~~~~")
    for dtls in students:
        print("Name: ",dtls["name"])
        print("Modules:")
        for module in dtls["modules"]:
            print(module["module name"],":",module["grade"])
        print("~~~~~~~~~~~~~~~~")