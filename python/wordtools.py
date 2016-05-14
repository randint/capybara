filename = "PrimeList.txt"

def charcount(filename):
    f = open(filename, 'r')
    data = f.read()
    return len(data)

# print(charcount(filename))


# factorial
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

n = 1
while True:
    print("%d: %d" % (n, fact(n)))
    n += 1

#def thisrunsfirst(function):