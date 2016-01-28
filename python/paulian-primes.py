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
    while k <= math.sqrt(n) + 1:
        if n % (k - 1) == 0 or n % (k + 1) == 0:
            return False
        k += 6
    return True

def is_paulian(p):
    p = str(p)
    for start_index in range(len(p)):
        for end_index in range(start_index + 1, len(p) + 1):
            if not is_prime(int(p[start_index : end_index])):
                return False
    return True

# start_time = time.time()
# start_range = 1
# end_range = 1000000
# for n in range(start_range, end_range + 1):
#     if is_paulian(n):
#         print(n)
# print(time.time() - start_time)

def expand_paulian(p, limit):
    if is_paulian(p):
        print(p)
    if len(p) >= limit:
        return p
    else:
        if p[-1] == "3":
            return expand_paulian(p + "7", limit)
        else:
            return expand_paulian(p + "3", limit)

expand_paulian("7", 996)