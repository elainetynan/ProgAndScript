# randomFruit.py
#
# Get a random fruit from a list of fruit.
#
# Author: Elaine Tynan

import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear', 'Strawberry']
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("Here is a random fruit: {}".format(fruit))