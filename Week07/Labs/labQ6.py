# labQ5.py
#
# Menu driven app to manage Student details and sve them to a file
#
# Author: Andrew Beatty

import json

students= []
filename = "students.json"

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj, f)

def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    
    return choice

def doAdd(students):
    curStudent = {}
    curStudent["name"] = input("Please enter a name: ")
    curStudent["modules"] = readModules()
    students.append(curStudent)
    print("in adding")

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

def displayModules(students):
    print("\n~~~~~~~~~~~~~~~~")
    for dtls in students:
        print("Name: ",dtls["name"])
        print("Modules:")
        for module in dtls["modules"]:
            print(module["module name"],":",module["grade"])
        print("~~~~~~~~~~~~~~~~")

def doView(students):
    #for currentStudent in students:
    #    print(currentStudent["name"])
    #    displayModules(currentStudent["modules"])
    displayModules(students)

def doSave(students):
    writeDict(students)
    print("Students saved")

#main program
choice = displayMenu()
while(choice != 'q'):
     # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice !='q':
        print("\n\nPlease select either a,v,s or q")
 
    choice=displayMenu()
