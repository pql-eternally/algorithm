"""
arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
每个值都认为是一种面值，且认为张数是无限的。
返回组成aim的最少货币数
"""
import time
from typing import List


class Solution:
    def min_coins(self, arr: List[int], aim: int):
        pass


class Solution2:
    def min_coins(self, arr: List[int], aim: int):
        pass


def main():
    arr = []
    aim = 1
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
