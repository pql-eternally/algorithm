"""
堆排序的实现
"""
import random
import copy
from heapq import heappush, heappop, heapify, heappushpop, heapreplace


class MyMinHeap(object):
    heap: list = None
    heap_size: int = 100

    def __init__(self, heap=None, heap_size: int = None):
        self.heap = []
        if heap:
            for i in heap:
                self.heap_insert(i)

        if heap_size:
            self.heap_size = heap_size

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def is_full(self) -> bool:
        return len(self.heap) == self.heap_size

    def heap_insert(self, item: int) -> None:
        if self.is_full():
            raise RuntimeError('full')
        heappush(self.heap, item)

    def heapify(self, pos):
        if self.is_empty():
            raise RuntimeError('empty')
        heap = self.heap
        end_pos = len(heap)
        child_pos = pos << 1 + 1
        while child_pos < end_pos:
            right_pos = child_pos + 1
            if right_pos < end_pos and heap[right_pos] < heap[child_pos]:
                child_pos = right_pos
            if heap[pos] <= heap[child_pos]:
                break
            self.swap(heap, pos, child_pos)
            pos = child_pos
            child_pos = pos << 1 + 1

    def heap_pop(self):
        if self.is_empty():
            raise RuntimeError('empty')
        return heappop(self.heap)

    def heap_sort(self):
        nums = []
        while not self.is_empty():
            item = self.heap_pop()
            nums.append(item)
        return nums

    def swap(self, arr: list, left: int, right: int):
        """
        交换堆中两个位置元素
        """
        min_index = min(left, right)
        max_index = max(left, right)
        if 0 <= min_index < max_index < len(self.heap):
            arr[min_index], arr[max_index] = arr[max_index], arr[min_index]


def generate_random_arr(max_size: int = 20, min_value: int = 0, max_value: int = 100) -> list:
    """
    生成随机数组
    """
    size = random.randint(1, max_size)
    arr = []
    for i in range(0, size):
        num = random.randint(min_value, max_value)
        arr.append(num)
    return arr


def comparator(arr):
    arr.sort()


def main():
    print('Start ...')
    test_count = 10000
    for i in range(0, test_count):
        arr = generate_random_arr(5)
        arr1 = copy.copy(arr)
        heap = MyMinHeap(arr1)
        arr1 = heap.heap_sort()
        arr2 = copy.copy(arr)
        comparator(arr2)
        if arr1 != arr2:
            print(f'arr: {arr}，res1：{arr1}，res2：{arr2}')
            return
    print('Done ...')


if __name__ == '__main__':
    main()
