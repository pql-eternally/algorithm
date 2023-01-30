"""
@Author : long
Date : 2023/1/30 10:58

"""
from typing import Any
from data_structures.linked_list import DoubleNode


class DoublyLinkedListEmptyError(Exception):
    pass


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self) -> bool:
        return self.head is None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        data_list = [str(node.data) for node in iter(self)]
        return ' <--> '.join(data_list)

    def insert_tail(self, data: Any) -> None:
        """
        从链表尾部插入数据
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list)
        1 <--> 2 <--> 3
        """
        node = DoubleNode(data, pre=self.tail)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_head(self, data: Any) -> None:
        """
        从链头尾部插入数据
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_head(1)
        >>> linked_list.insert_head(2)
        >>> linked_list.insert_head(3)
        >>> print(linked_list)
        3 <--> 2 <--> 1
        """
        node = DoubleNode(data, next=self.head)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.head.pre = node
            self.head = node
        self.size += 1

    def delete_tail(self) -> Any:
        """
        从链表尾部删除数据
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list.delete_tail())
        3
        >>> print(linked_list)
        1 <--> 2
        """
        if self.is_empty():
            raise DoublyLinkedListEmptyError

        delete_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            pre = delete_node.pre
            pre.next = None
            delete_node.pre = None
            self.tail = pre
            self.size -= 1
        return delete_node.data

    def delete_head(self) -> Any:
        """
        从链表头部删除数据
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_head(1)
        >>> linked_list.insert_head(2)
        >>> linked_list.insert_head(3)
        >>> print(linked_list.delete_head())
        3
        >>> print(linked_list)
        2 <--> 1
        """
        if self.is_empty():
            raise DoublyLinkedListEmptyError

        delete_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            next_node = delete_node.next
            next_node.pre = None
            delete_node.next = None
            self.head = next_node
            self.size -= 1
        return delete_node.data
