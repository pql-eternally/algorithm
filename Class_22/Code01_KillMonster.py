"""
给定3个参数，N，M，K
怪兽有N滴血，等着英雄来砍自己
英雄每一次打击，都会让怪兽流失[0~M]的血量
到底流失多少？每一次在[0~M]上等概率的获得一个值
求K次打击之后，英雄把怪兽砍死的概率
"""
import time
from typing import List


class Solution:
    def kill(self, N: int, M: int, K: int):
        pass


class Solution2:
    def kill(self, N: int, M: int, K: int):
        pass


def main():
    N = 5
    M = 5
    k = 5
    t1 = time.time()
    solution = Solution()
    res1 = solution.kill(N, M, k)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.kill(N, M, k)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
