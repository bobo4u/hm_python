"""
循环:指定的代码按照指定的次数执行

初始条件设置 —— 通常是重复执行的计数器
while 条件(判断 计数器 是否达到 目标次数):
    条件满足时，做1
    条件满足时，做2

    。。。

    处理条件（计数器+1）
"""
i = 1
while i <= 3:
    print("hello Python")
    # 处理条件，避免死循环
    i +=1
print("循环结束后，i是 %d"% i)

