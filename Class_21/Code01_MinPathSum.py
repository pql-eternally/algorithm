"""
给定一个二维数组matrix，一个人必须从左上角出发，最后到达右下角
沿途只可以向下或者向右走，沿途的数字都累加就是距离累加和
返回最小距离累加和
"""
import time
from typing import List


class Solution:
    def min_path(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        return self.process(matrix, row, col, row - 1, col - 1)

    def process(self, matrix: List[List[int]], row: int, col: int, x: int, y: int):
        """
        返回 0,0 位置出发到 x,y 位置最短路径
        @param matrix: 二维数组matrix
        @param row: 二维数组行数
        @param col: 二维数组列数
        @param x: 目标点x轴
        @param y: 目标点y轴
        @return:
        """
        if x == 0 and y == 0:
            return matrix[0][0]
        elif x == 0:
            return matrix[0][y] + self.process(matrix, row, col, 0, y - 1)
        elif y == 0:
            return matrix[x][0] + self.process(matrix, row, col, x - 1, 0)
        else:
            p1 = self.process(matrix, row, col, x, y - 1)
            p2 = self.process(matrix, row, col, x - 1, y)
            return matrix[x][y] + min(p1, p2)


class Solution2:
    def min_path(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        dp[0][0] = matrix[0][0]
        # 第0行
        for y in range(1, col):
            dp[0][y] = matrix[0][y] + dp[0][y - 1]
        # 第0列
        for x in range(1, row):
            dp[x][0] = matrix[x][0] + dp[x - 1][0]
        # 填中间部分
        for x in range(1, row):
            for y in range(1, col):
                dp[x][y] = matrix[x][y] + min(dp[x][y - 1], dp[x - 1][y])
        return dp[row - 1][col - 1]


def main():
    matrix = [[2, 4, 1], [3, 5, 2], [6, 3, 1], [2, 4, 0]]
    t1 = time.time()
    solution = Solution()
    res = solution.min_path(matrix)
    t2 = time.time()
    print(t2 - t1, res)

    solution2 = Solution2()
    res2 = solution2.min_path(matrix)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
