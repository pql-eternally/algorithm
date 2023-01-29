"""
@Author : long
Date : 2023/1/29 10:15

单链表相关案例
"""
from typing import Any, List
from data_structures.linked_list import Node


class LinkedListEmptyError(Exception):
    pass


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        if self.is_empty():
            return ""

        item_list: List[str] = []
        node = self.head
        while node:
            item_list.append(str(node.data))
            node = node.next
        return " --> ".join(item_list)

    def __len__(self) -> int:
        return self.size

    def insert_tail(self, data: Any) -> None:
        """
        从链表尾部插入数据
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list)
        1 --> 2 --> 3
        """
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node
        self.size += 1

    def insert_head(self, data: Any) -> None:
        """
        从链表头部插入数据
        >>> linked_list = LinkedList()
        >>> linked_list.insert_head(1)
        >>> linked_list.insert_head(2)
        >>> linked_list.insert_head(3)
        >>> print(linked_list)
        3 --> 2 --> 1
        """
        if self.is_empty():
            self.head = self.tail = Node(data)
            return
        self.head = Node(data, self.head)
        self.size += 1

    def delete_tail(self) -> Any:
        """
        从链表尾部删除数据
        >>> linked_list = LinkedList()
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
        current_node = self.head
        while current_node:
            if current_node.next == delete_node:
                self.tail = current_node
                current_node.next = None
                break
            current_node = current_node.next
        data = delete_node.data
        del delete_node
        self.size -= 1
        return data

    def delete_head(self) -> Any:
        """
        从链表头部删除数据
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(2)
        >>> linked_list.insert_tail(3)
        >>> print(linked_list.delete_head())
        1
        """
        if self.is_empty():
            raise LinkedListEmptyError
        delete_node = self.head
        new_head = self.head.next
        if new_head is None:
            self.head = self.tail = None
        else:
            self.head = new_head
        data = delete_node.data
        del delete_node
        self.size -= 1
        return data
