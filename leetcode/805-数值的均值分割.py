"""
给定你一个整数数组 nums

我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。

如果可以完成则返回true ， 否则返回 false  。

注意：对于数组 arr ,  average(arr) 是 arr 的所有元素除以 arr 长度的和。
"""
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 1、为防止求平均值时出行小数，将数组中的每个数都乘以总数
        count = len(nums)
        if count < 2:
            return False
        avg = sum(nums)

        # 2、将数组中的每个数都减去平均值
        nums = [num * count - avg for num in nums]
        if 0 in nums:
            return True

        # 3、从数组中找子集和为0

