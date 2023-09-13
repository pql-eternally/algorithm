"""

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def sigmoid(x):
    # Sigmoid 激活函数: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Sigmoid 的导数: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    # y_true and y_pred 都是等长度的 numpy 数组.
    return ((y_true - y_pred) ** 2).mean()


class OurNeuralNetwork:
    '''
    神经网络:
      - 1 个隐藏层，2 个神经元 (h1, h2)
      - 1 个输出层，1 个神经元 (o1)
    '''

    def __init__(self):
        # 权重（weights）
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        # 偏移量（biases）
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
        # x 是有 2个元素的 numpy 数组.
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        '''
        - 数据集是 (n x 2) 的 numpy 数组, n = 数据集中的样本数.
        - all_y_trues 是有 n 个元素的 numpy 数组.
          all_y_trues 中的元素与数据集一一对应.
        '''
        loss_data = []
        learn_rate = 0.1
        epochs = 1000  # 对整个数据集的训练总次数

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- 进行前馈操作 (我们后面要用到这些变量)
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1

                # --- 计算偏导数.
                # --- 命名方式：d_L_d_w1 代表 "dL / dw1"，即 L对 w1求偏导
                d_L_d_ypred = -2 * (y_true - y_pred)

                # 神经元 o1
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

                # 神经元 h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)

                # 神经元 h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)

                # --- 更新权重（w）与偏移量（b）
                # 神经元 h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # 神经元 h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                # 神经元 o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

            # --- 在每10次迭代结束后计算总 loss并打印出来
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse_loss(all_y_trues, y_preds)
                loss_data.append(loss)
                print("Epoch %d loss: %.3f" % (epoch, loss))

        return loss_data


df = pd.read_csv('../data/线上门店天气单量数据.csv')
# 定义数据集 data

#  数据标准化/归一化处理
size = df.index.size
avg_temperature = sum(df['温度']) / size
avg_order = sum(df['单量']) / size
df['温度'] = df['温度'] - avg_temperature
df['星期'] = df['星期'] - 3
df['单量'] = (df['单量'] - avg_order) / avg_order
data = np.array(df[['温度', '星期']])
all_y_trues = np.array(df['单量'])

# 训练我们的神经网络!
network = OurNeuralNetwork()
loss_data = network.train(data, all_y_trues)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel("epoch")  # 横坐标名
ax.set_ylabel("loss")  # 纵坐标名
ax.set_title("Neural Network Loss vs. Epochs")
epoch = range(0, 1000, 10)  # 100个点
plt.plot(epoch, loss_data)  # 绘图
plt.show()

# 神经网络预测
predict_data = np.array([22, 3])
print(f"predict result: {network.feedforward(predict_data)}")
