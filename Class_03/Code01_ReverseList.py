"""
反转单链表
反转双链表
"""
import random


class Node(object):
    value = None
    next = None

    def __init__(self, value):
        self.value = value


class DoubleNode(object):
    value = None
    pre = None
    next = None

    def __init__(self, value):
        self.value = value


def reverse_linked_list(head: Node) -> Node:
    pre_node = None
    cur_node = head
    while cur_node:
        next_node = cur_node.next
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
    # 注意：上个节点记录了尾节点
    return pre_node


def reverse_double_linked_list(head: DoubleNode) -> DoubleNode:
    pre_node = None
    cur_node = head
    while cur_node:
        next_node = cur_node.next
        # 切记一次循环中到了那个节点只管当前节点该干的事
        cur_node.pre = next_node
        cur_node.next = pre_node
        pre_node = cur_node
        cur_node = next_node
    return pre_node


def print_linked_list(head: Node) -> None:
    cur_node = head
    while cur_node:
        print(cur_node.value, end='->')
        cur_node = cur_node.next
    print()


def print_double_linked_list(head: DoubleNode, backward: bool = True) -> None:
    cur_node = head
    while cur_node:
        print(cur_node.value, end='->')
        if backward:
            cur_node = cur_node.next
        else:
            cur_node = cur_node.pre
    print()


def random_generator_linked_list() -> Node:
    head = None
    pre_node = None
    max_count = random.randint(1, 10)
    max_value = random.randint(1, 100)
    for i in range(0, max_count):
        value = random.randint(0, max_value)
        node = Node(value)
        if head is None:
            head = node
        else:
            pre_node.next = node
        pre_node = node
    return head


def random_generator_double_linked_list() -> tuple:
    head = None
    pre_node = None
    max_count = random.randint(1, 10)
    max_value = random.randint(1, 100)
    for i in range(0, max_count):
        value = random.randint(0, max_value)
        node = DoubleNode(value)
        if head is None:
            head = node
        else:
            pre_node.next = node
            node.pre = pre_node
        pre_node = node
    return head, pre_node


def main():
    # 测试单链表反转
    head = random_generator_linked_list()
    print_linked_list(head)
    res = reverse_linked_list(head)
    print_linked_list(res)
    print('=' * 20)

    # 测试反转双链表
    head, tail = random_generator_double_linked_list()
    print_double_linked_list(head)
    # print_double_linked_list(tail, backward=False)

    res = reverse_double_linked_list(head)
    print_double_linked_list(res)


if __name__ == '__main__':
    main()
