"""
逻辑运算
与and
或or
非not
"""
age = 11
if age >=0 and age <= 120:
    print("年龄正确")
else:
    print("年龄输入不正确")

python_score = 50
c_score = 20
if python_score >= 60 or c_score >= 60:
    print("考试通过")
else:
    print("考试失败，还需要努力") 


is_employee = False
if not is_employee:
    print("非本公司人员，请勿入内")