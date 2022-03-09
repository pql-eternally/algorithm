"""
斐波那契数（通常用F(n) 表示）形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
"""
import time
import copy
import numpy as np

from typing import List


class Solution1:
    """
    暴力递归
    """

    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    """
    暴力递归加记忆化搜索
    """
    fibs = {
        1: 1,
        2: 1
    }

    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n in self.fibs:
            return self.fibs[n]
        res = self.fib(n - 1) + self.fib(n - 2)
        self.fibs[n] = res
        return res


class Solution3:
    """
    动态规划
    """

    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        dp = [1, 1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


class Solution4:
    """
    二阶矩阵
    """

    base_matrix = [[1, 1], [1, 0]]
    unit_matrix = [[1, 0], [0, 1]]

    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        p = n - 2
        res = copy.deepcopy(self.unit_matrix)
        t = copy.deepcopy(self.base_matrix)
        while p != 0:
            if p & 1 != 0:
                res = self.matrix_multiply(res, t)
            t = self.matrix_multiply(t, t)
            p >>= 1
        return res[0][0] + res[1][0]

    @staticmethod
    def matrix_multiply(m1: List[List[int]], m2: List[List[int]]):
        res = [[0] * len(m2[0]) for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res


class Solution5:
    """
    二阶矩阵
    """

    def fib(self, n: int) -> int:
        if n < 1:
            return 0
        # base case
        if n == 1 or n == 2:
            return 1
        # 矩阵相乘次数：n - 2
        p = n - 2
        # 单位矩阵：等价于 1
        res = [[1, 0], [0, 1]]
        # fib 基础二阶矩阵
        t = [[1, 1], [1, 0]]
        while p != 0:
            if p & 1 != 0:
                res = self.matrix_multiply(res, t)
            t = self.matrix_multiply(t, t)
            p >>= 1
        return int(res[0][0] + res[1][0])

    @staticmethod
    def matrix_multiply(m1: List[List[int]], m2: List[List[int]]):
        """
        使用numpy进行二阶矩阵相乘
        """
        return list(np.array(m1) * np.array(m2))


def test_matrix_multiply(m1: List[List[int]], m2: List[List[int]]):
    return list(np.array(m1) * np.array(m2))


def main():
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()
    s4 = Solution4()
    s5 = Solution4()

    n = 3
    t1 = time.time()
    res1 = s1.fib(n)
    t2 = time.time()
    res2 = s2.fib(n)
    t3 = time.time()
    res3 = s3.fib(n)
    t4 = time.time()
    res4 = s4.fib(n)
    t5 = time.time()
    res5 = s5.fib(n)
    t6 = time.time()

    print(res1, res2, res3, res4, res5)
    print(t2 - t1, t3 - t2, t4 - t3, t5 - t4, t6 - t5)


if __name__ == '__main__':
    main()
