# T2.1-readInNumers.py
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
            print("That was not a number")
    return num

num1 = readNum()
num2 = readNum("Please enter another number: ")

answer = num1 * num2

print(f"Answer is {answer}")