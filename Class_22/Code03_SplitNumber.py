"""
给定一个正数n，求n的裂开方法数，
规定：后面的数不能比前面的数小
比如4的裂开方法有：
1+1+1+1、1+1+2、1+3、2+2、4
5种，所以返回5
"""
import time
from typing import List


class Solution:
    def split_number(self, n: int):
        pass


class Solution2:
    def split_number(self, n: int):
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
