#
price_str = input("苹果的单价:")
#
weight_str = input("苹果的重量:")
#注意两个字符串之间不能直接用乘法
#money = price_str * weight_str
#
price = float(price_str)
weight = float(weight_str)
money = price * weight
print(money)
"""
存在的问题:一个数字定义两个变量
input函数定义的变量都是string字符串

"""