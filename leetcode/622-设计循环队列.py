"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

链接：https://leetcode.cn/problems/design-circular-queue
"""
from typing import List


class MyCircularQueue:
    _queue: List[int]

    def __init__(self, k: int):
        self._queue = []
        self._size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._queue.pop(0)
        return True

    def Front(self) -> int:
        if not self._queue:
            return -1
        return self._queue[0]

    def Rear(self) -> int:
        if not self._queue:
            return -1
        return self._queue[-1]

    def isEmpty(self) -> bool:
        return len(self._queue) == 0

    def isFull(self) -> bool:
        return len(self._queue) == self._size


if __name__ == '__main__':
    queue = MyCircularQueue(3)
    res1 = queue.enQueue(1)
    res2 = queue.enQueue(2)
    res3 = queue.enQueue(3)
    res4 = queue.enQueue(4)
    res5 = queue.deQueue()
    res6 = queue.Front()
    res7 = queue.Rear()
    res8 = queue.isEmpty()
    res9 = queue.isFull()
    print(res1, res2, res3, res4)
    print(res5)
    print(res6, res7)
    print(res8, res9)
