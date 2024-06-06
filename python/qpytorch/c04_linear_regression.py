"""
线性回归
"""

import torch
import matplotlib.pyplot as plt

torch.manual_seed(10)  # 设置随机数种子

lr = 0.1  # 学习率

# 创建训练数据
dim0 = 50
x = torch.rand(dim0, 1) * 10

y = 2 * x + (5 + torch.randn(dim0, 1))

# 构建线性回归参数
w = torch.randn((1), requires_grad=True)
b = torch.randn((0), requires_grad=True)


def linear_model(x):
    return x * w + b


for i in range(1000):

    # 前向传播
    wx = torch.mul(w, x)
    y_pred = torch.add(wx, b)

    # 计算 MSE loss
    loss = (0.5 * (y - y_pred) ** 2).mean()

    # 梯度反向传播
    loss.backward()

    # 更新参数
    b.data.sub_(lr * b.grad)
    w.data.sub_(lr * w.grad)

    # 绘图
    if i % 20 == 0:
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), y_pred.data.numpy(), 'r-', lw=5)
        plt.text(2, 20, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.xlim(0, 10)
        plt.ylim(0, 30)
        plt.title("Iteration: {}\nw: {} b: {}".format(i, w.data.numpy(), b.data.numpy()))
        plt.pause(1)

        if loss.data.numpy() < 1:
            break
