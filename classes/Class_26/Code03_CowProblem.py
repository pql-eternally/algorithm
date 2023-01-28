"""
奶牛生小牛问题
第一年农场有1只成熟的母牛A，往后的每年：
1）每一只成熟的母牛都会生一只母牛
2）每一只新出生的母牛都在出生的第三年成熟
3）每一只母牛永远不会死
返回N年后牛的数量

每年母牛的数量：

第一年： A
第二年： A
第三年： A   A1
第四年： A   A1   A2
第五年： A   A1   A2   A3   A11
第六年： A   A1   A2   A3   A4    A11   A12   A21

1   1   2   3   5   8
分析：发现每年的牛的数量 = 上一年的牛的数量 + 两年前牛的数量（在当年都会生一只母牛）
f(n) = f(n - 1) + f(n - 2)

求二阶矩阵
|f(n), f(n-1)| = |f(n-1), f(n-2)| * |二阶矩阵|
x = ｜a b｜
    ｜c d｜
带入例子求得
x = ｜1 1｜
    ｜1 0｜
"""
import numpy as np

from typing import List


class Solution1:
    """
    暴力递归
    """

    def cow(self, n: int) -> int:
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.cow(n - 1) + self.cow(n - 2)


class Solution2:
    """
    动态规划
    """

    def cow(self, n: int) -> int:
        if n < 1:
            return 0
        dp = [1, 1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]


class Solution3:
    """
    矩阵运算
    """

    def cow(self, n: int) -> int:
        if n < 1:
            return 0

        p = n - 2
        t = [[1, 1], [1, 0]]
        res = [[1, 0], [0, 1]]
        while p != 0:
            if p & 1 != 0:
                res = self.matrix_multiply(res, t)
            t = self.matrix_multiply(t, t)
            p >>= 1
        return int(res[0][0] + res[1][0])

    @staticmethod
    def matrix_multiply(m1: List[List[int]], m2: List[List[int]]):
        return np.dot(np.array(m1), np.array(m2))


def main():
    s1 = Solution1()
    s2 = Solution2()
    s3 = Solution3()

    n = 10
    res1 = s1.cow(n)
    res2 = s2.cow(n)
    res3 = s3.cow(n)
    print(res1)
    print(res2)
    print(res3)


if __name__ == '__main__':
    main()
