"""
给定一个正数数组arr，
请把arr中所有的数分成两个集合，尽量让两个集合的累加和接近
返回最接近的情况下，较小集合的累加和
"""

import time
from typing import List


class Solution:
    def split_arr(self, arr: List[int]):
        arr_sum = sum(arr)
        return self.process(arr, 0, arr_sum >> 1)

    def process(self, arr: List[int], index: int, rest: int):
        """
        从arr的index到N中选择数使得和最接近rest但不能大于rest
        """
        N = len(arr)
        if index == N:
            return 0
        if rest == 0:
            return 0
        # 不使用当前数
        p1 = self.process(arr, index + 1, rest)
        # 使用当前数
        p2 = 0
        if rest >= arr[index]:
            p2 = arr[index] + self.process(arr, index + 1, rest - arr[index])
        return max(p1, p2)


class Solution2:
    def split_arr(self, arr: List[int]):
        """
        index: 0 -- N
        rest: 0 -- sum/2
        """
        arr_sum = sum(arr)
        target = arr_sum >> 1
        N = len(arr)
        dp = [[0] * (target + 1) for _ in range(N + 1)]
        for index in range(N - 1, -1, -1):
            for rest in range(target + 1):
                p1 = dp[index + 1][rest]
                p2 = 0
                if rest >= arr[index]:
                    p2 = arr[index] + dp[index + 1][rest - arr[index]]
                dp[index][rest] = max(p1, p2)
        return dp[0][target]


def main():
    arr = [2, 5, 6, 10]
    t1 = time.time()
    solution = Solution()
    res1 = solution.split_arr(arr)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.split_arr(arr)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
