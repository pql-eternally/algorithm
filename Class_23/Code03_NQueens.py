"""
N皇后问题是指在N*N的棋盘上要摆N个皇后，
要求任何两个皇后不同行、不同列， 也不在同一条斜线上
给定一个整数n，返回n皇后的摆法有多少种。n=1，返回1
n=2或3，2皇后和3皇后问题无论怎么摆都不行，返回0
n=8，返回92
"""
import time
from typing import List


class Solution:
    def num(self, N: int):
        pass


def main():
    n = 4
    t1 = time.time()
    solution = Solution()
    res1 = solution.num(n)
    t2 = time.time()
    print(t2 - t1, res1)


if __name__ == '__main__':
    main()
