# playingWithScope.py
#
# Trying things out
#
# Author: Elaine Tynan

num = 5
List = [
    {
        "name": "Mike",
        "modules": [
            {"module name": "M1", "grade": 99},
            {"module name": "M2", "grade": 88}
        ]
    },
    {
        "name": "Elaine", 
        "modules": [
            {"module name": "M3", "grade": 55}
        ]
    }
]

def scopeFunc():
    global num
    num = 6

def changeList(List):
    #global List
    List = [
        {
            "name": "Mike",
            "modules": [
                {"module name": "M1", "grade": 99},
                {"module name": "M2", "grade": 88}
            ]
        }
    ]

print(List)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
scopeFunc()
print(List)