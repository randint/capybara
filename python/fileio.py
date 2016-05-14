filename = input("File name: ")
with open(filename, 'r') as f:
    for line in f:
        print(line)