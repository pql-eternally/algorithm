"""
给你一个整数数组arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。

链接：https://leetcode.cn/problems/rank-transform-of-an-array
"""
from typing import List


class Solution:
    def arrayRankTransform1(self, arr: List[int]) -> List[int]:
        """
        大批量数据时会超时
        """
        order_arr = list(set(arr))
        order_arr.sort()
        for index, num in enumerate(arr):
            arr[index] = order_arr.index(num) + 1
        return arr

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {num: i for i, num in enumerate(sorted(set(arr)), 1)}
        return [ranks[num] for num in arr]


if __name__ == '__main__':
    s = Solution()
    # arr = [40, 10, 20, 30]
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    res = s.arrayRankTransform(arr)
    print(res)
