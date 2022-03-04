# T2.1-readInNumers.py
#
# Read in 2 numbers are multiply them.
#
# Author: Andrew Beatty


# num1 = False
# while num1 == False:
#    try:
#        num1 = int(input("Please enter a number: "))      

def readNum(message="Please enter a number: "):
    while True:
        try:
            num = int(input(message))
            break
        except ValueError:
            print("That was not a number", end="") # end="" does not go to a new line
    return num

num1 = readNum()
num2 = readNum("Please enter another number: ")

answer = num1 * num2

print(f"Answer is {answer}")