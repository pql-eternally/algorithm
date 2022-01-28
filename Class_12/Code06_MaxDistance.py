"""
给定一棵二叉树的头节点head，任何两个节点之间都存在距离，返回整棵二叉树的最大距离

1、左子树的最大距离
2、右子树的最大距离
3、当前节点作为最大距离的节点
4、当前节点不作为最大距离的节点

class Info:
    height: int
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
    height: int
    max_distance: int

    def __init__(self, h: int, d: int):
        self.height = h
        self.max_distance = d


def process1(head: Node) -> Info:
    if head is None:
        return Info(0, 0)
    left_info = process1(head.left)
    right_info = process1(head.right)
    height = max(left_info.height, right_info.height) + 1
    max_distance = max(left_info.max_distance, right_info.max_distance, left_info.height + right_info.height + 1)
    return Info(height, max_distance)


def max_distance1(head: Node) -> int:
    return process1(head).max_distance


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
    test_count = 1
    for i in range(test_count):
        root = generate_random_binary_tree(max_level, max_value)
        size1 = max_distance1(root)
        print_tree(root)
        print(size1)


if __name__ == '__main__':
    main()
