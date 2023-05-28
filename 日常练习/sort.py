numbers = int(input("you have how many class: "))
scores = []
for i in range(0,numbers):
    score = int(input("你的课程得分是： "))
    scores.append(score)
print(scores)
scores.sort(reverse=True)
print(scores)