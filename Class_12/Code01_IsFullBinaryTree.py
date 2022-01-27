"""
1）假设以X节点为头，假设可以向X左树和X右树要任何信息
2）在上一步的假设下，讨论以X为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S
5）递归函数都返回S，每一棵子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树信息整合出整棵树的信息

判断是否是满二叉树
1、左子树是满二叉树
2、右子树是满二叉树
3、左子树高度等于右子树的高度
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
    is_full: bool
    height: int

    def __init__(self, b: bool, h: int):
        self.is_full = b
        self.height = h


def process(head: Node) -> Info:
    if not head:
        return Info(True, 0)

    left_info = process(head.left)
    right_info = process(head.right)
    height = max(left_info.height, right_info.height) + 1
    is_full = left_info.is_full and right_info.is_full
    if is_full:
        is_full = left_info.height == right_info.height
    return Info(is_full, height)


def is_full_binary_tree(root: Node) -> bool:
    """
    判断是否是满二叉树
    """
    if not root:
        return True
    return process(root).is_full


class Info2:
    nodes: int
    height: int

    def __init__(self, nodes: int, h: int):
        self.nodes = nodes
        self.height = h


def process2(head: Node):
    if not head:
        return Info2(0, 0)
    left_info = process2(head.left)
    right_info = process2(head.right)
    nodes = left_info.nodes + right_info.nodes + 1
    height = max(left_info.height, right_info.height) + 1
    return Info2(nodes, height)


def is_full_binary_tree2(root: Node) -> bool:
    """
    统计每层节点树来判断是否是满二叉树
    1层 2^0
    2层 2^1
    3层 2^2
    """
    if not root:
        return True
    info = process2(root)
    return info.nodes == (2 ** info.height - 1)


def generate_random_binary_tree(max_level: int, max_value: int):
    return generate(1, max_level, max_value)


def generate(level: int, max_level: int, max_value) -> Node or None:
    if (level > max_level) or (random.random() < 0.5):
        return None
    head = Node(random.randint(0, max_value))
    head.left = generate(level + 1, max_level, max_value)
    head.right = generate(level + 1, max_level, max_value)
    return head


def main():
    max_level = 5
    max_value = 100
    test_count = 10000
    for i in range(test_count):
        root = generate_random_binary_tree(max_level, max_value)
        res1 = is_full_binary_tree(root)
        res2 = is_full_binary_tree2(root)
        print(res1, res2)
        assert res1 == res2, (print_tree(root), res1, res2)


if __name__ == '__main__':
    main()
