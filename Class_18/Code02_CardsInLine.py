"""
给定一个整型数组arr，代表数值不同的纸牌排成一条线
玩家A和玩家B依次拿走每张纸牌
规定玩家A先拿，玩家B后拿
但是每个玩家每次只能拿走最左或最右的纸牌
玩家A和玩家B都绝顶聪明
请返回最后获胜者的分数
"""
from typing import List


def win1(arr: List[int]):
    first = first_process1(arr, 0, len(arr) - 1)
    second = second_process1(arr, 0, len(arr) - 1)
    return max(first, second)


def first_process1(arr: List[int], left: int, right: int):
    """
    先手从范围为left ... right 排堆中拿到最大到分数
    """
    if left == right:
        return arr[left]
    # 拿左边
    p1 = arr[left] + second_process1(arr, left + 1, right)
    p2 = arr[right] + second_process1(arr, left, right - 1)
    return max(p1, p2)


def second_process1(arr: List[int], left: int, right: int):
    """
    当前玩家后手从剩余的排堆 left ... right 中拿到的最大的分数
    """
    if left == right:
        return 0
    # 对手拿了left位置的牌后当前玩家以先手能拿到的最大值
    p1 = first_process1(arr, left + 1, right)
    p2 = first_process1(arr, left, right - 1)
    # 注意这里取min，因为是对手做决定，对手一定会让你选择两种中最差的情况
    return min(p1, p2)


def win2(arr: List[int]):
    """
    增加缓存记忆
    """
    n = len(arr)
    res_cache = [[-1] * n for _ in range(n)]
    first = first_process2(arr, 0, n - 1, res_cache)
    second = second_process2(arr, 0, n - 1, res_cache)
    return max(first, second)


def first_process2(arr: List[int], left: int, right: int, res_cache: List[List[int]]):
    if res_cache[left][right] != -1:
        return res_cache[left][right]
    if left == right:
        res = arr[left]
    else:
        p1 = arr[left] + second_process2(arr, left + 1, right, res_cache)
        p2 = arr[right] + second_process2(arr, left, right - 1, res_cache)
        res = max(p1, p2)
    res_cache[left][right] = res
    return res


def second_process2(arr: List[int], left: int, right: int, res_cache: List[List[int]]):
    if res_cache[left][right] != -1:
        return res_cache[left][right]
    if left == right:
        res = 0
    else:
        p1 = first_process2(arr, left + 1, right, res_cache)
        p2 = first_process2(arr, left, right - 1, res_cache)
        res = min(p1, p2)
    return res


def win3(arr: List[int]):
    """
    动态规划
    """
    n = len(arr)
    # 先手dp
    first_dp = [[0] * n for _ in range(n)]
    # 后手dp
    second_dp = [[0] * n for _ in range(n)]
    for i in range(0, n):
        first_dp[i][i] = arr[i]
    for start_col in range(1, n):
        L = 0
        R = start_col
        while R < n:
            first_dp[L][R] = max(arr[L] + second_dp[L + 1][R], arr[R] + second_dp[L][R - 1])
            second_dp[L][R] = min(first_dp[L + 1][R], first_dp[L][R - 1])
            L += 1
            R += 1

    for f in first_dp:
        print(f)
    for s in second_dp:
        print(s)
    return max(first_dp[0][n - 1], second_dp[0][n - 1])


def main():
    arr = [20, 30, 40, 10, 50]
    res1 = win1(arr)
    res2 = win2(arr)
    res3 = win3(arr)
    print(res1)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
