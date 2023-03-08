"""
python2.2引入了yield关键字，yield关键字可以用来定义生成器函数，生成器函数可以用来生成迭代器，
"""


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        yield index
        index += 1


if __name__ == '__main__':
    for x in lazy_range(5):
        print(x)  # 0, 1, 2, 3, 4
