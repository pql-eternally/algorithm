"""
大顶堆（Max Heap）是一种二叉树，其中每个节点的值都大于或等于其子节点的值。大顶堆排序就是利用大顶堆的性质来进行排序。

构造大顶堆的步骤：
1、从最后一个非叶子节点开始，向前依次对每个非叶子节点进行堆调整（heapify）操作，使得每个非叶子节点的值都大于或等于其子节点的值。

堆排序步骤：
1、将初始序列构建成一个大顶堆
2、将堆顶元素与末尾元素交换，此时末尾就为最大值。
3、然后将剩余的n-1个元素重新构建成一个大顶堆，这样会得到n个元素中的次大值。
4、重复步骤2和步骤3，直到所有元素都被排好序。
"""
from math import log2, ceil

from typing import Iterable, Generator, List


class Heap(object):
    """
    A Max Heap Implementation
    """

    def __init__(self) -> None:
        self.heap = []
        self.heap_size = 0

    def heapify(self, index: int) -> None:
        """
        Maintain the max heap property
        """
        largest = index
        # 计算当前节点左右子节点的索引
        left = 2 * index + 1
        right = 2 * index + 2
        if left < self.heap_size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right
        # 如果当前节点不是最大值，则交换当前节点和最大值节点的值，并递归调用heapify
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def build_heap(self, nums: Iterable[int]) -> None:
        """
        Build a max heap from a list of numbers
        >>> heap = Heap()
        >>> heap.heap_sort([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
        >>> heap
        [10, 9, 8, 7, 6, 3, 4, 1, 2, 5]
        """
        self.heap = list(nums)
        self.heap_size = heap_size = len(self.heap)
        # 计算最后一个非叶子节点的索引
        for i in range(heap_size // 2 - 1, -1, -1):
            self.heapify(i)

    def convert_str(self, nums: Iterable[int]) -> Generator:
        for num in nums:
            if num < 10:
                yield f" {num}"
            else:
                yield str(num)

    def print_heap(self):
        """
        按堆的层级错位输出堆
        """
        # 计算堆的深度
        deep = ceil(log2(self.heap_size))
        n = 0
        while 2 ** n <= self.heap_size:
            # 当前层级的堆
            level_heap = self.heap[2 ** n - 1: 2 ** (n + 1) - 1]
            space_gap = 2 ** (deep - n - 1)
            print(' ' * space_gap + ('  ' * space_gap).join(self.convert_str(level_heap)))
            n += 1
        print('-----------------')

    def heap_sort(self, nums: Iterable[int]) -> List:
        """
        堆排序
        >>> heap = Heap()
        >>> res = heap.heap_sort([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
        >>> res
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        """
        result = []
        self.build_heap(nums)
        for i in range(self.heap_size - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            result.append(self.heap.pop())
            self.heap_size -= 1
            self.heapify(0)
        return result

    __repr__ = __str__ = lambda self: str(self.heap)


def main():
    heap = Heap()
    heap.build_heap([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
    print(heap)


if __name__ == '__main__':
    main()
