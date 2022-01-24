"""
二叉树先序、中序、后序的递归遍历和递归序
"""


class BinaryTree(object):
    left: None
    right: None
    value: int = None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value}'


def pre(node) -> None:
    """
    先序遍历：根左右
    """
    if node is None:
        return
    print(node, end=',')
    pre(node.left)
    pre(node.right)


def mid(node) -> None:
    """
    中序遍历：左根右
    """
    if node is None:
        return
    mid(node.left)
    print(node, end=',')
    mid(node.right)


def last(node) -> None:
    """
    后序遍历：左右根
    """
    if node is None:
        return
    last(node.left)
    last(node.right)
    print(node, end=',')


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    pre(root)
    print()
    mid(root)
    print()
    last(root)


if __name__ == '__main__':
    main()
