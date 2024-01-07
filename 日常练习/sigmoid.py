import numpy as np

# 阶跃函数
x = np.array([-1.0,2.0,3.0])
# print(sigmoid(x))
y = x > 0
print(y)

y = y.astype(np.int8)

print(y)

# sigmoid函数

def sigmoid(x):
    return 1/(1+np.exp(-x))
