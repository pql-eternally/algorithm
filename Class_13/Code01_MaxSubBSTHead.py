"""
给定一棵二叉树的头节点head，返回这颗二叉树中最大的二叉搜索子树的头节点

1、左子树是否是二叉搜索树
2、右子树是否是二叉搜索树
3、二叉搜索树的节点数
4、当前最大的二叉搜索节点数以及节点
5、最大值、最小值
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
    is_bst: bool
    cur_nodes: int = 0
    max_sub_bst_nodes: int = 0
    max_sub_bst_head: Node
    min_value: int
    max_value: int

    def __init__(self, is_bst: bool, cur_nodes: int, max_nodes: int, bst_head: Node or None, min_value: int,
                 max_value: int):
        self.is_bst = is_bst
        self.cur_nodes = cur_nodes
        self.max_sub_bst_nodes = max_nodes
        self.max_sub_bst_head = bst_head
        self.min_value = min_value
        self.max_value = max_value


def process(node: Node) -> Info or None:
    if node is None:
        return None

    is_bst = True
    cur_nodes = 1
    sub_bst_nodes = 0
    sub_bst_head = None
    min_value = node.value
    max_value = node.value
    left_info = process(node.left)
    right_info = process(node.right)
    if left_info:
        min_value = min(min_value, left_info.min_value)
        max_value = max(max_value, left_info.max_value)
        cur_nodes += left_info.cur_nodes
        if left_info.is_bst is False or left_info.max_value > node.value:
            is_bst = False
            sub_bst_nodes = left_info.max_sub_bst_nodes
            sub_bst_head = left_info.max_sub_bst_head
    if right_info:
        min_value = min(min_value, right_info.min_value)
        max_value = max(max_value, right_info.max_value)
        cur_nodes += right_info.cur_nodes
        if right_info.is_bst is False or right_info.min_value < node.value:
            is_bst = False
            if right_info.max_sub_bst_nodes > sub_bst_nodes:
                sub_bst_nodes = right_info.max_sub_bst_nodes
                sub_bst_head = right_info.max_sub_bst_head
    if is_bst:
        sub_bst_nodes = cur_nodes
        sub_bst_head = node
    return Info(is_bst, cur_nodes, sub_bst_nodes, sub_bst_head, min_value, max_value)


def max_sub_bst_head(head: Node):
    info = process(head)
    if info is None:
        return None
    return info.max_sub_bst_head


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
    max_level = 2
    max_value = 100
    test_count = 1
    for i in range(test_count):
        root = generate_random_binary_tree(max_level, max_value)
        head = max_sub_bst_head(root)
        print_tree(root)
        print('最大子数头节点：', head)


if __name__ == '__main__':
    main()
