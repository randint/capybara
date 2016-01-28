def fact(n):
    return 1 if(n <= 1) else n * fact(n - 1)

def combinations(n, k):
    return fact(n) / ((fact(n - k) * fact(k)))

def fact_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(fact(5))
print(fact_iter(5))