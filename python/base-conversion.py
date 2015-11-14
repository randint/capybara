# assumes starting from base 10
def printRange(start, end, toBase):
    for i in range(start, end + 1):
        print int(i, base=toBase)

printRange(0, 50, 2)
