"""
能不能不给单链表的头节点，只给想要删除的节点，就能做到在链表上把这个点删掉？
"""


class Node(object):
    value: int = None
    next = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'


def delete_target_node(head: Node, target: int) -> Node:
    cur = head
    head = pre = None
    while cur:
        next_node = cur.next
        cur.next = None
        if cur.value == target:
            cur = next_node
            continue
        if pre is None:
            head = pre = cur
        else:
            pre.next = cur
            pre = cur
        cur = next_node
    return head


def print_nodes(head: Node):
    while head:
        print(head.value, end=',')
        head = head.next
    print()


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next.next = Node(1)
    head = delete_target_node(head, 1)
    print_nodes(head)


if __name__ == '__main__':
    main()
