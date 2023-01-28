"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
"""
import copy
from typing import List, Dict


class Solution:
    """
    感染法
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] == '1':
                    self.infect(grid, i, j)
                    res += 1
        return res

    def infect(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = '2'
            # 上下左右进行感染
            self.infect(grid, i - 1, j)
            self.infect(grid, i + 1, j)
            self.infect(grid, i, j - 1)
            self.infect(grid, i, j + 1)


class Solution2:
    """
    使用并查集解决
    """

    class UnionFound:
        points: List
        parents: Dict
        sizes: Dict
        # 一共有多少个集合
        sets: int

        def __init__(self, grid: List[List[str]]):
            self.parents = {}
            self.sizes = {}
            # 注意这里小心列表初始化的浅拷贝
            self.points = [[None] * len(grid[0]) for _ in range(len(grid))]
            self.sets = 0
            for x, row in enumerate(grid):
                for y, cell in enumerate(row):
                    if cell == '1':
                        point = object()
                        self.points[x][y] = point
                        self.parents[point] = point
                        self.sizes[point] = 1
                        self.sets += 1

        def find(self, x: int, y: int):
            arr = []
            point = self.points[x][y]
            while point != self.parents[point]:
                arr.append(point)
                point = self.parents[point]
            while arr:
                self.parents[arr.pop()] = point
            return point

        def union(self, x1: int, y1: int, x2: int, y2: int):
            point1 = self.find(x1, y1)
            point2 = self.find(x2, y2)
            if point1 != point2:
                s1 = self.sizes[point1]
                s2 = self.sizes[point2]
                if s1 < s2:
                    small, big = point1, point2
                else:
                    small, big = point2, point1
                self.parents[small] = big
                self.sizes[big] = s1 + s2
                self.sizes.pop(small)
                self.sets -= 1

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        union_find = self.UnionFound(grid)
        # 处理第一行
        for y in range(1, col):
            if grid[0][y] == '1' and grid[0][y - 1] == '1':
                union_find.union(0, y, 0, y - 1)
        # 处理第一列
        for x in range(1, row):
            if grid[x][0] == '1' and grid[x - 1][0] == '1':
                union_find.union(x, 0, x - 1, 0)
        # 处理既有上也有左的部分
        for x in range(1, row):
            for y in range(1, col):
                if grid[x][y] == '1':
                    # 上面
                    if grid[x][y - 1] == '1':
                        union_find.union(x, y, x, y - 1)
                    # 左面
                    if grid[x - 1][y] == '1':
                        union_find.union(x, y, x - 1, y)
        return union_find.sets


def main():
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    s1 = Solution()
    res1 = s1.numIslands(copy.deepcopy(grid))

    s2 = Solution2()
    res2 = s2.numIslands(grid)
    print(res1, res2)
    assert res1 == res2


if __name__ == '__main__':
    main()
