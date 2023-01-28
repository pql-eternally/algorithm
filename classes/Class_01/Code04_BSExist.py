"""
有序数组中找到num
"""
import random


def binary_search(arr: list, num: int) -> bool:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] == num:
            return True
        # 中间数小于目标数，向右搜索
        elif arr[mid] < num:
            left = mid + 1
        # 中间数大于目标数，向左搜索
        else:
            right = mid - 1
    return False


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


def main():
    print('Start ...')
    size = 20
    min_value = 0
    max_value = 100
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(size, min_value, max_value)
        arr.sort()
        num = random.randint(min_value, max_value)
        if binary_search(arr, num) != (num in arr):
            print(f'列表：{arr}，数字：{num}，结果：{binary_search(arr, num)} {num in arr}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
