"""
elif else都必须和if语句联合使用，不能单独使用

if 条件1:
    ...
elif 条件2:
    ...
elif 条件3:
    ...
else:
    以上条件都不满足，执行当前代码。
"""
holiday = "情人节"

if holiday == "平安夜":
    print("应该买苹果，吃大餐")
elif holiday == "情人节":
    print("买玫瑰，看电影")
elif holiday == "生日":
    print("生日快乐")
else:
    print("每天都是节日呀")