"""
使用链表实现队列
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedQueue:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        """
        >>> linked_list = LinkedQueue()
        >>> for i in range(0, 5):
        ...     linked_list.enqueue(i)
        >>> len(linked_list) == 5
        True
        """
        return len(tuple(iter(self)))

    def is_empty(self):
        """
        >>> queue = LinkedQueue()
        >>> queue.is_empty()
        True
        >>> queue.enqueue('python')
        >>> queue.is_empty()
        False
        """
        return self.head is None

    def enqueue(self, data):
        """
        >>> queue = LinkedQueue()
        >>> queue.enqueue('python')
        >>> queue.enqueue('java')
        >>> queue.enqueue('c')
        >>> str(queue)
        'python->java->c'
        """
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        """
        >>> queue = LinkedQueue()
        >>> queue.enqueue('python')
        >>> queue.enqueue('java')
        >>> queue.enqueue('c')
        >>> queue.dequeue()
        'python'
        >>> queue.dequeue()
        'java'
        """
        if self.head is None:
            raise IndexError("queue is empty")
        else:
            data = self.head.data
            self.head = self.head.next
            return data
