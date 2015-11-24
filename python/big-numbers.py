import math

def factorial(n):

    answer = 1

    for n in range(1, n + 1):
        answer *= n
        
    return answer

print factorial(5)
print factorial(7)
print factorial(15)
print factorial(10000)
