"""
给定3个参数，N，M，K
怪兽有N滴血，等着英雄来砍自己
英雄每一次打击，都会让怪兽流失[0~M]的血量
到底流失多少？每一次在[0~M]上等概率的获得一个值
求K次打击之后，英雄把怪兽砍死的概率
"""
import time


class Solution:
    """
    暴力递归
    """

    def kill(self, N: int, M: int, K: int):
        total = pow(M + 1, K)
        live_count = self.process(N, M, K)
        return 1 - live_count / total

    def process(self, N: int, M: int, rest: int):
        if N <= 0:
            return 0
        if rest == 0:
            return 1
        count = 0
        for i in range(min(M + 1, N)):
            count += self.process(N - i, M, rest - 1)
        return count


class Solution2:
    """
    严格表结构依赖的dp
    """

    def kill(self, N: int, M: int, K: int):
        row = N + 1
        col = K + 1
        dp = [[0] * col for _ in range(row)]
        for x in range(row):
            dp[x][0] = 1
        for y in range(1, col):
            for x in range(row):
                count = 0
                for i in range(min(M + 1, x)):
                    count += dp[x - i][y - 1]
                dp[x][y] = count
        total = pow(M + 1, K)
        live_count = dp[N][K]
        return 1 - live_count / total


class Solution3:
    def kill(self, N: int, M: int, K: int):
        # TODO:
        pass


def main():
    N = 3
    M = 2
    k = 2
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
