"""
从一个模块中导入多个类，用逗号分隔各个类。导入必要的类，就可以根据需要创建每个类的任意数量实例。
from car import Car,ElectricCar

导入整个模块
import car
使用语法
module_name.ClassName访问需要的类

"""
from random import randint,choice

a = randint(1,6)

b = [1,4,8,15,21]

c = choice(b)
print(a)
print(b)
print(c)