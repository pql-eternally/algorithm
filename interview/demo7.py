"""
函数传参，传递的是什么？
"""
from typing import List


def inc(x: int):
    print(id(x))
    x += 1
    print(id(x))
    return x


def append_list(data: List):
    print(id(data))
    data.append(1)
    print(id(data))
    return data


def change_list(data: List):
    print(id(data))
    if len(data) < 3:
        data = [1, 2, 3]
    else:
        for index, value in enumerate(data):
            if isinstance(value, int):
                data[index] = inc(value)
            elif isinstance(value, list):
                data[index] = append_list(value)
    return data


if __name__ == '__main__':
    data = [1, 2]
    change_list(data)
    print(data)

    data = [1, 2, [3, 4]]
    change_list(data)
    print(data)
