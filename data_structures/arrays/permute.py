"""
@Author : long
Date : 2023/1/28 16:06

返回列表的所有排列组合情况.
>>> from itertools import permutations
>>> list(permutations([1, 2, 3]))
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    >>> from itertools import permutations
    >>> numbers= [1,2,3]
    >>> all(list(nums) in permute(numbers) for nums in permutations(numbers))
    True
    """
    result = []
    len_array = len(nums)
    if len_array == 1:
        return [nums.copy()]

    for _ in range(len_array):
        n = nums.pop(0)
        permutations = permute(nums)
        for p in permutations:
            p.append(n)
        result.extend(permutations)
        nums.append(n)
    return result


def main():
    result = permute([1, 2, 3])
    print(result)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
