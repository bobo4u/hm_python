"""
石头1
剪刀2
布3
"""
import random


player = int(input("请出拳，石头1，剪刀2，布3: "))
computer = random.randint(1,3)
print("玩家出的是%d，电脑出的拳头是%d"% (player,computer))
# if () or () or 
# 石头胜利剪刀
# 剪刀胜利布
# 布胜利石头
if ((player == 1 and computer == 2) 
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
    
    print("玩家胜利")
elif (player == computer):
    print("居然是平局")
else:
    print("电脑牛皮")