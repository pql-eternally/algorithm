"""
不用额外变量交换两个数的值
不用额外变量交换数组中两个数的值
"""


def swap() -> None:
    # python版交换两个数的值
    a = 1
    b = 2
    a, b = b, a
    print(f'a = {a}，b = {b}')

    # 使用异或交换两个数
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f'a = {a}，b = {b}')

    # 使用运算
    a = a + b
    b = a - b
    a = a - b
    print(f'a = {a}，b = {b}')

    # 使用第三个变量
    temp = a
    a = b
    b = temp
    print(f'a = {a}，b = {b}')


def main() -> None:
    swap()


if __name__ == '__main__':
    main()
