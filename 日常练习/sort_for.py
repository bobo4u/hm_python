numbers = int(input("一共出了几门成绩: "))
scores = []
for i in range(0,numbers):
    score = int(input("考试成绩分别是: "))
    scores.append(score)
print(scores)
# for a in range(0,numbers-1):
for a in range(0,numbers):
    for i in range(0,numbers-1):
            if scores[i] < scores[i+1]:
                swap = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = swap
print("*****************")
print(scores)

