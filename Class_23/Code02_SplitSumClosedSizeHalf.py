"""
给定一个正数数组arr，请把arr中所有的数分成两个集合
如果arr长度为偶数，两个集合包含数的个数要一样多
如果arr长度为奇数，两个集合包含数的个数必须只差一个
请尽量让两个集合的累加和接近
返回最接近的情况下，较小集合的累加和
"""
import time
from typing import List


class Solution:
    def split_arr(self, arr: List[int]):
        pass


class Solution2:
    def split_arr(self, arr: List[int]):
        pass


def main():
    arr = []
    t1 = time.time()
    solution = Solution()
    res1 = solution.split_arr(arr)
    t2 = time.time()
    print(t2 - t1, res1)

    solution2 = Solution2()
    res2 = solution2.split_arr(arr)
    t3 = time.time()
    print(t3 - t2, res2)


if __name__ == '__main__':
    main()
