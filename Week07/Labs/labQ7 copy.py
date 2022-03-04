# labQ7.py
#
# Menu driven app to manage Student details and sve them to a file
#
# Author: Andrew Beatty

import json
import os

students = []
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

def doLoad():
    x = type(students)
    print("### Type",x)
    return readDict()

def readDict():
    global students
    # this will throw an error if the file does not exist
    # it should really just return an empty dict
    # we can do this later
    if os.path.exists(filename):
        with open(filename, "rt") as f:
            students = json.load(f)
            print("*********************")
            print(students)
            print("*********************")
    x = type(students)
    print("### Type",x)
#            dataDict = json.loads(f)
#            splitArr = getStartIndexStudent(dataDict)
#            start = splitArr[0]
#            for i in range(1,len(splitArr)):
#                curStudent = dataDict[start,i]
#                studentItem = getStudentEntry(curStudent)
#                students.append(studentItem)
#                start = i
#            
#            curStudent = dataDict[start]
#            studentItem
#            students.append(studentItem)

def getStartIndexStudent(dataDict):
    splitArr = []
    i = 0
    while i > -1:        
        index = dataDict.find('{"name"')
        if (index > -1):
            splitArr.append(index)
    return splitArr

def getStudentEntry(studentStr):
    curStudent = {}
    curStudent["name"] = getNameFromString(studentStr)
    curStudent["modules"] = getModulesFromString(studentStr)
    return curStudent

def getNameFromString(studentStr):
    start = studentStr.find(': "'+3)
    end = studentStr.find('",')
    return studentStr[start:end]

def getModulesFromString(studentStr):
    goOn = True
    modulesList = []
    while goOn:
        start = studentStr.find('"module name":'+15)
        end = studentStr.find('",')
        moduleDict = {}
        moduleDict["module name"] = studentStr[start:end]
        gradeStart = studentStr.find('grade":'+9)
        gradeEnd = studentStr.find('}',gradeStart)
        moduleDict["grade"] = studentStr[gradeStart:gradeEnd]
        modulesList.append(moduleDict)
        if studentStr[gradeEnd+1] == "]":
            goOn = False
    return modulesList

#main program
doLoad()
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
