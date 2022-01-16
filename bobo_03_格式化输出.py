#格式化字符串 %s
name = "bobo"
print("我的名字叫小刘，请多多关照!")

print("我的名字叫%s，请多多关照!"% name)

#格式化整数变量 %d
student_no = 100
print("我的学号是 00001 ")
print("我的学号是 %06d " % student_no )

#格式化浮点数 %f
price = 8.5
weight = 7.5
money = price * weight

print("苹果单价 %.2f 元/斤，购买了 %.2f 斤，需要支付 %.4f 元 " %(price,weight,money) )

#格式化 百分号%
scale = 0.50 * 100
print("数据比例是%.2f%%" % scale)