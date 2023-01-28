"""
动态规划中利用窗口内最大值或最小值更新结构做优化（难）
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
返回组成aim的最少货币数
注意：因为是求最少货币数，所以每一张货币认为是相同或者不同就不重要了
"""
import sys
from typing import List


def min_coins(arr: List[int], aim: int) -> int:
    res = process1(arr, 0, aim)
    if res == sys.maxsize:
        return -1
    return res


def process1(arr: List[int], index: int, rest: int) -> int:
    if rest < 0:
        return sys.maxsize
    if index == len(arr):
        return 0 if rest == 0 else sys.maxsize
    p1 = process1(arr, index + 1, rest)
    p2 = process1(arr, index + 1, rest - arr[index])
    if p2 != sys.maxsize:
        p2 += 1
    return min(p1, p2)


def dp1(arr: List[int], aim: int) -> int:
    # index: 0 -> N
    N = len(arr)
    row = N + 1
    # rest: 0 -> aim
    col = aim + 1
    dp = [[sys.maxsize] * col for _ in range(row)]
    # dp[N][0] = 0
    dp[N][0] = 0
    # 填充dp从index：N -> 0
    for index in range(N - 1, -1, -1):
        cur_money = arr[index]
        for rest in range(col):
            p1 = dp[index + 1][rest]
            p2 = sys.maxsize
            if cur_money <= rest:
                p2 = dp[index + 1][rest - cur_money]
                if p2 != sys.maxsize:
                    p2 += 1
            dp[index][rest] = min(p1, p2)
    return dp[0][aim]


def min_coins2(arr: List[int], aim: int) -> int:
    # arr 统计货币种数和张数 ===> coins, counts
    coin_map = {}
    for money in arr:
        coin_map[money] = coin_map.get(money, 0) + 1
    coins = list(coin_map.keys())
    counts = list(coin_map.values())
    res = process2(coins, counts, 0, aim)
    if res == sys.maxsize:
        return -1
    return res


def process2(coins: List[int], counts: List[int], index: int, rest: int) -> int:
    N = len(coins)
    if index == N:
        return 0 if rest == 0 else sys.maxsize

    p = sys.maxsize
    money = coins[index]
    count = counts[index]
    i = 0
    while i <= count and money * i <= rest:
        p2 = process2(coins, counts, index + 1, rest - money * count)
        if p2 != sys.maxsize:
            p2 += 1
        p = min(p, p2)
        i += 1
    return p


def dp2(arr: List[int], aim: int) -> int:
    coin_map = {}
    for money in arr:
        coin_map[money] = coin_map.get(money, 0) + 1
    coins = list(coin_map.keys())
    counts = list(coin_map.values())
    N = len(coins)
    # 0 - > N
    row = N + 1
    # 0 - aim
    col = aim + 1
    dp = [[sys.maxsize] * col for _ in range(row)]
    dp[N][0] = 0
    for index in reversed(range(N)):
        money = coins[index]
        count = counts[index]
        for rest in range(col):
            p = sys.maxsize
            i = 0
            while i <= count and money * i <= rest:
                p2 = dp[index + 1][rest - money * count]
                if p2 != sys.maxsize:
                    p2 += 1
                p = min(p, p2)
                i += 1
            dp[index][rest] = p
    return dp[0][aim]


def main():
    arr = [1, 2, 5, 10, 20, 50]
    arr = [1, 2]
    aim = 3
    res = min_coins(arr, aim)
    res1 = dp1(arr, aim)
    print(res)
    print(res1)

    res2 = min_coins2(arr, aim)
    res3 = dp2(arr, aim)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
