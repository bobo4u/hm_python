xiaoming_dict = {"name":"小明"}

# 取值,字典指定的是key而不是索引
print(xiaoming_dict["name"])

# 增加/修改
xiaoming_dict["age"] = 18

# 删除
xiaoming_dict.pop("name")

print(xiaoming_dict)