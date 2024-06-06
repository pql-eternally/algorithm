import numpy as np
import torch


def test_create_tensor():
    arr = np.ones([3, 3])
    print(f'NDArray shape is {arr.shape}, dtype is {arr.dtype}')
    t = torch.tensor(arr)
    print(t)


def test_create_from_numpy():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    # 原始arr和tensor数据内存共享
    t = torch.from_numpy(arr)
    print(t)

    # 修改numpy数组的值
    arr[0, 0] = 0
    print(arr)
    print(t)

    # 修改tensor的值
    t[0, 0] = -1
    print(arr)
    print(t)


def test_create_ones():
    t = torch.ones([2, 3])
    print(t)


def test_create_full():
    t = torch.full([2, 3], 7)
    print(t)


def test_create_arange():
    """
    创建等差数列的1维张量
    """
    t = torch.arange(2, 10, 2)
    print(t)


def test_create_linspace():
    """
    创建均分的1维张量
    """
    t = torch.linspace(2, 10, 5)
    print(t)


def test_create_logspace():
    """
    创建对数均分的1维张量
    """
    t = torch.logspace(2, 10, 5, base=2)
    print(t)


def test_create_eye():
    """
    创建单位矩阵
    """
    t = torch.eye(4, 4)
    print(t)


def test_create_rand():
    """
    创建随机数张量
    """
    t = torch.rand(3, 3)
    print(t)


def test_create_normal():
    """
    创建正态分布张量
    """
    # mean: 均值, std: 标准差
    mean = torch.arange(1, 5, dtype=torch.float)
    std = torch.arange(1, 5, dtype=torch.float)
    t_normal = torch.normal(mean, std)
    print(f'{mean}\n{std}\n')
    print(t_normal)
