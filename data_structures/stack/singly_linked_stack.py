"""
A Stack using a linked list like structure
"""
from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Node[T] | None = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedStack(Generic[T]):
    """
    Linked List Stack implementing push (to top), pop (from top) and is_empty
    """

    def __init__(self):
        self.top: Node[T] | None = None

    def __iter__(self) -> Iterator[T]:
        node = self.top
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        >>> stack = LinkedStack[int]()
        >>> stack.push(5)
        >>> stack.push(9)
        >>> stack.push(1)
        >>> print(stack)
        1->9->5
        """
        return "->".join(str(item) for item in self)

    def push(self, data: T) -> None:
        """
        Add an item to the top of the stack
        """
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self) -> T:
        """
        Remove an item from the top of the stack
        """
        if self.top is None:
            raise IndexError("pop from empty stack")
        node = self.top
        self.top = node.next
        return node.data

    def peek(self) -> T:
        """
        Return the top item from the stack without removing it
        """
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data

    def clear(self) -> None:
        """
        Remove all items from the stack
        """
        self.top = None
