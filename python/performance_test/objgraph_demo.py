"""
objgraph_demo.py

objgraph is a Python module for creating object diagrams of Python programs.
"""

import objgraph

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
b.append(a)


def func_show_refs():
    # 查看对象的引用关系图
    objgraph.show_refs([a], filename='objgraph_show_refs.png')


def func_show_backrefs():
    # 查看对象的被引用关系图
    objgraph.show_backrefs([b], filename='objgraph_show_backrefs.png')


def func_show_growth():
    class MyBigFatObject(object):
        pass

    def compute_something(_cache={}):
        _cache[42] = dict(foo=MyBigFatObject(),
                          bar=MyBigFatObject())
        # a very explicit and easy-to-find "leak" but oh well
        x = MyBigFatObject()  # this one doesn't leak

    # 查看对象的增长情况
    objgraph.show_growth()
    compute_something()
    print('-' * 80)
    objgraph.show_growth()


if __name__ == '__main__':
    # 查看对象的引用关系图
    func_show_refs()

    # 查看对象的被引用关系图
    func_show_backrefs()

    # 输出最常见实例的类型
    objgraph.show_most_common_types()

    # 查看对象的增长情况
    func_show_growth()
