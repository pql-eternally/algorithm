import random
from queue import Queue, PriorityQueue
from heapq import heappush, heappop, heapify, heappushpop, heapreplace


def test_queue():
    q = Queue()
    q.put(2)
    q.put(3)
    q.put(1)

    while not q.empty():
        r = q.get()
        print(r)


def test_heap():
    """
    heapq内置heap相关操作，是小顶堆
    """
    heap = []
    for i in range(10):
        item = random.randint(0, 10)
        heappush(heap, item)
    print(heap)

    # 移除堆顶元素，添加新元素
    heapreplace(heap, 4)
    print(heap)

    while heap:
        item = heappop(heap)
        print(item, heap)


def test_priority_queue():
    heap = PriorityQueue()
    heap.put(2)
    heap.put(3)
    heap.put(1)
    heap.put(4)
    heap.put(2)
    while not heap.empty():
        item = heap.get()
        print(item)


def main():
    # test_queue()
    # test_heap()
    test_priority_queue()


if __name__ == '__main__':
    main()
