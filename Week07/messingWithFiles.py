# messingWithFiles.py
#
# Learning about files
#
# Author: Andrew Beatty

# filename = '../test.txt' # to create in parent directory
filename = 'test.txt'
#with open(filename, 'w+t') as f: # w+ allows you to read and write
with open(filename, 'wt') as f:
    f.write("Hello world")
    # f.seek(0) # Go to start of file
    # data = f.readline() # can't be done in write mode
    # print(data)

# filename = "testread.txt"
# with open(filename, "rt") as f:
#    data = f.read()
#    print(data)


filename = "sampleFile.txt"
with open(filename, "rt") as f:
    for line in f:
        print("Line:",line[:-1]) # [:-1] to counteract the carriage retrun from file