"""
在一个数组中，对于任何一个数num，求有多少个(后面的数*2)依然<num，返回总个数

比如：[3,1,7,0,2]
3的后面有：1，0
1的后面有：0
7的后面有：0，2
0的后面没有
2的后面没有
所以总共有5个
"""

import copy
import random


def bigger_twice(arr: list) -> int:
    return process(arr, 0, len(arr) - 1)


def process(arr: list, left: int, right: int) -> int:
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    return process(arr, left, mid) + process(arr, mid + 1, right) + merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int) -> int:
    res = 0
    # 统计当前merge操作中左侧数字是右侧数字两倍的个数
    window_r = mid + 1
    for i in range(left, mid + 1):
        while window_r <= right and arr[i] > (arr[window_r] << 1):
            window_r += 1
        res += window_r - mid - 1

    p1 = left
    p2 = mid + 1
    help_arr = []
    while p1 <= mid and p2 <= right:
        if arr[p1] <= arr[p2]:
            help_arr.append(arr[p1])
            p1 += 1
        else:
            help_arr.append(arr[p2])
            p2 += 1
    help_arr.extend(arr[p1: mid + 1])
    help_arr.extend(arr[p2: right + 1])
    arr[left: right + 1] = help_arr
    return res


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = 100) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def comparator(arr: list):
    res = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] << 1) < arr[i]:
                res += 1
    return res


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        res1 = bigger_twice(arr1)
        res2 = comparator(arr2)
        if res1 != res2:
            print(f'arr: {arr}，res1：{res1}，res2：{res2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
