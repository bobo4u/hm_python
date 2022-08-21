
# if True:
#     print('u are good')
# else:
#     print('...')


# guess = eval(input('请输入一个整数：'))
# if guess > 99 or guess < 100:
#     print("best") 


"""
身体质量指数BMI
输入
输出
"""
height,weight = eval(input())

bmi = weight / pow(height,2)

print('BIM 数值为:{:.2f}'.format(bmi))