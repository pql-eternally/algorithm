"""
规定1和A对应、2和B对应、3和C对应...26和Z对应
那么一个数字字符串比如"111”就可以转化为:
"AAA"、"KA"和"AK"
给定一个只有数字字符组成的字符串str，返回有多少种转化结果

从左做到右模型
"""

from typing import List


def convert_to_str(num_str: str):
    arr = list(num_str)
    return process(arr, 0)


def process(arr: List[str], index: int):
    N = len(arr)
    if index == N:
        return 1
    if arr[index] == '0':
        return 0
    # 当前位置独立作为一个字符串
    ways = process(arr, index + 1)
    # 当前位置和下一个字符串合起来为一个字符
    if index + 1 < N and int(arr[index]) * 10 + int(arr[index + 1]) < 27:
        ways += process(arr, index + 2)
    return ways


def convert_to_str1(num_str: str):
    arr = list(num_str)
    dp = [-1] * (len(arr) + 1)
    return process1(arr, 0, dp)


def process1(arr: List[str], index: int, dp: List[int]):
    if dp[index] != -1:
        return dp[index]
    N = len(arr)
    if index == N:
        ways = 1
    elif arr[index] == '0':
        ways = 0
    else:
        ways = process(arr, index + 1)
        if index + 1 < N and int(arr[index]) * 10 + int(arr[index + 1]) < 27:
            ways += process(arr, index + 2)
    dp[index] = ways
    return ways


def convert_to_str2(num_str: str):
    arr = list(num_str)
    N = len(arr)
    dp = [0] * (N + 1)
    dp[N] = 1
    # 从下标 N-1 填到 0
    for index in range(N - 1, -1, -1):
        ways = dp[index + 1]
        if index + 1 < N and int(arr[index]) * 10 + int(arr[index + 1]) < 27:
            ways += dp[index + 2]
        dp[index] = ways
    return dp[0]


def main():
    s = '1111'
    res = convert_to_str(s)
    res1 = convert_to_str1(s)
    res2 = convert_to_str2(s)
    print(res)
    print(res1)
    print(res2)
    assert res == res1 == res2


if __name__ == '__main__':
    main()
