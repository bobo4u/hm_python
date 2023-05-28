# 将多个字典放在一个列表中，再进行遍历

from sympy import plotting


card_list = [
    {"name":"张三",
     "qq":"12345",
     "phone":"10010"},
    {"name":"李四",
     "qq":"54321",
     "phone":"10086"},
]
print(card_list[0])

print("***" * 15)

for card_info in card_list:
    print(card_info)