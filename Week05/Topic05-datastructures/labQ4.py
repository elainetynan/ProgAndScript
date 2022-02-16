# labQ4.py
# List queue
# Author: Elaine Tynan

student = {
    "name": "Elaine",
    "modules": [
        {
            "name": "Prog & scripting",
            "grade": 99
        },
        {
            "name": "Computational Thinking",
            "grade": 80
        }
    ]
}

print(student)
print("~~~~~~~~~~~~~~~~~~~")
print("Student:",student["name"])
for module in student["modules"]:
    print("Module:", module["name"], "   Grade:",module["grade"])