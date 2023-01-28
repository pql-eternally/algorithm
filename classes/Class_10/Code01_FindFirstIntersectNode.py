"""
给定两个可能有环也可能无环的单链表，头节点head1和head2
请实现一个函数，如果两个链表相交，请返回相交的第一个节点。如果不相交返回null
要求如果两个链表长度之和为N，时间复杂度请达到O(N)，额外空间复杂度请达到O(1)
"""


class Node(object):
    value: int = None
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'


def get_intersect_node(head1: Node, head2: Node) -> Node or None:
    """
    主程序控制
    """
    if not head1 or not head2:
        return None
    loop1 = get_loop_node(head1)
    loop2 = get_loop_node(head2)
    # 都无环
    if loop1 is None and loop2 is None:
        return no_loop(head1, head2)
    # 都有环
    if loop1 and loop2:
        return both_loop(head1, loop1, head2, loop2)
    return None


def get_loop_node(head: Node) -> Node or None:
    """
    找到链表的第一个入环节点，如果没有返回None
    步骤：
    1、需要两个指针，快慢指针，慢指针一次跳一个节点，快指针一次跳两个节点
    2、如果快指针到了尾节点，则说明无环
    3、如果快指针和慢指针相撞了，一定有环
    4、此时让快指针回到头节点，然后和慢指针一次跳一个节点
    5、再次相撞的节点就是入环的第一个节点
    """
    if head is None or head.next is None or head.next.next is None:
        return None

    # 1 two pointer
    slow = head.next
    fast = head.next.next
    while slow != fast:
        #  2 fast go to tail node
        if fast.next is None or fast.next.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    # 3 slow 相撞的节点
    # 4 reset fast and dump
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    # 5 slow is first loop node
    return slow


def no_loop(head1: Node, head2: Node) -> Node or None:
    """
    两个链表都无环，如果相交返回第一个相交节点，否则返回None
    1、依次循环两个链表到尾节点 tail1 tail2，同时求出两个链表的长度len1, len2
    2、如果两个尾节点不是一个节点，说明不相交返回None
    3、求出两个链表长度差值，让长链表先跳差值个
    4、让两个链表分别开始跳，找到第一个相交的节点
    """
    # 1
    n = 0
    cur1 = head1
    while cur1.next:
        cur1 = cur1.next
        n += 1
    cur2 = head2
    while cur2.next:
        cur2 = cur2.next
        n -= 1
    # 2
    if cur1 != cur2:
        return None
    # 3、长短链表
    long, short = (head1, head2) if n > 0 else (head2, head1)
    n = abs(n)
    while n > 0:
        long = long.next
        n -= 1
    # 4 dump
    while short != long:
        short = short.next
        long = long.next
    return short


def both_loop(head1: Node, loop1: Node, head2: Node, loop2: Node) -> Node or None:
    """
    两个链表都有环，如果相交返回第一个相交节点，否则返回None
    1、如果loop1和loop2是一个节点，则一定相交求出相交的第一个节点
    2、从loop1开始循环如果不经过了loop2则不相交，返回None
    3、返回loop1或者loop2都可以
    """
    if loop1 == loop2:
        n = 0
        cur1 = head1
        while cur1.next:
            cur1 = cur1.next
            n += 1
        cur2 = head2
        while cur2.next:
            cur2 = cur2.next
            n -= 0
        long, short = (cur1, cur2) if n > 0 else (cur2, cur1)
        while n > 0:
            long = long.next
        while short != long:
            short = short.next
            long = long.next
        return short
    else:
        cur = loop1.next
        while cur != loop1:
            if cur == loop2:
                return loop1
            cur = cur.next
        return None


def main():
    # 无环
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)

    head2 = Node(20)
    head2.next = Node(21)
    head2.next.next = Node(22)
    head2.next.next.next = head1.next.next
    res = get_intersect_node(head1, head2)
    print(res)

    # 有环
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.next = Node(7)
    head1.next.next.next.next.next.next.next = head1.next

    head2 = Node(20)
    head2.next = Node(21)
    head2.next.next = Node(22)
    # head2.next.next.next = head2.next
    head2.next.next.next = head1.next.next.next.next
    res = get_intersect_node(head1, head2)
    print(res)


if __name__ == '__main__':
    main()
