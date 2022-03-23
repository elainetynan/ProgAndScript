# messingwithinst.py
#
# Messing with objects
#
# Author: Andrew Beatty

class Nameofclass:
    name = ""
    last = ""

    def getfullname(self):
        return self.name + " "+ self.last

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'Elaine'
inst2.last = 'Tynan'
person = inst

print(person.name)
# print(person['name']) # Can't do this

inst.last = "Tynan"
print(person.getfullname())

# Confirming strings are not mutable (pass by value or reference)
str1 = "abc"
str2 = str1
str1 += "def"
print(str2)