"""
键key 是索引
值values是数据


"""
xiaoming = {"name":"小明", 
            "age":18 ,
            "gender":True,
            "height":1.72,
            "weight":150}

print(type(xiaoming))

print(len(xiaoming))
# 合并字典
temp_dict = {"company":"中科",
             "age":22,}

xiaoming.update(temp_dict)

print(xiaoming)

# 循环遍历字典，每次训练获取到键值对的key

for key in xiaoming:
    print("%s %s" % (key,xiaoming[key]))