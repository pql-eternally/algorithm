"""
在一个数组中，一个数左边比它小的数的总和，叫该数的小和

所有数的小和累加起来，叫数组小和
例子： [1,3,4,2,5]
1左边比1小的数：没有
3左边比3小的数：1
4左边比4小的数：1、3
2左边比2小的数：1
5左边比5小的数：1、3、4、2
所以数组的小和为1+1+3+1+1+3+4+2=16
给定一个数组arr，求数组小和
"""
import copy
import random


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


def small_sum(arr: list) -> int:
    """
    求数组小和的问题，可以转化为求当前数后面有多少个数比本身大
    """
    return process(arr, 0, len(arr) - 1)


def process(arr: list, left: int, right: int) -> int:
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    left_sum = process(arr, left, mid)
    right_sum = process(arr, mid + 1, right)
    merge_sum = merge(arr, left, mid, right)
    return left_sum + right_sum + merge_sum


def merge(arr: list, left: int, mid: int, right: int):
    """
    合并两个有序列表
    """
    p1 = left
    p2 = mid + 1
    help_arr = []
    res = 0
    while p1 <= mid and p2 <= right:
        # 左侧数值小，拷贝左侧，拷贝左侧时需要计算右侧有多少个数比当前数大
        if arr[p1] < arr[p2]:
            help_arr.append(arr[p1])
            res += arr[p1] * (right - p2 + 1)
            p1 += 1
        # 右侧数值小，拷贝右侧
        else:
            help_arr.append(arr[p2])
            p2 += 1
    help_arr.extend(arr[p1: mid + 1])
    help_arr.extend(arr[p2: right + 1])
    arr[left: right + 1] = help_arr
    return res


def comparator(arr: list):
    res = 0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                res += arr[j]
    return res


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        res1 = small_sum(arr1)
        res2 = comparator(arr2)
        if res1 != res2:
            print(f'arr: {arr}，res1：{res1}，res2：{res2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
