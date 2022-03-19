# myFunctions.py
#
# Factorial to practice testing
#
# Author: Andrew Beatty

def factorial(num):
    if num == 1:
        return 0
    
    factorial = 1
    for i in range(1,num+1):
        #print("Before mult:",factorial,"by",i)
        factorial *= i
        #print("After mult:",factorial)
        #print()
    return factorial

if __name__ == "__main__":
    print("In myFunctions.py",__name__)
    print(factorial(7),__name__) # 7! is 5040
    assert factorial(7) == 5040
    assert factorial(7) == 5040
    assert factorial(7) == 5040
#factorial(7)