"""
插入排序及其对数器验证
"""
import random
import copy


def insertion_sort(arr: list) -> None:
    """
    当前数依次和前一个数比较，如果当前数小则交换位置，依次比较直到左侧没数字或者当前数不必左侧数小则停止
    """
    if not arr or len(arr) < 2:
        return
    for i in range(1, len(arr)):
        # 从当前位置依次向左侧比较
        for j in range(i, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]


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
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr()
        arr1 = copy.deepcopy(arr)
        arr2 = copy.deepcopy(arr)
        insertion_sort(arr1)
        comparator(arr2)
        if is_equal(arr1, arr2) is False:
            print(f'排序出错了，原数组：{arr}，冒泡排序：{arr1}，比较器排序：{arr2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
