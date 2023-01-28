"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的方法数
例如：arr = {1,2}，aim = 4
方法如下：1+1+1+1、1+1+2、2+2
一共就3种方法，所以返回3
"""
import time
from typing import List


class Solution:
    def get_ways(self, arr: List[int], aim: int):
        return self.process(arr, 0, aim)

    def process(self, arr: List[int], index: int, rest: int):
        if index == len(arr):
            return 1 if rest == 0 else 0
        ways = 0
        count = 0
        money = arr[index]
        while money * count <= rest:
            ways += self.process(arr, index + 1, rest - money * count)
            count += 1
        return ways


class Solution2:
    def get_ways(self, arr: List[int], aim: int):
        row = len(arr) + 1
        col = aim + 1
        dp = [[0] * col for _ in range(row)]
        dp[len(arr)][0] = 1
        for index in range(len(arr) - 1, -1, -1):
            for rest in range(0, col):
                ways = 0
                count = 0
                money = arr[index]
                while money * count <= rest:
                    ways += dp[index + 1][rest - money * count]
                    count += 1
                dp[index][rest] = ways
        return dp[0][aim]


class Solution3:
    """
    找关联关系
    """

    def get_ways(self, arr: List[int], aim: int):
        row = len(arr) + 1
        col = aim + 1
        dp = [[0] * col for _ in range(row)]
        dp[len(arr)][0] = 1
        for index in range(len(arr) - 1, -1, -1):
            money = arr[index]
            for rest in range(0, col):
                dp[index][rest] = dp[index + 1][rest]
                if rest - money >= 0:
                    dp[index][rest] += dp[index][rest - money]
        return dp[0][aim]


def main():
    arr = [1, 2, 5, 10, 20, 50, 100]
    aim = 300
    t1 = time.time()
    solution = Solution()
    res = solution.get_ways(arr, aim)
    t2 = time.time()
    print(t2 - t1, res)

    solution2 = Solution2()
    res2 = solution2.get_ways(arr, aim)
    t3 = time.time()
    print(t3 - t2, res2)

    solution3 = Solution3()
    res3 = solution3.get_ways(arr, aim)
    t4 = time.time()
    print(t4 - t3, res3)


if __name__ == '__main__':
    main()
