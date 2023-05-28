numbers = int(input("你有多少课程： "))
grades = []
for i in range(0,numbers,1):
    grade = input("我的课程得分是：")
    grades.append(grade)
print(grades)
for i in range(0,numbers,1):
    print(grades[i])

