"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的最少货币数
"""
import sys
import time
from typing import List


class Solution:
    def min_coins(self, arr: List[int], aim: int):
        return self.process(arr, 0, aim)

    def process(self, arr: List[int], index: int, rest: int):
        min_count = sys.maxsize
        N = len(arr)
        if index == N:
            return 0 if rest == 0 else min_count

        count = 0
        money = arr[index]
        while count * money <= rest:
            cur_count = count + self.process(arr, index + 1, rest - count * money)
            min_count = min(min_count, cur_count)
            count += 1
        return min_count


class Solution2:
    def min_coins(self, arr: List[int], aim: int):
        # 0 ... N
        N = len(arr)
        row = N + 1
        # 0 ... aim
        col = aim + 1
        dp = [[0] * col for _ in range(row)]
        dp[N][0] = 0
        for j in range(1, col):
            dp[N][j] = sys.maxsize
        for index in range(N - 1, -1, -1):
            for rest in range(col):
                min_count = sys.maxsize
                count = 0
                money = arr[index]
                while count * money <= rest:
                    cur_count = count + dp[index + 1][rest - count * money]
                    min_count = min(min_count, cur_count)
                    count += 1
                dp[index][rest] = min_count
        return dp[0][aim]


def main():
    arr = [1, 2, 5, 10]
    aim = 223
    t1 = time.time()
    solution = Solution()
    res1 = solution.min_coins(arr, aim)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.min_coins(arr, aim)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
