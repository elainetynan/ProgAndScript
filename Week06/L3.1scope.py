# L3.1scope.py
#
# Variable scope practice
#

x = 7

def toPower(number, power=3):
    global x # Tells it to use the global variable x
    x = 3
    print ("In function: ",x)
    return number ** power

toPower(4)
print("Outside function x is", x)