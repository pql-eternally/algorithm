"""
给定一个正数n，求n的裂开方法数，
规定：后面的数不能比前面的数小
比如4的裂开方法有：
1+1+1+1、1+1+2、1+3、2+2、4
5种，所以返回5
"""
import time


class Solution:
    def split_number(self, n: int):
        return self.process(1, n)

    def process(self, pre: int, rest: int):
        if rest == 0:
            return 1
        if pre > rest:
            return 0
        ways = 0
        for i in range(pre, rest + 1):
            ways += self.process(i, rest - i)
        return ways


class Solution2:
    def split_number(self, n: int):
        """
        dp
        pre: 1 - n
        rest: 0, n
        可以准备 n * n 的二维数组
        可以发现是斜对角方式进行填充或者是从底到上方式填充
        """
        N = n + 1
        dp = [[0] * N for _ in range(N)]
        # 填第0列
        for pre in range(N):
            dp[pre][0] = 1
        for pre in range(N, 0, -1):
            for rest in range(pre, N):
                ways = 0
                for i in range(pre, rest + 1):
                    ways += dp[i][rest - i]
                dp[pre][rest] = ways
        return dp[1][n]


class Solution3:
    def split_number(self, n: int):
        # TODO:
        pass


def main():
    n = 4
    t1 = time.time()
    solution = Solution()
    res1 = solution.split_number(n)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.split_number(n)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
