"""
输入链表头节点，奇数长度返回中点，偶数长度返回上中点
输入链表头节点，奇数长度返回中点，偶数长度返回下中点
输入链表头节点，奇数长度返回中点前一个，偶数长度返回上中点前一个
输入链表头节点，奇数长度返回中点前一个，偶数长度返回下中点前一个
"""


class Node(object):
    value: int = 0
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Node value: {self.value}'


def mid_or_up_mid_node(head: Node) -> Node:
    """
    输入链表头节点，奇数长度返回中点，偶数长度返回上中点
    """
    if head.next is None or head.next.next is None:
        return head
    slow = head.next
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_down_mid_node(head: Node) -> Node:
    """
    输入链表头节点，奇数长度返回中点，偶数长度返回下中点
    """
    if head.next is None:
        return head
    slow = head.next
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_up_mid_pre_node(head: Node) -> Node or None:
    """
    输入链表头节点，奇数长度返回中点前一个，偶数长度返回上中点前一个
    """
    if head.next is None or head.next.next is None:
        return None
    slow = head
    fast = head.next.next
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mid_or_down_mid_pre_node(head: Node) -> Node or None:
    """
    输入链表头节点，奇数长度返回中点前一个，偶数长度返回下中点前一个
    """
    if head.next is None:
        return None
    if head.next.next is None:
        return head
    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def comparator1(head: Node) -> Node:
    """
    输入链表头节点，奇数长度返回中点，偶数长度返回上中点
    """
    arr = []
    while head:
        arr.append(head)
        head = head.next
    length = len(arr)
    mid = ((length + 1) >> 1) - 1
    return arr[mid]


def comparator2(head: Node) -> Node:
    """
    输入链表头节点，奇数长度返回中点，偶数长度返回下中点
    """
    arr = []
    while head:
        arr.append(head)
        head = head.next
    length = len(arr)
    mid = length >> 1
    return arr[mid]


def comparator3(head: Node) -> Node or None:
    """
    输入链表头节点，奇数长度返回中点前一个，偶数长度返回上中点前一个
    """
    arr = []
    while head:
        arr.append(head)
        head = head.next
    length = len(arr)
    mid = ((length - 1) >> 1) - 1
    if mid < 0:
        return None
    return arr[mid]


def comparator4(head: Node) -> Node or None:
    """
    输入链表头节点，奇数长度返回中点前一个，偶数长度返回下中点前一个
    """
    arr = []
    while head:
        arr.append(head)
        head = head.next
    length = len(arr)
    mid = (length >> 1) - 1
    if mid < 0:
        return None
    return arr[mid]


def print_node(head):
    while head:
        print(head.value, end=', ')
        head = head.next
    print()


def main():
    head = Node(0)
    cur = head
    for i in range(1, 5):
        cur.next = Node(i)
        cur = cur.next
    print_node(head)

    n1 = mid_or_up_mid_node(head)
    n11 = comparator1(head)
    assert n1 == n11, (n1 and n1.value, n11 and n11.value)

    n2 = mid_or_down_mid_node(head)
    n22 = comparator2(head)
    assert n2 == n22, (n2 and n2.value, n22 and n22.value)

    n3 = mid_or_up_mid_pre_node(head)
    n33 = comparator3(head)
    assert n3 == n33, (n3 and n3.value, n33 and n33.value)

    n4 = mid_or_down_mid_pre_node(head)
    n44 = comparator4(head)
    assert n4 == n44, (n4 and n4.value, n44 and n44.value)


if __name__ == '__main__':
    main()
