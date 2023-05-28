numbers = int(input("你有几门考试出成绩了： "))
courses = []
# for i in range(0,numbers):
#     course = int(input("成绩是: "))
#     courses.append(course)
i = 0
while i < numbers:
    course = float(input("成绩： "))
    courses.append(course)
    i+=1
print(courses)
i = 0
while i <= numbers-1:
    print(courses[i])
    i = i + 1
