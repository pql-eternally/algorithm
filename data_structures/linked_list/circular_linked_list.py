"""
环形链表
"""
from typing import Any
from data_structures.linked_list import Node
from data_structures.linked_list.make_linked_list import make_linked_list


class LinkedListEmptyError(Exception):
    pass


class CircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
            if current == self.head:
                break

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def __str__(self):
        data_list = []
        for node in self:
            data_list.append(str(node.data))
        return " --> ".join(data_list)

    def insert_tail(self, data: Any) -> None:
        """
        从链表尾部插入数据
        >>> linked_list = CircularLinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list)
        1 --> 2 --> 3
        """
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.size += 1

    def insert_head(self, data: Any) -> None:
        """
        从链表头部插入数据
        >>> linked_list = CircularLinkedList()
        >>> linked_list.insert_head(1)
        >>> linked_list.insert_head(2)
        >>> linked_list.insert_head(3)
        >>> print(linked_list)
        3 --> 2 --> 1
        """
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.head = node
        self.size += 1

    def delete_tail(self) -> Any:
        """
        从链表尾部删除数据
        >>> linked_list = CircularLinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list.delete_tail())
        3
        >>> print(linked_list.delete_tail())
        2
        """
        if self.is_empty():
            raise LinkedListEmptyError

        delete_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            for node in self:
                if node.next == delete_node:
                    self.tail = node
                    self.tail.next = self.head
                    break
        delete_node.next = None
        self.size -= 1
        return delete_node.data

    def delete_head(self) -> Any:
        """
        从链表尾部删除数据
        >>> linked_list = CircularLinkedList()
        >>> linked_list.insert_head(1)
        >>> linked_list.insert_head(2)
        >>> linked_list.insert_head(3)
        >>> print(linked_list.delete_head())
        3
        >>> print(linked_list.delete_head())
        2
        """
        if self.is_empty():
            raise LinkedListEmptyError

        delete_node = self.head
        # 仅有一个节点
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return delete_node.data


class ContainsLoopError(Exception):
    pass


def has_loop(head: Node) -> bool:
    """
    判断链表是否有环
    >>> linked_list = CircularLinkedList()
    >>> linked_list.insert_tail(1)
    >>> linked_list.insert_tail(2)
    >>> linked_list.insert_tail(3)
    >>> head_node = linked_list.head
    >>> print(has_loop(head_node))
    True
    >>> head_node = make_linked_list([1, 2, 3])
    >>> print(has_loop(head_node))
    False
    """
    visited = []
    node = head
    while node:
        if node in visited:
            return True
        visited.append(node)
        node = node.next
    return False
