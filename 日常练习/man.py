class Man:
    def __init__(self,name):
        self.name = name
        print("Initialized")
    def hello(self):
        print("hello" + self.name + "!")
    def goodbye(self):
        print("Good-bye" + self.name + "!")    

m = Man("Bobo Liu")
m.hello()
m.goodbye()