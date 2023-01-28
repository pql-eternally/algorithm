"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

leetcode链接：https://leetcode.com/problems/largest-rectangle-in-histogram
"""
import random
from typing import List

from Code01_MonotonousStack import get_near_less_with_repeat, Stack


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        L = len(heights)
        stack = Stack[int]()
        for index, height in enumerate(heights):
            while not stack.is_empty() and heights[stack.peek()] >= height:
                cur_index = stack.pop()
                cur_height = heights[cur_index]
                left_index = -1 if stack.is_empty() else stack.peek()
                cur_res = cur_height * (index - left_index - 1)
                res = max(res, cur_res)
            stack.push(index)
        while not stack.is_empty():
            cur_index = stack.pop()
            cur_height = heights[cur_index]
            left_index = -1 if stack.is_empty() else stack.peek()
            cur_res = cur_height * (L - left_index - 1)
            res = max(res, cur_res)
        return res


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        pass
    print('Done ...')


if __name__ == '__main__':
    main()
