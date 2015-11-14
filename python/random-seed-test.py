import random

'''
Run this program multiple times.

Questions:
1) Which is the only group that changes in each trial?
2) Which group repeats the same line?
3) What line do Groups 1, 2, and 3 have in common?

'''

def randBits(length):
    bitstring = ''
    for i in range(0, length):
        bitstring += str(random.randint(0,1))
    return bitstring

def randChars(length):
    charString = ''
    for i in range(0, length):
        charString += chr(random.randint(65,90))
    return charString

# single seed
print "Group 1"
random.seed(5)
for i in range(0, 3):
    print randChars(5)
print

# single seed identical
print "Group 2"
random.seed(5)
for i in range(0, 3):
    print randChars(5)
print

# repeated seed
print "Group 3"
for i in range(0, 3):
    random.seed(5)
    print randChars(5)
print

# random seed (system time)
print "Group 4"
random.seed()
for i in range(0, 3):
    print randChars(5)
print
