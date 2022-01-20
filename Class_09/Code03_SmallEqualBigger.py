"""
给定一个单链表的头节点head，给定一个整数n，将链表按n划分成左边<n、中间==n、右边>n
"""


class Node(object):
    value: int = 0
    next = None

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f'Node value: {self.value}'


def partition(head: Node, target: int) -> Node:
    """
    使用数组排序
    """
    arr = []
    cur = head
    while cur:
        arr.append(cur)
        cur = cur.next
    # 快排分组
    arr_partition(arr, target)
    # 连接链表，返回头节点
    head = arr.pop(0)
    cur = head
    while arr:
        node = arr.pop(0)
        node.next = None
        cur.next = node
        cur = cur.next
    print(head)
    return head


def arr_partition(arr: list, target: int) -> None:
    """
    按目标值对节点列表快排分组
    1、小于区域指针指向最左侧，大于区域指针指向最后一个数
    2、依次循环列表中节点
        1）当前节点数小于目标数，则将当前数和小于区域的指向的数交换，小于区域向右扩，跳下一个
        2）当前节点数等于目标数，直接跳下一个
        2）当前数节点大于目标数，则将当前数和大于区域的指向的数交换，大于区域先左扩（注意这里不能跳下一个因为当前数还未比较过）
    """
    mid_index = 0
    max_index = len(arr) - 1
    index = mid_index
    while index < max_index:
        value = arr[index].value
        if value < target:
            arr[mid_index], arr[index] = arr[index], arr[mid_index]
            mid_index += 1
            index += 1
        elif value == target:
            index += 1
        else:
            arr[index], arr[max_index] = arr[max_index], arr[index]
            max_index -= 1


def partition2(head: Node, target: int) -> Node:
    """
    使用指针来记录每个区域头尾节点位置
    """
    small_head = small_tail = equal_head = equal_tail = big_head = big_tail = None
    cur = head
    while cur:
        value = cur.value
        next_node = cur.next
        cur.next = None
        if value < target:
            if small_head is None:
                small_head = small_tail = cur
            else:
                small_tail.next = cur
                small_tail = cur
        elif value == target:
            if equal_head is None:
                equal_head = equal_tail = cur
            else:
                equal_tail.next = cur
                equal_tail = cur
        else:
            if big_head is None:
                big_head = big_tail = cur
            else:
                big_tail.next = cur
                big_tail = cur
        cur = next_node

    # 连接头尾指针
    if small_head:
        small_tail.next = equal_head
    if equal_head is None:
        equal_head = small_head
        equal_tail = small_tail
    if equal_head:
        equal_tail.next = big_head
    return small_head or equal_head or big_head


def print_nodes(head: Node):
    while head:
        print(head.value, end=',')
        head = head.next
    print()


def build_nodes(word):
    head = cur = None
    for w in word:
        w = int(w)
        if head is None:
            head = Node(w)
            cur = head
        else:
            cur.next = Node(w)
            cur = cur.next
    return head


def main():
    head = build_nodes('122423473245421')
    # head = partition(head, 4)
    head = partition2(head, 6)
    print_nodes(head)


if __name__ == '__main__':
    main()
