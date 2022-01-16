"""
0-100之间所有数字的累计求和结果

"""
i = 0
sum = 0
sum_1 = 0
sum_2 = 0
while i <= 100:
    # print(i)
    # sum变量和i这个计数器相加
    sum += i
    if i % 2 == 0: #计算i是否是偶数，如果是则计算if代码块中的部分。
        sum_2 += i
    else:
        sum_1 += i #计算i是否是偶数，不是则计算else代码块中的部分。
    i += 1
print(i)
print("0-100累计相加等于 %d"% sum)
print("0-100的奇数累计相加等于 %d"% sum_1)      
print("0-100的偶数累计相加等于 %d"% sum_2)   
