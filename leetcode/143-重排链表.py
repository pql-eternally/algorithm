"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """
        输出当前节点及后续所有节点
        """
        data_list = []
        node = self
        while node:
            data_list.append(str(node.val))
            node = node.next
        return " --> ".join(data_list)


class Solution:

    def compute_mid_node(self, head: ListNode) -> ListNode:
        # slow指向上中点
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 断开链表返回下中点
        down_head = slow.next
        slow.next = None
        return down_head

    def reverse_list(self, head: ListNode) -> ListNode:
        # 将链表反转
        pre = None
        node = head
        while node:
            next_node = node.next
            node.next = pre
            pre = node
            node = next_node
        return pre

    def merge_list(self, head: ListNode, down: ListNode) -> ListNode:
        # 交叉合并链表
        up = head
        while up and down:
            up_next = up.next
            down_next = down.next
            up.next = down
            down.next = up_next
            up = up_next
            down = down_next
        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid_head = self.compute_mid_node(head)
        down_head = self.reverse_list(mid_head)
        self.merge_list(head, down_head)


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(head)
    Solution().reorderList(head)
    print(head)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    print(Solution().reorderList(head))

    head = ListNode(1)
    print(head)
    print(Solution().reorderList(head))

    head = None
    print(Solution().reorderList(head))
