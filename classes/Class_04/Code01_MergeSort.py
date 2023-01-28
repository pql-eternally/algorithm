"""
归并排序的递归和非递归实现
使用Master公式分析时间复杂度
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


def merge_sort(arr: list) -> None:
    """
    归并排序 -- 递归版
    使用Master公式计算时间复杂度
    T(N) = aT(N/b) + O(N^d)
    log(b, a) > d   ==>  O(N^log(b, a))
    log(b, a) < d   ==>  O(N^d)
    log(b, a) = d   ==>  O(N^d * logN)
    每次递归中，可以解决N/2个问题，并且需要两次，然后需要一次合并两个有序列表
    所以：T(N) = 2T(N/2) + O(N) ==> a=2 b=2 d=1
    log(b, a) = 1 = d  ==>  O(N^d * logN) ==> O(NlogN)
    """
    return process(arr, 0, len(arr) - 1)


def process(arr: list, left: int, right: int) -> None:
    if left == right:
        return
    mid = left + ((right - left) >> 1)
    process(arr, left, mid)
    process(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int) -> None:
    """
    数组：left -> mid有序、mid + 1 -> right有序
    合并这两个有序数组
    """
    help_arr = []
    p1 = left
    p2 = mid + 1
    while p1 <= mid and p2 <= right:
        if arr[p1] < arr[p2]:
            help_arr.append(arr[p1])
            p1 += 1
        else:
            help_arr.append(arr[p2])
            p2 += 1
    # 合并剩余的
    help_arr.extend(arr[p1: mid + 1])
    help_arr.extend(arr[p2: right + 1])
    # 替换排好序的部分
    arr[left: right + 1] = help_arr


def merge_sort_by_step(arr: list) -> None:
    """
    归并排序：非递归版，使用步长渐增：1 -> 2 -> 4 -> 8 ... > len(arr)
    """
    if not arr or len(arr) < 2:
        return

    step = 1
    size = len(arr)
    # 使用步长
    while step < size:
        left = 0
        while left < size:
            mid = left + step - 1
            right = mid + min(step, size - mid - 1)
            merge(arr, left, mid, right)
            left = right + 1
        # 防止溢出
        if step > (size >> 1):
            break
        step <<= 1


def comparator(arr: list) -> None:
    arr.sort()


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(100)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        arr3 = copy.copy(arr)
        merge_sort(arr1)
        comparator(arr2)
        merge_sort_by_step(arr3)
        if (arr1 != arr2) or (arr2 != arr3):
            print(f'arr: {arr}，res1：{arr1}，res2：{arr2}，res3：{arr3}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
