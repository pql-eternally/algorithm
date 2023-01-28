"""
一种特殊的单链表节点类描述如下
class Node {
    int value;
    Node next;
    Node rand;
    Node(int val) { value = val; }
}
rand指针是单链表节点结构中新增的指针，rand可能指向链表中的任意一个节点，也可能指向null
给定一个由Node节点类型组成的无环单链表的头节点head，请实现一个函数完成这个链表的复制
返回复制的新链表的头节点，要求时间复杂度O(N)，额外空间复杂度O(1)
"""


class Node(object):
    value: int = 0
    next = None
    rand = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


def copy_linked_list1(head: Node):
    """
    建立字典映射，空间复杂度N
    """
    node_map = {}
    cur = head
    # 建立映射
    while cur:
        copy_node = Node(cur.value)
        node_map[cur] = copy_node
        cur = cur.next

    # 拷贝指向
    cur = head
    while cur:
        copy_node = node_map[cur]
        copy_node.next = node_map.get(cur.next)
        copy_node.rand = node_map.get(cur.rand)
        cur = cur.next
    return node_map[head]


def copy_linked_list2(head: Node) -> Node:
    """
    1、按next指针循环原链表，同时创建当前节点的复制节点放到原节点后面
    2、从头节点开始，每次跳过2个几点去设置next、rand指针
    """
    cur = head
    while cur:
        copy_node = Node(cur.value)
        next_node = cur.next
        cur.next = copy_node
        copy_node.next = next_node
        cur = next_node

    # 拷贝rand
    cur = head
    while cur:
        copy_cur = cur.next
        if cur.rand:
            copy_cur.rand = cur.rand.next
        cur = cur.next.next

    # 拆分原链表和拷贝链表
    cur = head
    copy_head = cur.next
    while cur:
        copy_cur = cur.next
        next_node = cur.next.next
        cur.next = next_node
        if next_node:
            copy_cur.next = next_node.next
        cur = next_node
    return copy_head


def print_nodes(head: Node):
    while head:
        print(head.value, head.next, head.rand)
        head = head.next


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node1.rand = node3
    node2.next = node3
    node2.rand = node1
    node3.rand = node3
    print_nodes(node1)
    copy_node = copy_linked_list1(node1)
    copy_node2 = copy_linked_list2(node1)
    print_nodes(copy_node)
    print_nodes(copy_node2)


if __name__ == '__main__':
    main()
