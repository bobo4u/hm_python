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
    def printGrades(self):
        for i in range(0,self.nu):
            print(self.grades[i])
    def avGrades(self):
        totle = 0 
        for i in range(0,self.nu):
            totle = totle + self.grades[i] 
        ave = totle / self.nu   

        return ave
    def highLow(self):
        high = 0
        low = 100
        for i in range(0,self.nu):
            if self.grades[i] > high:
                high = self.grades[i]
            if self.grades[i] < low:
                low = self.grades[i]
        return high,low
student1 = Student("liu","bobo")
student1.inputGrade(4)
print(student1.grades)
ave1 = student1.avGrades()
print(ave1)
print(student1.highLow())