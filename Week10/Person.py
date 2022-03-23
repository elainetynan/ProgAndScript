# Person.py
#
# Intro to Classes/Objects
#
# Author: Andrew Beatty

class Person:
    # __init__ is the constructor (one of the dunder methods)
    def __init__(self, firstname, lastname, dob, height, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.height = height
        self.weight = weight

    def gethealthstats(self):
        pass

    def display(self):
        print(self)