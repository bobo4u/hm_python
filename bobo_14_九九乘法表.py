"""
1*1 = 1
1*2 = 2 2*2 = 4
1*3 = 3 2*3 = 6 3*3 = 9 
"""
row = 1
while row <= 9 :
    col = 1
    while col <= row:
        col +=1
        sum = col * row
        print(" %d * %d =  %d "% (col,row,sum),end="\t")
    print("")
    # print("上面是第%d行" % row)
    row += 1


print("1\t2\t3\t")
print("10\t20\t30\t")

