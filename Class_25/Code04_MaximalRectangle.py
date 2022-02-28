"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

leetcode: https://leetcode.com/problems/maximal-rectangle/
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


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_area = 0
        row_height = [0] * len(matrix[0])
        for row in matrix:
            for index, col in enumerate(row):
                row_height[index] = 0 if col == '0' else row_height[index] + 1
            max_area = max(max_area, self.maxRectangleFromBottom(row_height))
        return max_area

    def maxRectangleFromBottom(self, row_height: List[int]) -> int:
        """
        求以每个位置为最小值时，返回面积最大的情况
        """
        if not row_height:
            return 0
        max_area = 0
        length = len(row_height)
        stack = Stack[int]()
        for index, height in enumerate(row_height):
            while not stack.is_empty() and height <= row_height[stack.peek()]:
                cur_index = stack.pop()
                cur_height = row_height[cur_index]
                left_index = -1 if stack.is_empty() else stack.peek()
                cur_width = index - left_index - 1
                cur_area = cur_height * cur_width
                max_area = max(max_area, cur_area)
            stack.push(index)
        while not stack.is_empty():
            cur_index = stack.pop()
            cur_height = row_height[cur_index]
            left_index = -1 if stack.is_empty() else stack.peek()
            cur_width = length - left_index - 1
            cur_area = cur_height * cur_width
            max_area = max(max_area, cur_area)
        return max_area


def main():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    solution = Solution()
    res = solution.maximalRectangle(matrix)
    print(res)


if __name__ == '__main__':
    main()
