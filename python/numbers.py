class Number:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def __str__(self):
        if self.num % self.den == 0:
            return str(num/den)
        else:
            return "%d/%d" % (num, den)


x = Number(5)
print(x)