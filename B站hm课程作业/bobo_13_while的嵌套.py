"""
while 条件1:
    条件满足时，做11
    条件满足时，做12
    while 条件2:
        条件满足时，做21
        条件满足时，做22


        处理条件2
    处理条件1
"""
row = 1
"""
第一行输入一个*
第二行输入二个**
第N行输入N个*
while row <=5:
    print("*" * row)
    row += 1
"""
#在每一行引入一个列的概率，列<=行
row = 1
while row <=5:
    col = 1
    while col <= row:
        col += 1
        print("*",end="")  
    print("")
    print("第%d行" % row)
    row +=1


        