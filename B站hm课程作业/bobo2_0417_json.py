import json
numbers = [1,2,3,4,5,6,7]

filename = "numbers.json"
with open(filename,"w") as f:
    json.dump(numbers,f)
# 函数json.dump接受两个实参：要存储的数据以及可用于存储数据的文件对象。

with open(filename) as n:
    # 函数json.load接受文件名称
    numbers = json.load(n)


print(numbers)