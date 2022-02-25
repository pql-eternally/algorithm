"""
给定一个只包含正数的数组arr，arr中任何一个子数组sub，
一定都可以算出(sub累加和 )* (sub中的最小值)是什么，
那么所有子数组中，这个值最大是多少？

思路：
使用单调栈求出每个位置数左侧最小和右侧最小的数，然后取出最小的数 * sum（中间的数）
"""
import random
from typing import List

from Code01_MonotonousStack import get_near_less_with_repeat, Stack


def max_sub_arr1(arr: List[int]) -> int:
    """
    暴力法
    """
    return process1(arr, 0, len(arr) - 1)


def process1(arr: List[int], i: int, j: int) -> int:
    if i > j:
        return 0
    if i == j:
        return arr[i] * arr[i]
    # 包含i，j
    sub_arr1 = arr[i: j + 1]
    p1 = sum(sub_arr1) * min(sub_arr1)
    # 包含i，不包含j
    p2 = process1(arr, i, j - 1)
    # 不包含i，包含j
    p3 = process1(arr, i + 1, j)
    # 不包含i，不包含j
    p4 = process1(arr, i + 1, j - 1)
    return max(p1, p2, p3, p4)


def max_sub_arr2(arr: List[int]) -> int:
    """
    动态规划
    """
    N = len(arr)
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = arr[i] * arr[i]
    for i in reversed(range(N - 1)):
        for j in range(i + 1, N):
            sub_arr1 = arr[i: j + 1]
            p1 = sum(sub_arr1) * min(sub_arr1)
            # 包含i，不包含j
            p2 = dp[i][j - 1]
            # 不包含i，包含j
            p3 = dp[i + 1][j]
            # 不包含i，不包含j
            p4 = dp[i + 1][j - 1]
            dp[i][j] = max(p1, p2, p3, p4)
    return dp[0][N - 1]


def max_sub_arr3(arr: List[int]) -> int:
    """
    使用单调栈
    """
    less_indexes = get_near_less_with_repeat(arr)
    L = len(arr)
    res = 0
    for index, num in enumerate(arr):
        left_index, right_index = less_indexes[index]
        # 已当前数作为最小数时求结果
        if right_index == -1:
            right_index = L
        sub_arr = arr[left_index + 1: right_index]
        cur_res = sum(sub_arr) * min(sub_arr)
        res = max(res, cur_res)
    return res


def max_sub_arr4(arr: List[int]) -> int:
    """
    直接使用单调栈进行计算
    """
    res = 0
    L = len(arr)
    # 前缀和数组
    sums = [arr[0]]
    for index in range(1, L):
        sums.append(sums[-1] + arr[index])
    stack = Stack[int]()
    for index, num in enumerate(arr):
        # 相等时直接pop，此时计算以当前数为最小值结果是错误的，但是最终以当前数为最小值计算的结果是正确的
        while not stack.is_empty() and num <= arr[stack.peek()]:
            j = stack.pop()
            s = sums[index - 1] - sums[stack.peek()] if not stack.is_empty() else sums[index - 1]
            res = max(res, s * arr[j])
        stack.push(index)
    while not stack.is_empty():
        j = stack.pop()
        s = sums[L - 1] - sums[stack.peek()] if not stack.is_empty() else sums[L - 1]
        res = max(res, s * arr[j])
    return res


def generate_random_arr(max_size: int = 5, min_value: int = 0, max_value: int = 10) -> list:
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
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(10)
        res1 = max_sub_arr1(arr)
        res2 = max_sub_arr2(arr)
        res3 = max_sub_arr3(arr)
        res4 = max_sub_arr4(arr)
        assert res1 == res2 == res3 == res4, (arr, res1, res2, res3, res4)
    print('Done ...')


if __name__ == '__main__':
    main()
