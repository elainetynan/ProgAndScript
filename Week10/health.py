# personsmodule.py
#
# Use person module
#
# Author: Andrew Beatty

from personmodule import *
import datetime as dt

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