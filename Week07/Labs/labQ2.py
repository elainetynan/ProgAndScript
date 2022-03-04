# labQ2.py
#
# Reads in a number from a file that already exists
#
# Author: Andrew Beatty

filename = "count.txt"

# Question 2a
def readNumber():
    with open(filename) as f:
        number = int(f.read())
    return number

# test it
#num = readNumber()
#print (num)

# Question 2b
def writeNumber(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
#writeNumber(3)

# Question 2c
def readNumber2():
    with open(filename) as f:
        number = int(f.read())
    return number
    
def writeNumber2(number):
    with open(filename, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

# main
num = readNumber2()
num += 1
print ("we have run this program {} times".format(num))
writeNumber2(num)