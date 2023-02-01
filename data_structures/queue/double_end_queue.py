"""
双端队列
"""

from typing import Any, Iterable


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Node | None = None
        self.prev: Node | None = None


class DoubleEndQueue(object):
    """
    Operations
    ----------
    push(data: Any) -> None
    push_left(data: Any) -> None
    extend(iterable: Iterable) -> None
    extend_left(iterable: Iterable) -> None
    pop() -> Any
    pop_left() -> Any
    is_empty() -> bool
    ----------
    Attributes
    ----------
    head: Node
        head of the deque. the first element
    tail: Node
        back of the element a.k.a. the last element
    length: int
        the number of nodes
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "->".join(str(item) for item in iter(self))

    def push(self, data: Any) -> None:
        """
        push data to the back of the deque
        >>> queue = DoubleEndQueue()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.push(3)
        >>> queue
        1->2->3
        """
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def push_left(self, data: Any) -> None:
        """
        push data to the front of the deque
        >>> queue = DoubleEndQueue()
        >>> queue.push_left(1)
        >>> queue.push_left(2)
        >>> queue.push_left(3)
        >>> queue
        3->2->1
        """
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def extend(self, iterable: Iterable) -> None:
        """
        extend the deque with iterable
        >>> queue = DoubleEndQueue()
        >>> queue.extend([1, 2, 3])
        >>> queue
        1->2->3
        """
        for item in iterable:
            self.push(item)

    def extend_left(self, iterable: Iterable) -> None:
        """
        extend the deque with iterable
        >>> queue = DoubleEndQueue()
        >>> queue.extend_left([1, 2, 3])
        >>> queue
        3->2->1
        """
        for item in iterable:
            self.push_left(item)

    def pop(self) -> Any:
        """
        pop data from the back of the deque
        >>> queue = DoubleEndQueue()
        >>> queue.extend([1, 2, 3])
        >>> queue.pop()
        3
        >>> queue.pop()
        2
        """
        if self.head is None:
            raise IndexError("pop from empty deque")
        delete_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return delete_node.data

    def pop_left(self) -> Any:
        """
        pop data from the front of the deque
        >>> queue = DoubleEndQueue()
        >>> queue.extend([1, 2, 3])
        >>> queue.pop_left()
        1
        >>> queue.pop_left()
        2
        """
        if self.head is None:
            raise IndexError("pop from empty deque")
        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return delete_node.data
