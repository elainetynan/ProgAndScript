# labQ3.py
# List queue
# Author: Elaine Tynan

import random

queue = []
max = int(input("Please enter the max value you would like: "))

for i in range(0,10):
    queue.append(random.randint(0,max))

print("Queue: ", queue)
print("~~~~~~~~~~~~~~~~~")

while len(queue) > 0:
    x = queue.pop(0)
    print("The value popped is:", x, "   The queue is",queue)

print("The queue is empty")