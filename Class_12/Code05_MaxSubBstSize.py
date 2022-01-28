"""
给定一棵二叉树的头节点head，返回这颗二叉树中最大的二叉搜索子树的大小

1、左子树是否搜索二叉树
2、右子树是否搜索二叉树
3、二叉搜索树节点数
4、最大值
5、最小值
"""
import random
from Class_11.Code04_PrintBinaryTree import print_tree


class Node(object):
    left: None
    right: None
    value: int = None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value}'


class Info:
    # 最大子数节点数
    max_size: int
    # 所有节点数
    nodes: int
    max_value: int
    min_value: int

    def __init__(self, s: int, nodes: int, mi: int, ma: int):
        self.max_size = s
        self.nodes = nodes
        self.min_value = mi
        self.max_value = ma

    @property
    def is_bst(self):
        return self.max_size == self.nodes


def process(head: Node) -> Info or None:
    if head is None:
        return None

    left_info = process(head.left)
    right_info = process(head.right)
    is_bst = True
    max_value = head.value
    min_value = head.value
    nodes = 1
    left_max_size = 0
    right_max_size = 0
    if left_info:
        min_value = min(min_value, left_info.min_value)
        max_value = max(max_value, left_info.max_value)
        nodes += left_info.nodes
        left_max_size = left_info.max_size
        if left_info.is_bst is False:
            is_bst = False
        if left_info.max_value > head.value:
            is_bst = False
    if right_info:
        min_value = min(min_value, right_info.min_value)
        max_value = max(max_value, right_info.max_value)
        nodes += right_info.nodes
        right_max_size = right_info.max_size
        if right_info.is_bst is False:
            is_bst = False
        if right_info.min_value < head.value:
            is_bst = False

    # 当节点x不作为搜索二叉树的节点时
    if is_bst is False:
        max_size = max(left_max_size, right_max_size)
    else:
        max_size = left_max_size + right_max_size + 1
    return Info(max_size, nodes, min_value, max_value)


def max_sub_bst_size(head: Node) -> int:
    """
    1、左子树是否搜索二叉树
    2、右子树是否搜索二叉树
    3、二叉搜索树节点数
    4、最大值
    5、最小值
    """
    if head is None:
        return 0
    return process(head).max_size


def get_bst_size2(head: Node) -> int:
    if head is None:
        return 0
    arr = []
    mid_order2(head, arr)
    for index, num in enumerate(arr):
        if index == 0:
            continue
        if arr[index] < arr[index - 1]:
            return 0
    return len(arr)


def mid_order2(head: Node, arr: list) -> None:
    if head is None:
        return
    mid_order2(head.left, arr)
    arr.append(head.value)
    mid_order2(head.right, arr)


def max_sub_bst_size2(head: Node) -> int:
    if head is None:
        return 0
    h = get_bst_size2(head)
    if h > 0:
        return h
    return max(max_sub_bst_size2(head.left), max_sub_bst_size2(head.right))


def generate_random_binary_tree(max_level: int, max_value: int):
    return generate(1, max_level, max_value)


def generate(level: int, max_level: int, max_value) -> Node or None:
    if (level > max_level) or (random.random() < 0.2):
        return None
    head = Node(random.randint(0, max_value))
    head.left = generate(level + 1, max_level, max_value)
    head.right = generate(level + 1, max_level, max_value)
    return head


def main():
    max_level = 5
    max_value = 100
    test_count = 100000
    for i in range(test_count):
        root = generate_random_binary_tree(max_level, max_value)
        size1 = max_sub_bst_size(root)
        size2 = max_sub_bst_size2(root)
        print(size1, size2)
        assert size1 == size2, (print_tree(root), size1, size2)


if __name__ == '__main__':
    main()
