class Student():
    def __init__(self,first,Last) -> None:
        self.first = first
        self.last = Last
    def inputGrade(self,nu):
        self.nu = nu
        self.grades = []
        for i in range(0,self.nu):
            grade = int(input("请输入你的成绩: "))
            self.grades.append(grade)
        return self.grades

    

s1 = Student('bobo','liu')
a = s1.inputGrade(3)
print(s1.first,s1.last)
print(a)