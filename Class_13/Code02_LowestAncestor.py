"""
给定一棵二叉树的头节点head，和另外两个节点a和b，返回a和b的最低公共祖先
1、a是否在子树中
2、b是否在子树中
3、
"""

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
    find_a: bool
    find_b: bool
    ancestor_node: Node

    def __init__(self, find_a: bool, find_b: bool, node: Node or None):
        self.find_a = find_a
        self.find_b = find_b
        self.ancestor_node = node


def process(node: Node, a: Node, b: Node):
    if node is None:
        return Info(False, False, None)
    left_info = process(node.left, a, b)
    right_info = process(node.right, a, b)
    find_a = left_info.find_a or right_info.find_a or node == a
    find_b = left_info.find_b or right_info.find_b or node == b
    ancestor_node = None
    if find_a and find_b:
        ancestor_node = left_info.ancestor_node or right_info.ancestor_node or node
    return Info(find_a, find_b, ancestor_node)


def get_lowest_ancestor(head: Node, a: Node, b: Node):
    return process(head, a, b).ancestor_node


def main():
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    print_tree(root)
    res = get_lowest_ancestor(root, node6, node2)
    print(res)


if __name__ == '__main__':
    main()
