"""
基于比较的排序：冒泡排序、插入排序、选择排序、归并排序、快排、堆排序、希尔排序
不基于比较的排序：计数排序，堆排序
"""
import copy
import random

MAX_VALUE = 100


def count_sort(arr):
    """
    计数排序，统计每个数出现的次数，根据计数还原回原来的数据
    """
    min_value = min(arr)
    max_value = max(arr)
    bucket = [0] * (max_value - min_value + 1)
    for i in arr:
        bucket[i - min_value] += 1

    i = 0
    for num, count in enumerate(bucket, min_value):
        if count == 0:
            continue
        arr[i: i + count] = [num] * count
        i += count


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = MAX_VALUE) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def comparator(arr: list) -> None:
    arr.sort()


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        count_sort(arr1)
        comparator(arr2)
        assert arr1 == arr2, f'arr: {arr}，res2：{arr1}，res2：{arr2}'
    print('Done ...')


if __name__ == '__main__':
    main()
