"""
堆结构的实现
"""


class MyMaxHeap(object):
    """大顶堆"""
    heap: list
    limit: int

    def __init__(self, limit: int):
        self.limit = limit
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def is_full(self):
        return len(self.heap) == self.limit

    def push(self, value: int):
        if self.is_full():
            raise RuntimeError('堆满了，不能放数据了！')
        self.heap.append(value)
        index = len(self.heap) - 1
        self.heap_insert(self.heap, index)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('堆空了，不能拿数据了！')
        res = self.heap[0]
        index = len(self.heap) - 1
        self.swap(self.heap, 0, index)
        self.heap.pop()
        self.heapify(self.heap, 0)
        return res

    def swap(self, arr: list, left: int, right: int):
        """
        交换堆中两个位置元素
        """
        min_index = min(left, right)
        max_index = max(left, right)
        if 0 <= min_index < max_index < len(self.heap):
            arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

    def heap_insert(self, arr: list, index: int):
        """
        新加进来的数，现在停在了index位置，请依次往上移动，
        移动到0位置，或者干不掉自己的父亲了，停！
        """
        while True:
            parent_index = (index - 1) >> 1
            if index != parent_index and arr[index] > arr[parent_index]:
                self.swap(arr, parent_index, index)
                index = parent_index
            else:
                break

    def heapify(self, arr: list, index: int):
        """
        从index位置，往下看，不断的下沉
        停：较大的孩子都不再比index位置的数大；已经没孩子了
        """
        heap_size = len(self.heap)
        left_child = index >> 1 + 1
        while left_child < heap_size:
            right_child = left_child + 1
            largest = right_child if right_child < heap_size and arr[right_child] > arr[left_child] else left_child
            largest = largest if arr[largest] > arr[index] else index
            if largest == index:
                break
            self.swap(arr, index, largest)
            index = largest
            left_child = index >> 1 + 1

    def __str__(self):
        return ','.join(map(str, self.heap))


def main():
    heap = MyMaxHeap(10)
    heap.push(2)
    heap.push(4)
    heap.push(3)
    print(heap)

    res = heap.pop()
    print(res)
    print(heap)


if __name__ == '__main__':
    main()
