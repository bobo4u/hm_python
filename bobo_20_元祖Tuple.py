"""
元祖Tuple,用()定义

"""
empty_tuple = (5,)
print(type(empty_tuple))

into_tuple = ("liuzhenbo",1.7,150)
print(type(into_tuple))

for my_info in into_tuple:
    
    # 元祖中保存的数据类型不一样
    print(my_info)
# List与Tuple转换
abc = list(into_tuple)
print(abc)
print(type(abc))