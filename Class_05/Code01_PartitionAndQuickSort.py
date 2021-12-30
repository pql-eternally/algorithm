"""
快排
"""
import copy
import random


def quick_sort_v1(arr: list) -> None:
    """
    快排1.0版：以最后一个数为准，将所有小于等于这个数的放左侧，大于这个数的放右侧
    步骤：
    1、小于区域指针指向最左侧
    2、依次循环列表中数字
        1）当前数小于目标数，则将当前数和小于区域的指向的数交换，小于区域向右扩，跳下一个
        2）当前数等于目标数，则将当前数和小于区域的指向的数交换，小于区域向右扩，跳下一个
        2）当前数大于目标数，跳下一个
    3、将目标数和小于区域下一个数交换
    4、这样所有小于等于目标数都在左侧，大于目标数的在右侧
    缺点：每次只能够确定目标数一个数的位置
    """
    process_v1(arr, 0, len(arr) - 1)


def partition_v1(arr: list, left: int, right: int) -> int:
    if left > right:
        return -1
    if left == right:
        return left

    less_point = left - 1
    num = arr[right]
    for i in range(left, right):
        if arr[i] <= num:
            less_point += 1
            arr[i], arr[less_point] = arr[less_point], arr[i]
    # 将目标数移动到小于区域
    less_point += 1
    arr[less_point], arr[right] = arr[right], arr[less_point]
    return less_point


def process_v1(arr: list, left: int, right: int) -> None:
    if left >= right:
        return
    # 寻找分片
    m = partition_v1(arr, left, right)
    process_v1(arr, left, m - 1)
    process_v1(arr, m + 1, right)


def quick_sort_v2(arr: list) -> None:
    """
    快排2.0版：以最后一个数为准，将所有小于等于这个数的放左侧，等于当前数的让中间，大于这个数的放右侧
    步骤：
    1、小于区域指针指向最左侧，大于区域指针指向最后一个数前一个
    2、依次循环列表中数字
        1）当前数小于目标数，则将当前数和小于区域的指向的数交换，小于区域向右扩，跳下一个
        2）当前数等于目标数，直接跳下一个
        2）当前数大于目标数，则将当前数和大于区域的指向的数交换，大于区域先左扩（注意这里不能跳下一个因为当前数还未比较过）
    3、将目标数和大于区域第一个数交换
    4、这样所有小于目标数都在左侧，等于目标数的在中间，大于目标数的在右侧
    优点：每次能够确定一批等于目标数的位置
    缺点：一直使用最右侧的数作为目标数，在最坏情况时时间复杂度高
    """
    process_v2(arr, 0, len(arr) - 1)


def process_v2(arr: list, left: int, right: int) -> None:
    if left >= right:
        return
    p1, p2 = partition(arr, left, right)
    process_v2(arr, left, p1 - 1)
    process_v2(arr, p2 + 1, right)


def partition(arr: list, left: int, right: int) -> tuple:
    if left > right:
        return -1, -1
    if left == right:
        return left, right

    # 小于区域
    p1 = left - 1
    # 大于区域
    p2 = right
    target_num = arr[right]
    # 当前位置，不能和 > 区的左边界撞上
    index = left
    while index < p2:
        if arr[index] < target_num:
            p1 += 1
            arr[p1], arr[index] = arr[index], arr[p1]
            index += 1
        elif arr[index] == target_num:
            index += 1
        else:
            p2 -= 1
            arr[index], arr[p2] = arr[p2], arr[index]
    # 将目标数和大于区域第一个数交换
    arr[right], arr[p2] = arr[p2], arr[right]
    # 注意：这里p1是小于区域最后一个，等于区域为下一个
    return p1 + 1, p2


def quick_sort_v3(arr: list) -> None:
    """
    快排3.0版：随机选择一个数和最后一个数交换，以最后一个数为准，将所有小于等于这个数的放左侧，等于当前数的让中间，大于这个数的放右侧
    使用随机选择后可以将最坏的情况趋向于没有
    """
    process_v3(arr, 0, len(arr) - 1)


def process_v3(arr: list, left: int, right: int) -> None:
    if left >= right:
        return
    # 随机选择目标数
    r = random.randint(left, right)
    arr[r], arr[right] = arr[right], arr[r]
    # 确定等于区域位置
    p1, p2 = partition(arr, left, right)
    process_v3(arr, left, p1 - 1)
    process_v3(arr, p2 + 1, right)


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
        arr4 = copy.copy(arr)
        quick_sort_v1(arr1)
        quick_sort_v2(arr2)
        quick_sort_v2(arr3)
        comparator(arr4)
        if arr3 != arr4:
            print(f'arr: {arr}，res2：{arr2}，res3：{arr3}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
