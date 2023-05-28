numbers =int(input("你班级里面有几个学生： "))
message = []
for i in range(0,numbers,1):
    name = input("请输入学生的名字: ")
    average = int(input("请输入他的成绩: "))
    message.append([name,average])
print(message)

while (1==1):
    a = input("请输入你要查询的学生名字: ")

    # for i in message[0:numbers-1][0]:
    #     if i == a:
    #         print(message[0][1])

    for student in message:
        # print(student)
        if student[0] == a:
            print(student[1])