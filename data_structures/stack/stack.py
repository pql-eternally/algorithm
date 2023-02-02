"""
@Author : long
Date : 2023/2/2 09:33

A stack is an abstract data type that serves as a collection of
elements with two principal operations: push() and pop(). push() adds an
element to the top of the stack, and pop() removes an element from the top
of a stack. The order in which elements come off of a stack are
Last In, First Out (LIFO).
"""

from typing import Any, List, Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Operations
    ----------
    push(data: T) -> None
    pop() -> T
    top() -> T
    is_empty() -> bool
    is_full() -> bool
    ----------
    Attributes
    ----------
    stack: List
        存放数据的列表
    capacity: int
        栈的容量
    ----------
    """

    def __init__(self, capacity: int = 10) -> None:
        self.stack: List[T] = []
        self.capacity = capacity

    def __len__(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.capacity

    def top(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def push(self, data: T) -> None:
        """
        入栈
        >>> stack = Stack()
        >>> stack.push("A")
        >>> (len(stack), stack.top())
        (1, 'A')
        >>> stack.push("B")
        >>> (len(stack), stack.top())
        (2, 'B')
        """
        if self.is_full():
            raise IndexError("Stack is full")
        self.stack.append(data)

    def pop(self) -> T:
        """
        出栈
        >>> stack = Stack()
        >>> stack.pop()
        Traceback (most recent call last):
            ...
        IndexError: Stack is empty
        >>> stack.push("A")
        >>> stack.push("B")
        >>> stack.pop()
        'B'
        >>> (stack.__len__(), stack.top())
        (1, 'A')
        >>> stack.pop()
        'A'
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def __str__(self) -> str:
        return str(self.stack)

    def __iter__(self) -> T:
        return iter(self.stack)

    def __next__(self) -> T:
        return next(self.stack)

    def __getitem__(self, index: int) -> T:
        return self.stack[index]

    def __contains__(self, item: T) -> bool:
        return item in self.stack

    def __reversed__(self) -> T:
        return reversed(self.stack)
