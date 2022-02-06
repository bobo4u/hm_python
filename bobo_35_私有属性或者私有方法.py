"""
属性或者方法名前  ＋ 下划线
"""


class Women:

    def __init__(self,name):
        self.name = name
        self.age = 18 

    def __secret(self):
        
        print("%s 的年龄是 %d 私有方法" %(self.name,self.age))

xiaofang = Women("小芳")

print(xiaofang.name)
print(xiaofang.age)
xiaofang._Women__secret()