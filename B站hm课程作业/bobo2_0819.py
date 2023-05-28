def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        # 增加字典的key与value
        person['age'] = age
    return person


name = build_person('liu','bo',age=30)

print(name)