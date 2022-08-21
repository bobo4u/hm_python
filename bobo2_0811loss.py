import numpy as np
#定义L1损失函数
def L1_loss(y_true,y_pre): 
    return np.sum(np.abs(y_true-y_pre))
#定义L2损失函数
def L2_loss(y_true,y_pre):
    return np.sum(np.square(y_true-y_pre))

#假设我们得到了真实值和预测值
y_true = np.array([1,2,3,4,5,6,7,8,9])
y_pre  = np.array([1.2,2.3,3.5,4.3,4.6,5.6,6.1,7.1,8.8])

#定义函数
print('L1 loss is {}'.format(L1_loss(y_true,y_pre)))
"""L1 loss is 4.1000000000000005"""
print('L2 loss is {}'.format(L2_loss(y_true,y_pre)))
"""L2 loss is 2.450000000000001"""



def FGSM(image, epsilon, data_grad):
    """
    :param image: 需要攻击的图像
    :param epsilon: 扰动值的范围
    :param data_grad: 图像的梯度
    :return: 扰动后的图像
    """
    # 收集数据梯度的元素符号
    sign_data_grad = data_grad.sign()
    # 通过调整输入图像的每个像素来创建扰动图像
    perturbed_image = image + epsilon*sign_data_grad
    # 添加剪切以维持[0,1]范围
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    # 返回被扰动的图像
    return perturbed_image