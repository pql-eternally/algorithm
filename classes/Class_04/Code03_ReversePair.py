"""
在一个数组中，任何一个前面的数a，和任何一个后面的数b，如果(a,b)是降序的，就称为降序对。给定一个数组arr，求数组的降序对总数量
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


def reverse_pair(arr: list) -> int:
    return process(arr, 0, len(arr) - 1)


def process(arr: list, left: int, right: int) -> int:
    if left == right:
        return 0
    mid = left + ((right - left) >> 1)
    return process(arr, left, mid) + process(arr, mid + 1, right) + merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    """
    合并两个有序列表
    """
    p1 = left
    p2 = mid + 1
    help_arr = []
    res = 0
    while p1 <= mid and p2 <= right:
        # 左侧数值小，拷贝左侧
        if arr[p1] <= arr[p2]:
            help_arr.append(arr[p1])
            p1 += 1
        # 右侧数值小，拷贝右侧，拷贝右侧时说明此处是一个逆序对，查看左侧有多少数字比当前数大
        else:
            help_arr.append(arr[p2])
            res += mid - p1 + 1
            p2 += 1
    help_arr.extend(arr[p1: mid + 1])
    help_arr.extend(arr[p2: right + 1])
    arr[left: right + 1] = help_arr
    return res


def comparator(arr: list):
    res = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                res += 1
    return res


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(10)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        res1 = reverse_pair(arr1)
        res2 = comparator(arr2)
        print(f'arr: {arr}，res1：{res1}，res2：{res2}')
        if res1 != res2:
            print(f'arr: {arr}，res1：{res1}，res2：{res2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
