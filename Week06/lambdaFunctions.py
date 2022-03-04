# More messing with functions
# Anonymous functions
# Author: Andrew Beatty

def tripler(num):
    return num * 3

def doubler(num):
    return num * 2

isMax = False
if isMax:
    fun = lambda num : num * 2
else:
    fun = lambda num : num * 3

var = fun(10)
print(var)

# sorted
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
        {'first':'Grace', 'last':'Hopper', 'YOB':1906},
        {'first':'Alan', 'last':'Turing', 'YOB':1912}]

list = [22, 33, 11, 1, 44]
print(list)
newList = sorted(list)
print(newList)

#def sortFun(item):
#   return item['first']
#
#newData = sorted(data, key = sortFun)
newData = sorted(data, key = lambda item : item['last'])
print(newData)