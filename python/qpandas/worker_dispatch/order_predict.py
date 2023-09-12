"""
解决问题：根据历史单量及环境因素等分析预测明天骑手排班计划

影响骑手配送效率因素：
（1）天气因素（雨天、高温、雪天、雾霾）
（2）配送单量
（3）配送距离
（4）配送地址密度
（5）交通道路
（6）骑手技能和经验
（7）骑手装备和工具
（8）商家备餐时间

需要收集数据：
（1）历史单量
（2）历史天气
（3）历史配送距离
（4）历史配送地址密度
（5）历史交通道路
（6）骑手技能和经验
（7）骑手装备和工具
（8）商家备餐时间
（9）明日天气预报

问题拆分：
（1）分析历史天气对单量的影响
（2）明日逐小时单量预测
（3）给现有骑手打标签（全职/兼职）
（4）分析骑手运力
（5）分析历史天气对骑手运力的影响
（6）明日逐小时骑手运力预测
（7）给出明日骑手排班计划

实现思路：
（1）分析历史天气对单量的影响 -- 使用决策树模型分析历史天气对单量的影响
（2）明日逐小时单量预测 -- 使用时间序列模型预测明日逐小时单量
（3）给现有骑手打标签（全职/兼职）-- 使用聚类模型给现有骑手打标签
（4）分析骑手运力 -- 使用聚类模型分析骑手运力
（5）分析历史天气对骑手运力的影响 -- 使用决策树模型分析历史天气对骑手运力的影响
（6）明日逐小时骑手运力预测 -- 使用时间序列模型预测明日逐小时骑手运力
（7）给出明日骑手排班计划 -- 使用排班算法给出明日骑手排班计划

决策树（Decision Tree）：
特点：决策树是一种基于树状结构的预测模型，通过一系列的分裂规则将数据集划分为不同的子集，最终预测目标变量的值。
优点：易于理解和解释；可以处理连续和离散型特征；可捕捉非线性关系。
缺点：容易过拟合；对输入数据的小变动敏感。

随机森林（Random Forest）：
特点：随机森林是一种集成学习方法，通过构建多个决策树并对它们进行组合来进行预测。每个决策树的预测结果通过投票或平均得到最终结果。
优点：具有较高的预测准确度；对异常值和噪声具有一定的鲁棒性；能够处理高维数据。
缺点：模型解释性较差；对于处理大规模数据集可能较慢。

支持向量机（Support Vector Machines, SVM）：
特点：支持向量机是一种用于分类和回归的监督学习算法，通过寻找一个最优的超平面来实现数据的分类或预测。
优点：在高维空间中有效；能够处理非线性关系；对于小样本数据表现良好。
缺点：对大规模数据处理较慢；对于噪声和缺失数据敏感；模型参数选择较为困难。

朴素贝叶斯（Naive Bayes）：
特点：朴素贝叶斯是一类基于贝叶斯定理的分类算法，假设特征之间相互独立。它通过计算给定特征条件下目标变量的概率来进行分类。
优点：简单、易于实现；对小规模数据表现良好；对缺失数据具有较好的鲁棒性；在处理大规模数据时计算效率高。
缺点：由于特征独立性的假设，对于特征之间存在强相关性的数据表现不佳。

神经网络（Neural Networks）：
特点：神经网络是一种模拟人脑神经元网络结构的计算模型。它由多层神经元组成，通过学习数据的权重和偏置来建立输入和输出之间的复杂非线性关系。
优点：适用于处理复杂的非线性问题；能够自动学习特征表示；在图像识别、自然语言处理等领域表现出色。
缺点：对于小样本数据和高维稀疏数据表现较差；需要大量的计算资源和训练时间；模型的解释性较差。

梯度提升树（Gradient Boosting Tree）：
特点：梯度提升树是一种集成学习方法，通过迭代地训练决策树来减小损失函数的梯度。每次迭代都会构建一个新的决策树，将其与之前的树结合起来得到最终的预测结果。
优点：具有较高的预测准确度；能够处理连续和离散型特征；对异常值和噪声具有一定的鲁棒性；能够捕捉非线性关系。
缺点：训练时间较长；对于处理大规模数据集可能较慢；模型的解释性较差。
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import datetime
import time
import os
import math
import random
import xgboost as xgb

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR, SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster import MeanShift
from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import Birch
from sklearn.cluster import OPTICS
from sklearn.cluster import AffinityPropagation

from scipy.cluster.hierarchy import dendrogram, ward
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

from xgboost import plot_importance
from xgboost import XGBRegressor

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf


def load_weather_df():
    """
    天气数据
    """
    dtype = {
        '最低温度': float,
        '最高温度': float,
        '雨量等级': int,
    }
    df = pd.read_csv('../data/北京8月天气.csv', dtype=dtype)
    df['温度'] = (df['最低温度'] + df['最高温度']) / 2
    return df


def load_worker_order_df():
    df = pd.read_csv('./data/北京8月订单.csv')
    df = df.rename(columns={'shipping_date': 'book_day'})
    date_field = 'accepted_at'
    df['date'] = pd.to_datetime(df[date_field])  # 将日期转换为时间格式
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['weekday'] = df['date'].dt.weekday
    return df


def decision_tree_predict(df):
    """
    使用决策树分析历史天气对单量的影响
    要素：温度、降雨量、风速
    """
    # 定义特征和目标变量
    features = ['温度', '雨量等级', '风力']
    target = '单量'

    # 划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2,
                                                        random_state=42)

    # 创建决策树回归模型
    model = DecisionTreeRegressor()
    # 拟合模型
    model.fit(x_train, y_train)
    # 在测试集上进行预测
    y_pred = model.predict(x_test)

    # 评估模型性能
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print("均方误差 (MSE):", mse)
    print("回归评分函数 (R2):", r2)

    # 特征重要性分析
    feature_importance = pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_})
    print('特征重要性分析')
    print(feature_importance)

    # 使用模型进行未来订单量预测
    predict_data = pd.DataFrame({'温度': [26], '雨量等级': [0], '风力': [3]})
    predict_result = model.predict(predict_data)
    print("明日单量预测:", predict_result)


def random_forest(df):
    """
    使用随机森林模型进行预测
    """
    # 划分特征和目标变量
    X = df.drop("target_variable", axis=1)  # 特征
    y = df["target_variable"]  # 目标变量

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80%训练集，20%测试集

    # 创建随机森林回归模型
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)  # 设置100个决策树

    # 在训练集上训练模型
    rf_model.fit(X_train, y_train)

    # 在测试集上进行预测
    y_predict = rf_model.predict(X_test)

    # 评估模型
    mse = mean_squared_error(y_test, y_predict)
    print("均方误差（MSE）:", mse)

    # 特征重要性分析
    feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': rf_model.feature_importances_})
    print('特征重要性分析')

    # 特征重要性可视化
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Importance", y="Feature", data=feature_importance.sort_values(by="Importance", ascending=False))

    # 使用模型进行未来订单量预测
    tomorrow_data = pd.DataFrame({'气温': [26], '降雨量': [0], '风速': [3]})
    predicted_order_quantity = rf_model.predict(tomorrow_data)
    print("明日单量预测:", predicted_order_quantity)


def svr_predict(df):
    # 划分特征和目标变量
    X = df.drop("target_variable", axis=1)  # 特征
    y = df["target_variable"]  # 目标变量

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 创建支持向量机回归模型
    svm_model = SVR(kernel='rbf')  # 选择径向基函数作为核函数

    # 在训练集上训练模型
    svm_model.fit(X_train, y_train)

    # 在测试集上进行预测
    y_predict = svm_model.predict(X_test)

    # 评估模型
    mse = mean_squared_error(y_test, y_predict)
    print("均方误差（MSE）:", mse)


def xgboost_predict(df):
    # 划分特征和目标变量
    X = df.drop("target_variable", axis=1)  # 特征
    y = df["target_variable"]  # 目标变量

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 创建xgboost回归模型
    xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                             colsample_bytree=1, max_depth=7)  # 设置100个决策树

    # 在训练集上训练模型
    xgb_model.fit(X_train, y_train)

    # 在测试集上进行预测
    y_predict = xgb_model.predict(X_test)

    # 评估模型
    mse = mean_squared_error(y_test, y_predict)
    print("均方误差（MSE）:", mse)


def arima_predict(df):
    """
    使用ARIMA模型进行预测
    """
    # 划分特征和目标变量
    X = df.drop("target_variable", axis=1)  # 特征
    y = df["target_variable"]  # 目标变量

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 创建ARIMA模型
    arima_model = ARIMA(y_train, order=(7, 1, 0))  # 设置ARIMA模型的阶数
    arima_result = arima_model.fit(disp=-1)  # 训练模型
    predict = arima_result.predict()  # 预测

    # 评估模型
    mse = mean_squared_error(y_train, predict)
    print("均方误差（MSE）:", mse)


def neural_network_predict(df):
    """
    神经网络（Neural Networks）
    """
    # 划分特征和目标变量
    X = df.drop("target_variable", axis=1)  # 特征
    y = df["target_variable"]  # 目标变量

    # 特征缩放
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 创建神经网络分类器模型
    mlp_model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', random_state=42)

    # 在训练集上训练模型
    mlp_model.fit(X_train, y_train)

    # 在测试集上进行预测
    y_pred = mlp_model.predict(X_test)

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print("准确率:", accuracy)


if __name__ == '__main__':
    weather_df = load_weather_df()
    order_df = load_worker_order_df()
    # 按天统计单量
    day_order_df = order_df.groupby('day').size().reset_index(name='order_count')
    day_order_df = day_order_df.rename(columns={'day': '日期', 'order_count': '单量'})
    df = day_order_df.merge(weather_df, on='日期', how='inner')
    print(df)
