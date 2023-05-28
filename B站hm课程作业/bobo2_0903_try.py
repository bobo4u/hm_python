# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("U can't divide by zero!")

filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'sorry, the file{filename} does not exist.')
