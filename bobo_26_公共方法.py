"""
len计算元素个数
del删除元素/变量
max元素最大值
min元素最小值
"""
# 运算符
"""
合并+
重复*  字典dict与int不支持
"""
print(1 in [0,1,2])

students = [{"name":"阿土"},
            {"name":"小美"},
            {"name":"小康"}
            ]
find_name = "阿"

for stu_dict in students:
    # print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了")
        break
    else:
        # print(stu_dict)
        print("继续找")
        
else:
    print("抱歉没有找到")
