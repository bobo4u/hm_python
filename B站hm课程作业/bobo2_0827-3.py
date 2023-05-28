filename = 'guest_book.txt'

while True:
    name = input("请输入名称")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as fl:
            fl.write(name + '\n')
    print("Hi " + name + ", you've been added to the guest book.")

