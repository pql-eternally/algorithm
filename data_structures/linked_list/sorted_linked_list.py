"""
@Author : long
Date : 2023/1/30 09:33

有序链表
"""
from typing import Iterable, Iterator
from data_structures.linked_list import Node

test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 11, 0, 8, 10, 3, -2)


class SortedLinkedList:

    def __init__(self, nums: Iterable[int]) -> None:
        head = prev = None
        for num in sorted(nums):
            node = Node(num)
            if head is None:
                head = prev = node
            else:
                prev.next = node
                prev = node
        self.head = head

    def __iter__(self) -> Iterator[Node]:
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        """
        >>> len(SortedLinkedList([]))
        0
        >>> len(SortedLinkedList(test_data_odd))
        8
        """
        return len(list(iter(self)))

    def __str__(self):
        """
        >>> str(SortedLinkedList([]))
        ''
        >>> str(SortedLinkedList(test_data_odd))
        '-11 --> -1 --> 0 --> 1 --> 3 --> 5 --> 7 --> 9'
        >>> str(SortedLinkedList(test_data_even))
        '-2 --> 0 --> 2 --> 3 --> 4 --> 6 --> 8 --> 10 --> 11'
        """
        return " --> ".join([str(node.data) for node in self])


def merge_sorted_linked_list(left: SortedLinkedList, right: SortedLinkedList) -> SortedLinkedList:
    """
    合并两个有序链表成为一个大的有序链表
    >>> merged = merge_sorted_linked_list(SortedLinkedList(test_data_odd), SortedLinkedList(test_data_even))
    >>> len(merged)
    16
    >>> print(merged)
    -11 --> -2 --> -1 --> 0 --> 0 --> 1 --> 2 --> 3 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10 --> 11
    """
    nums = [node.data for node in left] + [node.data for node in right]
    return SortedLinkedList(nums)


def merge_sorted_linked_list2(left: SortedLinkedList, right: SortedLinkedList) -> SortedLinkedList:
    """
    合并两个有序链表成为一个大的有序链表
    >>> merged = merge_sorted_linked_list2(SortedLinkedList(test_data_odd), SortedLinkedList(test_data_even))
    >>> print(merged)
    -11 --> -2 --> -1 --> 0 --> 0 --> 1 --> 2 --> 3 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9 --> 10 --> 11
    """
    nums = []
    left = iter(left)
    right = iter(right)
    left_node = next(left)
    right_node = next(right)
    while True:
        if left_node.data <= right_node.data:
            nums.append(left_node.data)
            try:
                left_node = next(left)
            except StopIteration:
                nums.append(right_node.data)
                break
        else:
            nums.append(right_node.data)
            try:
                right_node = next(right)
            except StopIteration:
                nums.append(left_node.data)
                break
    nums.extend([node.data for node in left])
    nums.extend([node.data for node in right])
    return SortedLinkedList(nums)
