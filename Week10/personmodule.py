# personsmodule.py
#
# Demonstration of a module
#
# Author: Andrew Beatty

import datetime as dt

def gethealthdata(person):
    print("Get health data:",person['firstname'])

def displayperson(person):
    print(person)

if __name__ == '__main__':
    person1 = {
        'firstname': 'Elaine',
        'lastname': 'Tynan',
        'dob': dt.date(2010,1,1),
        'height': 160,
        'weight': 52
    }

    displayperson(person1)
    gethealthdata(person1)