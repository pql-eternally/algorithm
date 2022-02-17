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
    def queen(self, N: int):
        # 记录每行存放的皇后位置
        record = [0] * N
        return self.process(N, 0, record)

    def process(self, N: int, index: int, record: List):
        if index == N:
            return 1
        ways = 0
        for col in range(N):
            if self.validate_conflict(record, index, col):
                record[index] = col
                ways += self.process(N, index + 1, record)
        return ways

    def validate_conflict(self, record: List[int], index: int, col: int):
        for i in range(index):
            # 校验列/左下对角线/右下对角线是否冲突
            if col == record[i] or abs(record[i] - col) == abs(index - i):
                return False
        return True


class Solution2:
    def queen(self, N: int):
        """
        使用位运算实现
        """
        pass


def main():
    n = 4
    t1 = time.time()
    solution = Solution()
    res1 = solution.queen(n)
    t2 = time.time()
    print(t2 - t1, res1)


if __name__ == '__main__':
    main()
