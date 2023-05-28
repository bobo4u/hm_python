"""
列表的定义:List,其他语音通常也叫作数组.
列表的索引从0开始
"""
name_list = ["zhangshan","lisi","wangwu"]
# 取值和取索引
print(name_list[0])
print(name_list.index("lisi"))
# 修改
name_list[1] = "李四"
# 列表指定的索引超出范围 IndexError: list assignment index out of range
# name_list[3] = "李四"
# 增加,append方法向列表的末尾追加数据
name_list.append("xiaoer")
# 指定索引插入数据
name_list.insert(1,"小妹妹")
# extend 方法 把其他列表的内容追加到当前列表
temp_list = ["liu","zhen","bo"]
name_list.extend(temp_list)
# 删除数据
name_list.remove("wangwu")
# 把列表中最后一个数据删除
name_list.pop()
# pop方法指定要删除元素的索引
name_list.pop(3)
# 清空列表
name_list.clear()
print(name_list)



     