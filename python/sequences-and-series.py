import time
import math

def sigma(start, end, diff):
    summation = 0
    for n in range(start, end + 1):
        summation = summation + n * diff
    return summation
    # return (diff * start + diff * end) * (end - start) / 2

'''
def main():
    '''
    for n in range(101):
        print "sum of first " + str(n) + ": " + str(sigma(1, n, 1))
    '''
    print sigma(1, 100, 1)
'''

time_elapsed = 0
n = 1

while time_elapsed < 10:
    start_time = time.time()

    print "Sum of first %i integers: %s" % (n, sigma(1, n, 1))

    time_elapsed = (time.time() - start_time)
    print "%s seconds elapsed\n" % time_elapsed
    n = n * 10

'''
for x in range(100):
    print "factorial(" + str(x) + "): " + str(math.factorial(x))
'''

'''
x = raw_input("Find factorial of __: ")
print factorial(int(x))
'''
