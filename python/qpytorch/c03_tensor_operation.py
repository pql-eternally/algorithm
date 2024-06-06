import torch


def test_cat():
    """
    将张量按维度dim进行拼接
    dim=0表示行拼接，dim=1表示列拼接
    """
    t = torch.ones([2, 3])
    t_0 = torch.cat([t, t], dim=0)
    t_1 = torch.cat([t, t], dim=1)
    print(t, t.shape)
    print(t_0, t_0.shape)
    print(t_1, t_1.shape)


def test_stack():
    """
    在新创建的维度进行拼接，拓展张量的维度
    """
    t = torch.ones([2, 3])
    t_stack = torch.stack([t, t], dim=0)
    print(t_stack, t_stack.shape)

    t_stack = torch.stack([t, t], dim=1)
    print(t_stack, t_stack.shape)


def test_trunk():
    """
    张量按维度dim进行评价切分
    """
    t = torch.ones([2, 7])
    list_of_tensors = torch.chunk(t, dim=1, chunks=3)
    for idx, t in enumerate(list_of_tensors):
        print(f"第{idx}个张量：{t}, shape is {t.shape}")

    t = torch.ones([4, 4])
    list_of_tensors = torch.chunk(t, dim=0, chunks=2)
    for idx, t in enumerate(list_of_tensors):
        print(f"第{idx}个张量：{t}, shape is {t.shape}")


def test_split():
    """
    张量按维度dim进行切分
    """
    t = torch.ones([2, 5])
    list_of_tensors = torch.split(t, [2, 1, 2], dim=1)
    for idx, t in enumerate(list_of_tensors):
        print(f"第{idx}个张量：{t}, shape is {t.shape}")


def test_index_select():
    """
    在维度dim上，按index索引数据，输出的张量与index的shape一样
    """
    t = torch.randint(0, 9, size=(3, 3))
    idx = torch.tensor([0, 2], dtype=torch.long)  # float
    t_select = torch.index_select(t, dim=1, index=idx)
    print(t)
    print(t_select)


def test_mask_select():
    """
    通过掩码的方式进行数据的选择
    """
    t = torch.randint(0, 9, size=(3, 3))
    mask = t.ge(5)  # ge: greater equal, gt: greater
    print(t)
    print(mask)
    t_select = torch.masked_select(t, mask)
    print(t_select)


def test_reshape():
    """
    张量的形状变换
    """
    t = torch.randperm(8)
    t_reshape = torch.reshape(t, (-1, 2, 2))
    print(f"t: \n{t}")
    print(f"t_reshape: \n{t_reshape}")

    t[0] = 1024
    print(f"t_reshape: \n{t_reshape}")


def test_transpose():
    """
    张量的转置
    """
    t = torch.rand((2, 3, 4))
    t_transpose = torch.transpose(t, dim0=1, dim1=2)
    print(f"t shape: {t.shape}")
    print(f"t_transpose shape: {t_transpose.shape}")


def test_t():
    """
    转置
    """
    t = torch.rand((2, 3))
    t_t = t.t()
    print(f"t: {t} shape: {t.shape}")
    print(f"t_t: {t_t} shape: {t_t.shape}")


def test_squeeze():
    """
    压缩长度为1的维度
    """
    t = torch.rand((1, 2, 3, 1))
    t_sq = torch.squeeze(t)
    print(f"t shape: {t.shape}")
    print(f"t_sq shape: {t_sq.shape}")
    t0 = torch.squeeze(t, dim=0)
    print(f"t0 shape: {t0.shape}")
    t1 = torch.squeeze(t, dim=1)
    print(f"t1 shape: {t1.shape}")


def test_un_squeeze():
    """
    增加维度
    """
    t = torch.rand((2, 3, 4))
    t_unsq = torch.unsqueeze(t, dim=0)
    print(f"t shape: {t.shape}")
    print(f"t_unsq shape: {t_unsq.shape}")
