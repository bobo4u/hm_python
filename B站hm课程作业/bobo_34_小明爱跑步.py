class Person:

    def __init__(self,name,weight) :
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        
        return "我的名字叫 %s 体重是 %.2f公斤" %(self.name,self.weight)

    def run(self):
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 爱吃东西" % self.name)
        self.weight += 1


# 小明
xiaoming = Person("小明",75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)
# 小康
xiaokang = Person("小康",48.0)
xiaokang.eat()
xiaokang.run()
print(xiaokang)



