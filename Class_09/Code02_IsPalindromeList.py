"""
给定一个单链表的头节点head，请判断该链表是否为回文结构
"""


class Node(object):
    value: int = 0
    next = None

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f'Node value: {self.value}'


def is_palindrome1(head: Node) -> bool:
    """
    使用栈实现，需要额外的空间复杂度N
    """
    cur = head
    stack = []
    while cur:
        stack.insert(0, cur)
        cur = cur.next

    while head:
        if head != stack.pop(0):
            return False
        head = head.next
    return True


def is_palindrome2(head: Node) -> bool:
    """
    使用栈实现，找到队列的上中点，将下半部分所有链表压入栈中，需要额外的空间复杂度N/2
    """
    if head is None or head.next is None:
        return True
    if head.next.next is None:
        return head.value == head.next.value

    # 求中点位置
    slow = head.next
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    stack = []
    # 慢指针现在在中点或者上中点位置
    cur = slow.next
    while cur:
        stack.insert(0, cur)
        cur = cur.next
    # 判断栈中和链表是否相等
    cur = head
    while stack:
        if stack.pop(0) != cur:
            return False
        cur = cur.next
    return True


def is_palindrome3(head: Node) -> bool:
    """
    使用栈实现，找到队列的上中点，反转下半部分链表，不使用额外的空间复杂度
    """
    if head is None or head.next is None:
        return True
    # 求中点位置
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next  # mid
        fast = fast.next.next  # end
    mid = slow

    # 反转下半部分链表
    pre = None
    cur = mid.next
    mid.next = None
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    end = pre

    # 判断链表是否一致
    flag = True
    start = head
    last = end
    while start and end:
        if start.value != end.value:
            flag = False
            break
        start = start.next
        end = end.next

    # 还原原链表
    pre = None
    cur = last
    while cur:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    mid.next = pre
    return flag


def print_nodes(head: Node):
    while head:
        print(head.value, end=',')
        head = head.next
    print()


def build_nodes(word):
    head = cur = None
    for w in word:
        if head is None:
            head = Node(w)
            cur = head
        else:
            cur.next = Node(w)
            cur = cur.next
    return head


def main():
    head = build_nodes('12321')
    res1 = is_palindrome1(head)
    res2 = is_palindrome2(head)
    res3 = is_palindrome3(head)
    print_nodes(head)
    assert res1 == res2 == res3 is True

    head = build_nodes('1')
    res1 = is_palindrome1(head)
    res2 = is_palindrome2(head)
    res3 = is_palindrome3(head)
    print_nodes(head)
    assert res1 == res2 == res3 is True

    head = build_nodes('12')
    res1 = is_palindrome1(head)
    res2 = is_palindrome2(head)
    res3 = is_palindrome3(head)
    print_nodes(head)
    assert res1 == res2 == res3 is False

    head = build_nodes('1221')
    res1 = is_palindrome1(head)
    res2 = is_palindrome2(head)
    res3 = is_palindrome3(head)
    print_nodes(head)
    assert res1 == res2 == res3 is True, (res1, res2, res3)


if __name__ == '__main__':
    main()
