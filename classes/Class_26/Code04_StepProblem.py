"""
一个人可以一次往上迈1个台阶，也可以迈2个台阶，返回迈上N级台阶的方法数

1级台阶：1
2级台阶：2
3级台阶：3
4级台阶：5
5级台阶：8

n级台阶的方法数 = n-1级台阶的方法数 + n-2级台阶的方法数
f(n) = f(n - 1) + f(n - 2)
"""
import numpy as np

from typing import List


class Solution1:
    """
    暴力递归
    """

    def step(self, n: int) -> int:
        return self.process(n)

    def process(self, rest: int) -> int:
        """
        剩余rest步，返回上台阶的方法数
        """
        if rest < 0:
            return 0
        if rest == 0:
            return 1
        return self.process(rest - 1) + self.process(rest - 2)


class Solution2:
    """
    动态规划
    """

    def step(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


class Solution3:
    """
    二阶矩阵
    """

    def step(self, n: int) -> int:
        if n <= 2:
            return n
        t = [[1, 1], [1, 0]]
        res = [[1, 0], [0, 1]]
        p = n - 2
        while p != 0:
            if p & 1 != 0:
                res = self.matrix_multiply(res, t)
            t = self.matrix_multiply(t, t)
            p >>= 1
        return int(2 * res[0][0] + res[1][0])

    @staticmethod
    def matrix_multiply(m1: List[List[int]], m2: List[List[int]]):
        return np.dot(np.array(m1), np.array(m2))


def main():
    n = 5
    s1 = Solution1()
    res1 = s1.step(n)
    print(res1)

    s2 = Solution2()
    res2 = s2.step(n)
    print(res2)

    s3 = Solution3()
    res3 = s3.step(n)
    print(res3)


if __name__ == '__main__':
    main()
