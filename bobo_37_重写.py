# 当父类的方法没办法满足子类需求，对方法进行重写(override)

class Animal:

    def eat(self):

        print("吃")



class Dog(Animal):

    def bark(self):

        print("叫")

class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

# 子类定义父类一个同名的方法
    def bark(self):
        print("叫2")

# 在父类的方法之上，扩展新的功能. 
# super().eat()
    def eat(self):
        # 1.特有需求
        print("吃吃")
        # 2.使用super(),调用父类
        super().eat()
        # 3.增加其他子类的代码
        print("好")

  
xtq = XiaoTianQuan()
xtq.bark()
print("*" * 20)
xtq.eat()