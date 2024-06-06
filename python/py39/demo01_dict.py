from collections import ChainMap


def test_chain_map():
    """
    ChainMap 类可以用于合并多个字典
    但是，如果多个字典中有相同的键，只有第一个字典中的键值对会被保留
    而且，对合并后的 ChainMap 对象的修改会影响到第一个字典
    """
    d1 = {'a': 1, 'b': 11}
    d2 = {'b': 2}
    merged = ChainMap(d2, d1)
    merged['b'] = 3
    print(merged)
    print(d2)
