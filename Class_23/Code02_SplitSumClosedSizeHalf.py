"""
给定一个正数数组arr，请把arr中所有的数分成两个集合
如果arr长度为偶数，两个集合包含数的个数要一样多
如果arr长度为奇数，两个集合包含数的个数必须只差一个
请尽量让两个集合的累加和接近
返回最接近的情况下，较小集合的累加和
"""
import time
from typing import List


class Solution:
    def split_arr(self, arr: List[int]):
        arr_sum = sum(arr)
        target = arr_sum >> 1
        N = len(arr)
        # 偶数
        if N & 1 == 0:
            num = N >> 1
            return self.process(arr, num, 0, target)
        else:
            num1 = N >> 1
            num2 = num1 + 1
            p1 = self.process(arr, num1, 0, target)
            p2 = self.process(arr, num2, 0, target)
            return max(p1, p2)

    def process(self, arr: List[int], num: int, index: int, rest: int):
        """
        从arr中选择 从index到N的数只能选num个，求最接近与rest的值
        """
        N = len(arr)
        if num == 0:
            return 0
        if index == N:
            return -1
        # 未选择当前数
        p1 = self.process(arr, num, index + 1, rest)
        # 选择当前数
        p2 = 0
        if rest >= arr[index]:
            res = self.process(arr, num - 1, index + 1, rest - arr[index])
            if res != -1:
                p2 = arr[index] + res
        return max(p1, p2)


class Solution2:
    def split_arr(self, arr: List[int]):
        """
        3维表
        num: 0 - N/2
        index: 0 - N
        rest: 0 - sum/2
        """
        arr_sum = sum(arr)
        target = arr_sum >> 1
        N = len(arr)
        picks = (N + 1) >> 1
        dp = [[[-1] * (target + 1) for _ in range(N + 1)] for _ in range(picks + 1)]
        for index in range(N + 1):
            for rest in range(target + 1):
                dp[0][index][rest] = 0

        for index in range(N - 1, -1, -1):
            for num in range(picks + 1):
                for rest in range(target + 1):
                    p1 = dp[num][index + 1][rest]
                    p2 = 0
                    if rest >= arr[index]:
                        res = dp[num - 1][index + 1][rest - arr[index]]
                        if res != -1:
                            p2 = arr[index] + res
                    dp[num][index][rest] = max(p1, p2)
        # 偶数
        if N & 1 == 0:
            num = N >> 1
            return dp[num][0][target]
        else:
            num1 = N >> 1
            num2 = num1 + 1
            return max(dp[num1][0][target], dp[num2][0][target])


def main():
    arr = [2, 13, 5, 10, 8, 4]
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
