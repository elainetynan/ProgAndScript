# messingWithJson.py
#
# Learning about the json module
#
# Author: Andrew Beatty

import json

filename = "storeData.json"
electricBill = {
    'name': 'Andrew',
    'amount': '999'
}

with open(filename, "wt") as f:
    json.dump(electricBill, f) # writes the dictionary obj to the file as a json object

with open(filename, "rt") as f:
    readDict = json.load(f) # reads and converts the json object into a list of dictionary
    print(readDict["name"])