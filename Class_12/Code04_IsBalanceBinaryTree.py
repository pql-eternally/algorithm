"""
1）假设以X节点为头，假设可以向X左树和X右树要任何信息
2）在上一步的假设下，讨论以X为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S
5）递归函数都返回S，每一棵子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树信息整合出整棵树的信息

判断是否是平衡二叉树
1、左子树是平衡二叉树
2、右子树是平衡二叉树
3、左右子树的高度差绝对值不能大于1

class Info
    is_balance: bool
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
    is_balance: bool
    height: int

    def __init__(self, b: bool, h: int):
        self.is_balance = b
        self.height = h


def process1(head: Node) -> Info:
    if head is None:
        return Info(True, 0)
    left_info = process1(head.left)
    right_info = process1(head.right)
    height = max(left_info.height, right_info.height) + 1
    # 左右子树都是平衡二叉树
    is_balance = left_info.is_balance and right_info.is_balance
    if is_balance is True:
        # 两棵树的高度差大于1
        if abs(left_info.height - right_info.height) > 1:
            is_balance = False
    return Info(is_balance, height)


def is_bst1(head: Node) -> bool:
    """
    判断是否是平衡二叉树
        1、左子树是平衡二叉树
        2、右子树是平衡二叉树
        3、左右子树的高度差绝对值不能大于1
    """
    return process1(head).is_balance


def process2(head: Node, ans: list) -> int:
    if ans[0] is False or head is None:
        return -1
    left_height = process2(head.left, ans)
    right_height = process2(head.right, ans)
    if abs(left_height - right_height) > 1:
        ans[0] = False
    return max(left_height, right_height) + 1


def is_bst2(head: Node) -> bool:
    ans = [True]
    process2(head, ans)
    return ans[0]


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
    test_count = 100000
    for i in range(test_count):
        root = generate_random_binary_tree(max_level, max_value)
        res1 = is_bst1(root)
        res2 = is_bst2(root)
        assert res1 == res2, (print_tree(root), res1, res2)


if __name__ == '__main__':
    main()
