"""
给定2D空间中四个点的坐标p1,p2,p3和p4，如果这四个点构成一个正方形，则返回 true 。

点的坐标pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

一个 有效的正方形 有四条等边和四个等角(90度角)。

链接：https://leetcode.cn/problems/valid-square
"""
from typing import List


class Solution:
    def calculateDistance(self, p1: List[int], p2: List[int]):
        x1, y1 = p1
        x2, y2 = p2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        d12 = self.calculateDistance(p1, p2)
        d34 = self.calculateDistance(p3, p4)
        if d12 != d34:
            return False
        d13 = self.calculateDistance(p1, p3)
        d24 = self.calculateDistance(p2, p4)
        if d13 != d24:
            return False
        d14 = self.calculateDistance(p1, p4)
        d23 = self.calculateDistance(p2, p3)
        if d14 != d23:
            return False
        # 如果出现0肯定不是
        if 0 in [d12, d13, d14]:
            return False
        # 判断相邻两边也必须相等
        if d12 != d13 and d12 != d14 and d13 != d14:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    # p1 = [0, 0]
    # p2 = [5, 0]
    # p3 = [5, 4]
    # p4 = [0, 4]

    # p1 = [0, 0]
    # p2 = [1, 1]
    # p3 = [1, 0]
    # p4 = [0, 1]

    p1 = [0, 0]
    p2 = [0, 0]
    p3 = [0, 0]
    p4 = [0, 0]
    res = s.validSquare(p1, p2, p3, p4)
    print(res)
