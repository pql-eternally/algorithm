"""
Epoch: 所有训练样本都已输入到模型中，称为一个Epoch
Iteration: 一批训练样本输入到模型中，称为一个Iteration
BatchSize: 批大小，一批训练样本的个数，决定了一个Epoch中有多少个Iteration

举例：
样本总数：80，BatchSize：8
1 Epoch 10 Iteration

样本总数：87，BatchSize：8
1 Epoch 10 Iteration drop_last = True
1 Epoch 11 Iteration drop_last = False

Dataset 是一个抽象类，所有的数据集都应该继承它，并且覆写其中的两个方法：
__getitem__：返回一条数据或一个样本，一般返回的是一个 tuple 或者 dict
__len__：返回样本的数量

"""
