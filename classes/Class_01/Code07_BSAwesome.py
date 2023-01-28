"""
局部最小值问题
定义何为局部最小值：
1. arr[0] < arr[1]，0位置是局部最小；
2. arr[N-1] < arr[N-2]，N-1位置是局部最小；
3. arr[i-1] > arr[i] < arr[i+1]，i位置是局部最小；
给定一个数组arr，已知任何两个相邻的数都不相等，找到随便一个局部最小位置返回
"""
import random


def local_min_index(nums: list) -> int:
    """
    局部最小值问题：任意两个相邻位置数不等，返回一个存在的局部最小就行
    """
    if not nums:
        return -1
    length = len(nums)
    # 只有一个数
    if length == 1:
        return 0
    # 查看开头
    left, right = nums[0], nums[1]
    if left < right:
        return 0
    # 查看结尾
    left, right = nums[length - 2], nums[length - 1]
    if right < left:
        return length - 1
    # 不是两边的话，开头是递减函数，结尾是递增函数，根据连续性可以知道中间某个位置一定存在拐点（局部最小）
    left = 0
    right = length - 1
    # 注意：要保证mid、mid-1、mid+1落在l和r之间，所以至少要保证有3个数以上
    while left < right - 1:
        mid = int((left + right) / 2)
        num = nums[mid]
        left_num = nums[mid - 1]
        right_num = nums[mid + 1]
        # 看当前位置是否局部最小
        if (num < left_num) & (num < right_num):
            return mid
        # 当前大于左侧，递增趋势，说明mid左侧一定存在局部最小
        if num > left_num:
            right = mid
        # 当前大于右侧，递减趋势，说明mid右侧一定存在局部最小
        elif num > right_num:
            left = mid


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = 100) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    while len(arr) <= size:
        num = random.randint(min_value, max_value)
        if arr and num == arr[-1]:
            continue
        arr.append(num)
    return arr


def verify_res(arr: list, index: int) -> bool:
    """
    校验结果
    """
    if index == 0:
        return arr[0] < arr[1]
    if index == (len(arr) - 1):
        return arr[index] < arr[index - 1]
    return arr[index - 1] > arr[index] < arr[index + 1]


def main():
    print('Start ...')
    size = 20
    min_value = 0
    max_value = 100
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(size, min_value, max_value)
        res = local_min_index(arr)
        if verify_res(arr, res) is False:
            print(f'列表：{arr}，结果：{res}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
