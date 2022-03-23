# messingWithInit.py
#
# Messing with init
#
# Author: Andrew Beatty

class Person:
    # __init__ is the constructor (one of the dunder methods)
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    
    def fullname(self):
        if hasattr(self, 'middlename'):
            return self.firstname + " " + self.middlename + " " + self.lastname
        else:
            return self.firstname + " " + self.lastname

    def __str__(self):
        return self.fullname()

    def addmiddlename(self, middlename):
        self.middlename = middlename

if __name__ == '__main__':
    person1 = Person('Elaine', 'Tynan')
    
    print(person1.firstname)
    print(person1.fullname())
    print(person1)
    person1.addmiddlename("Jim")
    print(person1)