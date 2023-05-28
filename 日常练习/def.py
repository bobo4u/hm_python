# 学习创建函数

def inputGardes():
    numbers = int(input("你有几门课： "))
    grades = []
    for i in range(0,numbers):
        grade = int(input("他的成绩是: "))
        grades.append(grade)
    return grades

def printGrades(grades):
    for i in grades:
        print(i)

def AvGrades(grades):
    totle = 0
    ave = 0
    for i in grades:
        totle = totle + int(i)
    ave = totle/len(grades)
    return ave

# def HighLow(grades):
#     # scores.sort(reverse=True)
#     shunxu = grades.sort(reverse=False)
#     return shunxu

def HighLow(grades):
    grades.sort(reverse=True)
    return grades

a = inputGardes()
printGrades(a)
c = AvGrades(a)
d = HighLow(a)
print(c)
print(d)