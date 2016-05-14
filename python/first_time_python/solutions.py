# CHALLENGE 8: Temperature Conversion
# Write a program that converts from Celsius to Fahrenheit and Fahrenheit to Celsius
def challenge8():
    def cToF(celsius):
        return (celsius * 9/5) + 32

    def fToC(fahrenheit):
        return (fahrenheit - 32) * 5/9

    option = ''

    while option != '1' and option != '2':
        option = input("Enter an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")

    if option == '1':
        degrees = int(input("Temperature in Celsius: "))
        print(cToF(degrees))
    elif option == '2':
        degrees = int(input("Temperature in Fahrenheit: "))
        print(fToC(degrees))


# CHALLENGE 11: A simple function/Functions are just code
def challenge11():
    for i in range(97, 97 + 26):
        print(chr(i))

def challenge12(name):
    def happy_birthday(name):
        print("Happy birthday to you")
        print("Happy birthday to you")
        print("Happy birthday, dear " + name)
        print("Happy birthday to you!")

    happy_birthday(name)


# CHALLENGE 13: Taking Multiple Arguments
# Make a function that takes a name, age, weight, and height and prints a bio
def challenge13():
    name = input("Tell me your name: ")
    age = input("Tell me your age: ")
    weight = input("Tell me your weight (in pounds): ")
    height = input("Tell me your height (in inches): ")
    print("%s is %s and weighs %s pounds and is %s inches tall" % (name, age, weight, height))


# CHALLENGE 14: Charlie Oscar Oscar Lima
# Write a program that takes a string and returns the ICAO equivalent
def challenge14():
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    string = input("What is your string? ")
    output = ""
    for c in string:
        if c.lower() in d:
            output = output + d[c.lower()] + ' '
    output = output.strip()
    print(output)


# CHALLENGE 15: Letter Frequency
# Write a function char_freq() that takes a string and returns a frequency listing dictionary of the characters
def challenge15():
    def char_freq(string):
        d = {}
        for c in string:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

    string = input("What is your string? ")
    #print(char_freq(string))
    for thing in char_freq(string):
        print(thing)


# challenge11()
# challenge12("Guido van Rossum")
# challenge13()
# challenge14()
# challenge15()
