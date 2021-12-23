"""
选择排序及其对数器验证
"""
import random
import copy


def selection_sort(arr: list) -> None:
    """
    0 ~ n-1  找到最小值，在哪，放到 0 位置上
    1 ~ n-1  找到最小值，在哪，放到 1 位置上
    2 ~ n-1  找到最小值，在哪，放到 2 位置上
    """
    if not arr:
        return

    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i == min_index:
            continue
        # 交换当前最小值到对应位置
        arr[i], arr[min_index] = arr[min_index], arr[i]


def comparator(arr: list) -> None:
    """
    比较器，通常使用简单的方式来实现相同的功能，用来验证排序算法是否正确
    """
    arr.sort()


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


def is_equal(arr1: list, arr2: list) -> bool:
    """
    判断两个列表是否相等
    """
    if len(arr1) != len(arr2):
        return False
    for i in range(0, len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def main():
    """
    编写对数器，大数据量测试
    """
    print('Start ...')
    test_count = 100000
    for i in range(0, test_count):
        arr = generate_random_arr()
        arr1 = copy.deepcopy(arr)
        arr2 = copy.deepcopy(arr)
        selection_sort(arr1)
        comparator(arr2)
        if is_equal(arr1, arr2) is False:
            print(f'排序出错了，原数组：{arr}，插入排序：{arr1}，比较器排序：{arr2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
