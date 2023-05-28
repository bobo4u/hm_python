# 继承的代码实现代码的重用，相同的代码不需要重复的编写
# 子类拥有父类的所有的方法和属性

class Animal:

    def eat(self):

        print("吃")



class Dog(Animal):

    def bark(self):

        print("叫")

class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

# 定义一个变量
wangcai = XiaoTianQuan()
wangcai.eat()
wangcai.bark()
wangcai.fly()