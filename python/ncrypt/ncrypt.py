import time

wheel = []
for i in range(32, 127): # readable basic ASCII characters
    wheel.append(chr(i))

#f = open("charset", 'r')
#wheel = f.readlines().split()
#wheel = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','#','&','!']

print(wheel)


def encrypt(om):
    s = 0
    key = time.time()
    em = ""
    for i in range(len(om)):


def decrypt(em):
    s = 0
    key = ""
    while em[len(key)] not in wheel:
        key += ""

while True:
    encrypt(input("Message to encrypt: "))