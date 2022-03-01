"""
给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。

示例 1：

输入：mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
输出：13
解释：
有 6个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13。
示例 2：

输入：mat = [[0,1,1,0],
           [0,1,1,1],
           [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21
示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5

链接：https://leetcode-cn.com/problems/count-submatrices-with-all-ones
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
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        nums = 0
        row_height = [0] * len(mat[0])
        for row in mat:
            for index, col in enumerate(row):
                row_height[index] = 0 if col == 0 else row_height[index] + 1
            nums += self.countFromBottom(row_height)
        return nums

    def countFromBottom(self, row_height: List[int]):
        if not row_height:
            return 0
        nums = 0
        length = len(row_height)
        stack = Stack[int]()
        for index, height in enumerate(row_height):
            while not stack.is_empty() and height <= row_height[stack.peek()]:
                cur_index = stack.pop()
                left_index = -1 if stack.is_empty() else stack.peek()
                n = index - left_index - 1
                down = max(0 if left_index == -1 else row_height[left_index], height)
                nums += (row_height[cur_index] - down) * self.calc_num(n)
            stack.push(index)

        while not stack.is_empty():
            cur_index = stack.pop()
            left_index = -1 if stack.is_empty() else stack.peek()
            n = length - left_index - 1
            down = 0 if left_index == -1 else row_height[left_index]
            nums += (row_height[cur_index] - down) * self.calc_num(n)
        return nums

    def calc_num(self, n: int) -> int:
        return (n * (n + 1)) >> 1


def main():
    mat = [[1, 0, 1],
           [1, 1, 0],
           [1, 1, 0]]
    mat = [[0, 1, 1, 0],
           [0, 1, 1, 1],
           [1, 1, 1, 0]]
    mat = [[1, 1, 1, 1, 1, 1]]
    solution = Solution()
    res = solution.numSubmat(mat)
    print(res)


if __name__ == '__main__':
    main()
