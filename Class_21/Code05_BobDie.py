"""
给定5个参数，N，M，row，col，k
表示在N*M的区域上，醉汉Bob初始在(row,col)位置
Bob一共要迈出k步，且每步都会等概率向上下左右四个方向走一个单位
任何时候Bob只要离开N*M的区域，就直接死亡
返回k步之后，Bob还在N*M的区域的概率
"""
import time
from typing import List


class Solution:
    def bob_die(self, N: int, M: int, row: int, col: int, k: int):
        count = self.process(N, M, row, col, k)
        total = pow(4, k)
        return count / total

    def process(self, N: int, M: int, x: int, y: int, rest: int):
        # N * M，x 到不了N， y到不了M
        if x < 0 or x == N or y < 0 or y == M:
            return 0
        if rest == 0:
            return 1
        ways = 0
        ways += self.process(N, M, x, y + 1, rest - 1)
        ways += self.process(N, M, x, y - 1, rest - 1)
        ways += self.process(N, M, x - 1, y, rest - 1)
        ways += self.process(N, M, x + 1, y, rest - 1)
        return ways


class Solution2:
    def bob_die(self, N: int, M: int, row: int, col: int, k: int):
        total = pow(4, k)
        # x ==> 0 -- N
        # y ==> 0 -- M
        # z ==> 0 -- k
        X = N
        Y = M
        Z = k + 1
        dp = [[[0] * Z for _ in range(Y)] for _ in range(X)]
        # 第0层
        for x in range(X):
            for y in range(Y):
                dp[x][y][0] = 1

        for z in range(1, Z):
            for x in range(X):
                for y in range(Y):
                    dp[x][y][z] = self.pick(dp, N, M, x, y + 1, z - 1) + self.pick(dp, N, M, x, y - 1, z - 1) + \
                                  self.pick(dp, N, M, x - 1, y, z - 1) + self.pick(dp, N, M, x + 1, y, z - 1)
        return dp[row][col][k] / total

    def pick(self, dp: List[List[List[int]]], N: int, M: int, x: int, y: int, z: int):
        if x < 0 or x == N or y < 0 or y == M:
            return 0
        return dp[x][y][z]


def main():
    N = 5
    M = 5
    row = 2
    col = 2
    k = 5
    t1 = time.time()
    solution = Solution()
    res1 = solution.bob_die(N, M, row, col, k)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.bob_die(N, M, row, col, k)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
