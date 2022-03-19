# myFunctionsLogging.py
#
# Factorial to practice testing with logging
#
# Author: Andrew Beatty

import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING) # Won't see the debug messages

def factorial(num):
    if num < 0:
        logging.warning("Factorial recieved a number less than 0")
        return -1

    if num == 0:
        return 1
    
    factorial = 1
    for i in range(1,num+1):
        logging.debug("Before mult:%s by %d",factorial, i)
        factorial *= i
        logging.debug("After mult: %s",factorial)
        #print()
    return factorial

if __name__ == "__main__":
    #print("In myFunctions.py",__name__)
    #print(factorial(7),__name__) # 7! is 5040
    assert factorial(7) == 5040
    assert factorial(-1) == 5040
#factorial(7)