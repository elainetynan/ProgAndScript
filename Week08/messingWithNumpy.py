# messingWithNumpy.py
#
# Messing with Numpy
#
# Author: Andrew Beatty

import numpy as np

listOfNums = [1,2,3,8]
numbers = np.array([1,2,3,5,6])
print(listOfNums)
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")

#listOfNums = listOfNums + 3 # Can't add  anumber to a list
numbers = numbers + 3 # Whereas this adds 3 to each element in the numbers NumPy array
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")

numbers = numbers * 2
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")

numbers = numbers / 3
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")

numbers = np.array([1,2,3,5,6])

# multiplies each element by its corresponding element
# NumPy arrays must be the same length
numbers = numbers * np.array([1,2,3,2,4])
print(numbers)
print("~~~~~~~~~~~~~~~~~~~~~~")

numbers = np.array([1,2,3,5,6])

# Puts in 5 random numbers from 100 up to but not including 200
randNums = np.random.randint(100, 105, 5)
print (randNums)
print("~~~~~~~~~~~~~~~~~~~~~~")

# A normal distribution
randNums = np.random.normal(size = 100)
print (randNums)
print("~~~~~~~~~~~~~~~~~~~~~~")
