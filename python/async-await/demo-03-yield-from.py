"""
python3.3引入yield from，可以简化生成器嵌套的写法。
"""


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0

    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1

    yield from gratuitous_refactor()


if __name__ == '__main__':
    for x in lazy_range(5):
        print(x)  # 0, 1, 2, 3, 4
