filename = '1.txt'
with open(filename) as file:
    lines = file.readlines()
    print(type(lines))
print(type(filename))
for line in lines:
    print(line.rstrip())