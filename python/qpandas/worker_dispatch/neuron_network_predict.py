"""

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense, concatenate
from tensorflow.python.keras.models import Model
from sklearn.preprocessing import MinMaxScaler, StandardScaler


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


def load_df():
    """
    加载数据，数据标准化/归一化处理
    """
    df = pd.read_csv('../data/线上门店天气单量数据.csv')
    size = df.index.size
    avg_temperature = sum(df['温度']) / size
    avg_order = sum(df['单量']) / size
    df['温度'] = df['温度'] - avg_temperature
    df['星期'] = df['星期'] - 3
    df['单量'] = (df['单量'] - avg_order) / avg_order
    return df


def test_neural_network():
    df = load_df()
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


def test_keras():
    """
    使用keras实现神经网络预测订单量
    """
    df = pd.read_csv('../data/线上门店天气单量数据.csv')

    # 选取需要的特征列，并做数据归一化处理
    feature_columns = ['温度', '星期', '天气', '是否节假日', '是否周末', '是否雨天', '是否晴天',
                       '是否阴天', '是否多云', '风力']
    predict_column = '单量'
    min_max_scaler = MinMaxScaler()
    scaled_x = min_max_scaler.fit_transform(df[feature_columns])

    standard_scaler = StandardScaler()
    scaled_y = standard_scaler.fit_transform(df[[predict_column]])

    # 定义模型
    feature_size = len(feature_columns)
    inputs = Input(shape=(feature_size,))
    x = Dense(feature_size, activation='sigmoid')(inputs)
    x = Dense(feature_size, activation='sigmoid')(x)
    outputs = Dense(1, activation='sigmoid')(x)
    model = Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer='adam', loss='mse')

    # 训练模型
    model.fit(scaled_x, scaled_y, epochs=1000, batch_size=10)

    # 评估模型
    # loss = model.evaluate(scaled_x, scaled_y)
    # print(f"loss: {loss}")

    # 预测结果
    predict_data = {
        '日期': [20230913, 20230914, 20230915],
        '温度': [29, 28, 26.5],
        '星期': [3, 4, 5],
        '天气': [12, 24, 24],
        '是否节假日': [0, 0, 0],
        '是否周末': [0, 0, 0],
        '是否雨天': [0, 1, 1],
        '是否晴天': [0, 0, 0],
        '是否阴天': [0, 0, 0],
        '是否多云': [1, 0, 0],
        '风力': [2, 2, 2],
    }
    predict_df = pd.DataFrame(predict_data)
    predict_data = min_max_scaler.fit_transform(predict_df[feature_columns])
    predict_result = model.predict(predict_data)
    # 预测结果反归一化
    predict_order = standard_scaler.inverse_transform(predict_result)
    predict_df['预测单量'] = predict_order
    # print(f"Day {day} predict order: {predict_order}")
    print(predict_df)


def test_lstm():
    """
    使用LSTM实现神经网络预测订单量
    """
    from tensorflow.python.keras.models import Sequential
    from tensorflow.python.keras.layers import LSTM
    from scikeras.wrappers import KerasRegressor
    from sklearn.model_selection import GridSearchCV

    df = pd.read_csv('../data/线上门店天气单量数据.csv')

    # 选取需要的特征列，并做数据归一化处理
    feature_columns = ['温度', '星期', '天气', '是否节假日', '是否周末', '是否雨天', '是否晴天',
                       '是否阴天', '是否多云', '风力']
    predict_column = '单量'
    min_max_scaler = MinMaxScaler()
    scaled_x = min_max_scaler.fit_transform(df[feature_columns])
    train_x = np.reshape(scaled_x, (scaled_x.shape[0], 1, scaled_x.shape[1]))

    standard_scaler = StandardScaler()
    scaled_y = standard_scaler.fit_transform(df[[predict_column]])
    train_y = np.reshape(scaled_y, (scaled_y.shape[0], 1, scaled_y.shape[1]))

    def build_model():
        model = Sequential()
        model.add(LSTM(10))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='nadam')
        return model

    # 定义模型
    grid_model = KerasRegressor(model=build_model, verbose=0)
    # 定义优化器
    optimizers = ['adam', 'rmsprop']
    # 定义训练次数
    epochs = [10, 50, 100]
    # 定义批次大小
    batches = [5, 10, 20]
    # 定义参数网格
    param_grid = dict(optimizer=optimizers, epochs=epochs, batch_size=batches)
    # 定义网格搜索
    grid = GridSearchCV(estimator=grid_model, param_grid=param_grid, n_jobs=-1, cv=3)
    # 执行网格搜索
    grid_result = grid.fit(train_x, train_y)
    # 打印结果
    print(grid_result)
