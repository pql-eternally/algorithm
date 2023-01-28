"""
@Author : long
Date : 2023/1/28 15:40

前缀和数组的实现，可以快速求数组中任意两个位置的求和。
"""
from typing import List


class PrefixSum:

    def __init__(self, array: List[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        """
        返回列表中从开始位置到结束位置的求和
        时间复杂的: O(1)
        空间复杂度: O(1)

        >>> PrefixSum([1,2,3]).get_sum(0, 2)
        6
        >>> PrefixSum([1,2,3]).get_sum(1, 2)
        5
        >>> PrefixSum([1,2,3]).get_sum(2, 2)
        3
        >>> PrefixSum([1,2,3]).get_sum(2, 3)
        Traceback (most recent call last):
        ...
        IndexError: list index out of range
        """
        if start == 0:
            return self.prefix_sum[end]

        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        """
        判断当前列表中是否包含目标和
        时间复杂的: O(n)
        空间复杂度: O(n)

        >>> PrefixSum([1,2,3]).contains_sum(6)
        True
        >>> PrefixSum([1,2,3]).contains_sum(5)
        True
        >>> PrefixSum([1,2,3]).contains_sum(3)
        True
        >>> PrefixSum([1,2,3]).contains_sum(4)
        False
        >>> PrefixSum([1,2,3]).contains_sum(7)
        False
        >>> PrefixSum([1,-2,3]).contains_sum(2)
        True
        """
        sums = {0}

        for sum_item in self.prefix_sum:
            if sum_item - target_sum in sums:
                return True
            sums.add(sum_item)
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
