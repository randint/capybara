# Find the largest prime under 10000 for which any substring of the prime is also prime
# ex: given 257, all substrings must be prime: 2, 25, 257, 5, 57, 7

import math
import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 6
    while k <= math.sqrt(n):
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k = k + 6
    return True

def is_paulian(n):
    n = str(n)
    for start_index in xrange(len(n)):
        for end_index in xrange(start_index + 1, len(n) + 1):
            num = int(n[start_index : end_index])
            if not is_prime(num):
                return False
    return True
            
start_range = 1
end_range = 1000000

start_time = time.time()
for i in xrange(start_range, end_range + 1):
    if (is_paulian(i)):
        print i
print time.time() - start_time
