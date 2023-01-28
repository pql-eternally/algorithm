"""
基数排序
"""
import copy
import random


def radix_sort(arr: list) -> None:
    """
    基数排序（桶排序）
    # 准备一个10个长度的列表
    # 统计每一位出现数字的个数
    # 产生前缀和辅助数组
    # 循环原数据，将数据按每位排序好后放入对应位置
    # 最终按个位、十位、百位的顺序排好序
    """
    max_value = max(arr)
    # 求出最大的数值的位数
    digit = len(str(max_value))
    # 帮助数组，和原数组长度一致
    help_arr = [None] * len(arr)
    for d in range(1, digit + 1):
        # 统计每一位出现数字的个数
        count = [0] * 10
        for num in arr:
            value = get_digit_value(num, d)
            count[value] += 1
        # 产生前缀和辅助数组
        for i in range(10):
            if i == 0:
                continue
            count[i] = count[i] + count[i - 1]
        # 计算每个数的位置
        for num in arr[::-1]:
            value = get_digit_value(num, d)
            help_arr[count[value] - 1] = num
            count[value] -= 1
        # 数组拷贝
        arr[::] = help_arr[::]


def get_digit_value(num: int, digit: int) -> int:
    """
    获取某个数字对应位上的数值
    """
    str_num = str(num)
    max_digit = len(str_num)
    if max_digit < digit:
        return 0
    return int(str_num[max_digit - digit])


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
        radix_sort(arr1)
        comparator(arr2)
        assert arr1 == arr2, f'arr: {arr}，res2：{arr1}，res2：{arr2}'
    print('Done ...')


if __name__ == '__main__':
    main()
