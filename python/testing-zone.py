'''
sum = lambda a, b: a + b

def summation(*addends):
    sum = 0
    for addend in addends:
        sum += addend
    return sum

def summation2(num1, num2, *extras):
    sum = num1 + num2
    for addend in extras:
        sum += addend
    return sum

def summation3(addends):
    sum = 0
    for addend in addends:
        sum += addend
    return sum

print("Lambda")
print(sum(1, 1))

print("Summation 1")
print(summation())
print(summation(1, 1, 2))

print("Summation 2")
print(summation2(1, 2, 3, 5))
# Invalid
# print(summation3(1))

print("Summation 3")
print(summation3([1]))
print(summation3([1, 2, 3]))
'''

def lcm(num1, *nums):
    lcm = num1
    for num in nums:
        if num % lcm != 0:
            lcm *= num
    return lcm

def factorize(*nums):
    result = []
    for num in nums:
        prime_factors

# lcm reduced to gcd operation

print(lcm(2, 4, 5, 3))