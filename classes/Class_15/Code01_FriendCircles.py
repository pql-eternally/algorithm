"""
一群朋友中，有几个不相交的朋友圈
Leetcode题目：https://leetcode.com/problems/friend-circles/
"""
from typing import List


class Solution:
    """
    使用并查集解决
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        return union_find.sets


class UnionFind:
    """
    使用列表实现并查集
    """
    parents: List
    sizes: List
    # 一共有多少个集合
    sets: int

    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.sets = n

    def find(self, i: int):
        arr = []
        while i != self.parents[i]:
            arr.append(i)
            i = self.parents[i]
        while arr:
            self.parents[arr.pop()] = i
        return i

    def union(self, i: int, j: int):
        fi = self.find(i)
        fj = self.find(j)
        if fi != fj:
            si = self.sizes[i]
            sj = self.sizes[j]
            if si < sj:
                small, big = fi, fj
            else:
                small, big = fj, fi
            self.parents[small] = big
            self.sizes[big] = si + sj
            self.sizes[small] = 0
            self.sets -= 1


def main():
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    s = Solution()
    res = s.findCircleNum(isConnected)
    print(res)


if __name__ == '__main__':
    main()
