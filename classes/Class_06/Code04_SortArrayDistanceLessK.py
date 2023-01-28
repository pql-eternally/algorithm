"""
已知一个几乎有序的数组。几乎有序是指，如果把数组排好顺序的话，每个元素移动的距离一定不超过k
k相对于数组长度来说是比较小的。请选择一个合适的排序策略，对这个数组进行排序。
"""
import copy
import random
from queue import PriorityQueue


def sort_arr_distance_less_k(arr: list, k: int):
    heap = PriorityQueue()
    i = 0
    for index in range(0, len(arr)):
        heap.put(arr[index])
        if heap.qsize() > k:
            arr[i] = heap.get()
            i += 1
    while not heap.empty():
        arr[i] = heap.get()
        i += 1


def comparator(arr):
    arr.sort()


def random_array_move_less_k(max_size: int = 20, min_value: int = 0, max_value: int = 100, k: int = 5) -> list:
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    # 排序
    arr.sort()
    # 记录交换过的下标
    swaps = []
    for i in range(len(arr)):
        j = random.randint(i - k, i + k)
        if j < 0 or j > len(arr) - 1:
            continue
        if i not in swaps and j not in swaps:
            arr[i], arr[j] = arr[j], arr[i]
            swaps.extend([i, j])
    return arr


def main():
    print('Start ...')
    test_count = 10000
    k = 5
    for i in range(0, test_count):
        arr = random_array_move_less_k(10, k=k)
        arr1 = copy.copy(arr)
        arr2 = copy.copy(arr)
        sort_arr_distance_less_k(arr1, k)
        comparator(arr2)
        if arr1 != arr2:
            print(f'arr: {arr}，res1：{arr1}，res2：{arr2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
