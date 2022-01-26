"""
打印二叉树的函数设计
"""


class BinaryTree(object):
    value: int
    left: None
    right: None

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def get_space(num: int):
    space = ' '
    return space * num


def print_mid_order(head: BinaryTree, height: int, to: str, length: int):
    if head is None:
        return
    print_mid_order(head.right, height + 1, 'v', length)
    value = f'{to}{head.value}{to}'
    m = len(value)
    l = int((length - m) / 2)
    r = length - m - l
    value = get_space(l) + value + get_space(r)
    print(get_space(height * length) + value)
    print_mid_order(head.left, height + 1, '^', length)


def print_tree(head: BinaryTree):
    print('Binary Tree:')
    print_mid_order(head, 0, 'H', 17)
    print()


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print_tree(root)


if __name__ == '__main__':
    main()
