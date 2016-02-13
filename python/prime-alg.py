import math

plist = []

def is_prime(n):
    if n < 100:
        return n in plist
    for f in plist:
        if n % f == 0:
            return False
    for f in range(102, round(int(math.sqrt(n))), 6):
        if n % (f - 1) == 0 or n % (f + 1) == 0:
            return False    
    return True


# [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def check_range_of_primes(start_range, end_range):
    for i in range(start_range, end_range + 1):
        pass


plist = generate_primes(100)
print(plist)
print(len(plist))

check_range_of_primes(1, 1000)
