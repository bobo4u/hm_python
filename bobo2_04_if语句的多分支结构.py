
score = int(input("请输入一个成绩:")) 

if score >=80 and score <=100:
    print("A级别")

# elif score >=60 and score < 80:
elif 60 <= score < 80:
    print("及格")

else:
    print("对不起,成绩有误")