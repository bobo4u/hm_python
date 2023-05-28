from itertools import count


name_list = ["liu","zhen","bo"]
# del关键字本质上是将一个变量从内存中删除
"""
del name_list[0]
print(name_list)

name = "wangwu"
del name
# NameError: name 'name' is not defined
print(name)

"""
list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)
name_list.append("liu")
count = name_list.count("liu")
print("出现的liu的次数 %d" % count)

# 列表删除数据
name_list.remove("liu")
print(name_list)


  
