# grades = [100,99,98,97,96]

# for grade in grades:
#     print(grade)

# numbers = int(input("你有几门课呢: "))
# grades = []
# for number in range(1,numbers+1):
#     list = []
#     list.append(number)
#     # print(f'第{number}课')
#     # print(list)
#     for grade in list:
#         grade = input(f"请输入你第{list}的成绩: ")
#         grades.append(grade)
# print(grades)
numbers = int(input("你有几门课呢: "))
grades = []
totle = 0
for i in range(numbers):
    grade = int(input("请输入你的成绩： "))
    grades.append(grade)    
# for i in range(0,numbers,1):
    # print(grades[i])
print("----------------------------")
# print(totle)
for i in grades:
    totle += i
print(totle)
score = totle/numbers
print(score)
print(grades)
a = max(grades)
b = min(grades)

print(a,b)