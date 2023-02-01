"""
使用列表实现队列
"""
from typing import Any


class ListQueue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self) -> bool:
        """
        判断队列是否为空
        >>> queue = ListQueue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue(1)
        >>> queue.is_empty()
        False
        """
        return self.queue == []

    def enqueue(self, item) -> None:
        """
        入队列
        >>> queue = ListQueue()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> str(queue)
        '1->2->3'
        """
        self.queue.append(item)

    def dequeue(self) -> Any:
        """
        出队列
        >>> queue = ListQueue()
        >>> queue.dequeue()
        Traceback (most recent call last):
        ...
        IndexError: pop from empty list
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.dequeue()
        1
        """
        return self.queue.pop(0)

    def size(self) -> int:
        """
        返回队列的大小
        >>> queue = ListQueue()
        >>> queue.size()
        0
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> queue.size()
        3
        """
        return len(self.queue)

    def __str__(self) -> str:
        return "->".join([str(item) for item in self.queue])
