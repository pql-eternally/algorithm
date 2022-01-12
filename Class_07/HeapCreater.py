"""
加强堆的实现
"""


class HeapCreator(object):
    heap: list = None
    # 索引表
    index_map = dict = None
    heap_size = int = 0

    def __init__(self):
        self.heap = []
        self.heap_size = 0
        self.index_map = {}

    def heapify(self, index) -> int:
        """
        从index位置，往下看，不断的下沉
        停：较小的孩子都不再比index位置的数小；已经没孩子了
        返回新的index值
        """
        child_index = (index << 1) + 1
        while child_index < self.heap_size:
            right_child_index = child_index + 1
            if right_child_index < self.heap_size and self.heap[right_child_index] < self.heap[child_index]:
                child_index = right_child_index
            if self.heap[index] < self.heap[child_index]:
                break
            self.swap(index, child_index)
            index = child_index
            child_index = (index << 1) + 1
        return index

    def heap_insert(self, index) -> int:
        """
        新加进来的数，现在停在了index位置，请依次往上移动，
        移动到0位置，或者干不掉自己的父亲了，停！
        返回新的index值
        """
        parent_index = (index - 1) >> 1
        while parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) >> 1
        return index

    def is_empty(self):
        return self.heap_size == 0

    def size(self):
        return self.heap_size

    def contains(self, value: int) -> bool:
        """
        查看当前值是否存在堆中
        """
        return value in self.index_map

    def push(self, value):
        """
        堆中添加元素
        """
        self.heap.append(value)
        self.heap_size += 1
        index = self.heap_size - 1
        index = self.heap_insert(index)
        self.index_map[value] = index

    def pop(self):
        """
        移除堆顶元素
        """
        if self.is_empty():
            raise RuntimeError('empty')
        last_index = self.heap_size - 1
        self.swap(0, last_index)
        item = self.heap.pop(last_index)
        self.heap_size -= 1
        self.index_map.pop(item)
        self.heapify(0)
        return item

    def remove(self, value: int):
        """
        移除堆中当前值，并保证堆有序
        """
        if value not in self.index_map:
            raise RuntimeError('Not exist')
        index = self.index_map[value]
        last_index = self.heap_size - 1
        if index != last_index:
            self.swap(index, last_index)
        self.heap.pop(last_index)
        self.heap_size -= 1
        self.index_map.pop(value)
        self.resign(index)

    def resign(self, index: int):
        """
        调整堆
        """
        self.heapify(index)
        self.heap_insert(index)

    def peek(self):
        """
        查看堆顶元素，不进行移除
        """
        if self.is_empty():
            raise RuntimeError('empty')
        return self.heap[0]

    def get_all_elements(self):
        """
        获取堆中所有元素
        """
        return self.heap

    def swap(self, i: int, j: int) -> None:
        """
        交换堆中两个位置元素
        """
        heap = self.heap
        self.index_map[heap[i]] = j
        self.index_map[heap[j]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def __str__(self):
        # TODO: print tree
        return ', '.join(map(str, self.get_all_elements()))


def main():
    heap = HeapCreator()
    heap.push(2)
    heap.push(4)
    heap.push(3)
    heap.push(5)
    heap.push(1)
    heap.push(6)
    heap.push(7)
    print(heap)
    # print(heap.peek())
    # print(heap.get_all_elements())
    # heap.pop()
    # print(heap)
    heap.remove(2)
    print(heap)
    heap.remove(4)
    print(heap)


if __name__ == '__main__':
    main()
