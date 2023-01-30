"""
@Author : long
Date : 2023/1/30 13:59

使用Python列表实现循环队列FIFO
"""
from typing import Any
from data_structures.queue import QueueEmptyError


class CircularQueue:

    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        self.queue = [0] * capacity
        self.size = 0
        self.head_index = 0
        self.tail_index = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self) -> Any:
        if self.is_empty():
            raise QueueEmptyError
        return self.queue[self.head_index]

    def enqueue(self, data: Any) -> Any:
        """
        入队列
        >>> queue = CircularQueue()
        >>> queue.enqueue("A")
        >>> (queue.size, queue.first())
        (1, 'A')
        >>> queue.enqueue("B")
        >>> (queue.size, queue.first())
        (2, 'A')
        """
        self.queue[self.tail_index] = data
        self.tail_index = (self.tail_index + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)
        return self

    def dequeue(self) -> Any:
        """
        出队列
        >>> queue = CircularQueue()
        >>> queue.dequeue()
        Traceback (most recent call last):
           ...
        data_structures.queue.QueueEmptyError
        >>> queue.enqueue("A").enqueue("B").dequeue()
        'A'
        >>> (queue.size, queue.first())
        (1, 'B')
        >>> queue.dequeue()
        'B'
        """
        if self.is_empty():
            raise QueueEmptyError
        data = self.queue[self.head_index]
        self.head_index = (self.head_index + 1) % self.capacity
        self.size -= 1
        return data
