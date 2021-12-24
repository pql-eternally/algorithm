"""
在链表中删除指定值的所有节点
"""

import random
import copy


class Node(object):
    value = None
    next = None

    def __init__(self, value):
        self.value = value


def remove_value(head: Node, num: int) -> Node:
    head_node = None
    pre_node = None
    cur_node = head
    while cur_node:
        next_node = cur_node.next
        if cur_node.value == num:
            cur_node = next_node
            if pre_node:
                pre_node.next = None
            continue
        if head_node is None:
            head_node = cur_node
        if pre_node:
            pre_node.next = cur_node
        pre_node = cur_node
        cur_node = next_node
    return head_node


def remove_value2(head: Node, num: int) -> Node:
    # 分两步走
    # 1、如果头节点也是当前值，移动头节点
    while head:
        if head.value != num:
            break
        head = head.next

    # 2、移除非头节点
    cur_node = head
    pre_node = head
    while cur_node:
        next_node = cur_node.next
        if cur_node.value == num:
            pre_node.next = cur_node.next
        else:
            pre_node = cur_node
        cur_node = next_node
    return head


def random_generator_linked_list() -> Node:
    head = None
    pre_node = None
    max_count = random.randint(10, 20)
    max_value = random.randint(1, 10)
    for i in range(0, max_count):
        value = random.randint(0, max_value)
        node = Node(value)
        if head is None:
            head = node
        else:
            pre_node.next = node
        pre_node = node
    return head


def print_linked_list(head: Node) -> None:
    cur_node = head
    while cur_node:
        print(cur_node.value, end='->')
        cur_node = cur_node.next
    print()


def main() -> None:
    head = random_generator_linked_list()
    value = random.randint(1, 10)
    print(f'remove value is: {value}')
    print_linked_list(head)
    print('=' * 20)
    head1 = remove_value(copy.deepcopy(head), value)
    print_linked_list(head1)
    head2 = remove_value2(copy.deepcopy(head), value)
    print_linked_list(head2)


if __name__ == '__main__':
    main()
