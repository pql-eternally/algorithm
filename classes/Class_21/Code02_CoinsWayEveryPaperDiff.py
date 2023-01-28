"""
arr是货币数组，其中的值都是正数。再给定一个正数aim。
每个值都认为是一张货币，
即便是值相同的货币也认为每一张都是不同的，
返回组成aim的方法数
例如：arr = {1,1,1}，aim = 2
第0个和第1个能组成2，第1个和第2个能组成2，第0个和第2个能组成2
一共就3种方法，所以返回3

从左到右模型
"""
import time
from typing import List


class Solution:
    def get_ways(self, arr: List[int], aim: int):
        return self.process(arr, 0, aim)

    def process(self, arr: List[int], index: int, rest: int):
        N = len(arr)
        if rest < 0:
            return 0
        # 没有货币可以使用了
        if index == N:
            return 1 if rest == 0 else 0
        return self.process(arr, index + 1, rest) + self.process(arr, index + 1, rest - arr[index])


class Solution2:
    def get_ways(self, arr: List[int], aim: int):
        """
        dp 变量右2个
        index: 0 -> N
        aim: 0 -> aim
        row 为 cur index
        col 为 rest aim
        """
        row, col = len(arr) + 1, (aim + 1)
        dp = [[0] * col for _ in range(row)]
        dp[row - 1][0] = 1
        for index in range(len(arr) - 1, -1, -1):
            for rest in range(col):
                dp[index][rest] = dp[index + 1][rest]
                if rest >= arr[index]:
                    dp[index][rest] += dp[index + 1][rest - arr[index]]
        return dp[0][aim]


def main():
    arr = [1, 1, 1]
    aim = 2
    t1 = time.time()
    solution = Solution()
    res = solution.get_ways(arr, aim)
    t2 = time.time()
    print(t2 - t1, res)

    solution2 = Solution2()
    res2 = solution2.get_ways(arr, aim)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
