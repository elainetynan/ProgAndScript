# readfrom sources.py
#
# Various ways to read in data to pandas

# Author: Andrew Beatty

import pandas as pd

# Reading in dictionary objects
# The attribute names will be column names
# The index is automatically made
dataAsDictOfList = {
    "Name": [
        "Braund, Mr Owen Harris",
        "Allem, Mr William Henry",
        "Bonnell, Miss Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
}
df = pd.DataFrame(dataAsDictOfList)
#df = pd.DataFrame(dataAsDictOfList, index=['a', 'b', 'c'])

#print(df)
#print(df.describe())

# or

dataAsDictOfDict = {
    "Name": {
        '101':"Braund, Mr Owen Harris",
        '102':"Allem, Mr William Henry",
        '103':"Bonnell, Miss Elizabeth",
    },
    "Age": {'101':22, '102':35, '104':58},
    "Sex": {'101':"male", '102':"male", '103':"female"}
}

df = pd.DataFrame(dataAsDictOfDict)
#print(df)

# or with just lists
dataAsList = [[1, 2, 100, 'male'],
[2, 4, 100, 'male,'],
[3, 8, 100, 'female']]

#df = pd.DataFrame(dataAsList)
df = pd.DataFrame(dataAsList, columns=['x', 'y', 'percent', 'sex'])

print (df)
