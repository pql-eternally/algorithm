"""
给定一个整数数组 arr，找到 min(b)的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums

示例 1：
输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

示例 2：
输入：arr = [11,81,94,43,3]
输出：444
"""
from typing import List, TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.data = []

    def push(self, item: T) -> None:
        self.data.append(item)

    def pop(self) -> T:
        if self.is_empty():
            return
        return self.data.pop()

    def peek(self) -> T:
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


class Solution1:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        暴力解
        """
        sums = 0
        length = len(arr)
        for i in range(length):
            for j in range(i, length):
                sub_arr = arr[i: j + 1]
                sums += min(sub_arr)
        return sums


class Solution2:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        小心算重
        """


class Solution3:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr_sums = 0
        stack = Stack[int]()
        for index, num in enumerate(arr):
            while not stack.is_empty() and num <= arr[stack.peek()]:
                cur_index = stack.pop()

                left_index = -1 if stack.is_empty() else stack.peek()
                width = index - left_index - 1

            stack.push(index)
        while not stack.is_empty():
            cur_index = stack.pop()


def main():
    # arr = [3, 1, 2, 4]
    # arr = [11, 81, 94, 43, 3]
    arr = [3, 1, 2, 4, 2, 2, 1, 5]
    s1 = Solution1()
    res = s1.sumSubarrayMins(arr)
    print(res)


if __name__ == '__main__':
    main()
