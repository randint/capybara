import re

filename = input("File name to search: ")
f = open(filename, 'r')
contents = f.read()
f.close()

while "Dave is awesome":
    expression = input("Enter regular expression (leave blank to quit): ")
    replace = input("Enter replacement: ")
    contents = re.sub(expression, replace, contents)
    print(contents)

out_filename = "Filename to save to (blank to exit without saving):"
if out_filename != '':
    out = open(out_filename, 'w')
    out.write(contents)
    out.close()
