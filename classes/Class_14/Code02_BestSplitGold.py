"""
一块金条切成两半，是需要花费和长度数值一样的铜板
比如长度为20的金条，不管怎么切都要花费20个铜板，一群人想整分整块金条，怎么分最省铜板?
例如，给定数组{10,20,30}，代表一共三个人，整块金条长度为60，金条要分成10，20，30三个部分。
如果先把长度60的金条分成10和50，花费60；再把长度50的金条分成20和30，花费50；一共花费110铜板
但如果先把长度60的金条分成30和30，花费60；再把长度30金条分成10和20，花费30；一共花费90铜板
输入一个数组，返回分割的最小代价
"""
import random


def best_split(arr: list):
    arr.sort(reverse=True)
    s = sum(arr)
    res = 0
    while len(arr) > 1:
        cur = arr.pop(0)
        s -= cur
        cur += s
        res += cur
    return res


def generator_random_arr(arr_len: int):
    arr = []
    arr_len = random.randint(1, arr_len)
    for i in range(arr_len):
        arr.append(random.randint(1, 100))
    return arr


def main():
    arr = generator_random_arr(5)
    print(arr)
    arr = [10, 20, 30, 40]
    res = best_split(arr)
    print(res)


if __name__ == '__main__':
    main()
