"""
1）假设以X节点为头，假设可以向X左树和X右树要任何信息
2）在上一步的假设下，讨论以X为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S
5）递归函数都返回S，每一棵子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树信息整合出整棵树的信息

判断是否是搜索二叉树
1、左子树是搜索二叉树
2、右子树是搜索二叉树
3、左子树的最大值小于根节点值
4、右子树的最小值大于根节点值

class Info:
    is_bst: bool
    min_value: int
    max_value: int

对数器：二叉树的先序遍历是递增
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
    min_value: int
    max_value: int

    def __init__(self, s: bool, mi: int, ma: int):
        self.is_bst = s
        self.min_value = mi
        self.max_value = ma


def process(head: Node) -> Info or None:
    if not head:
        return None

    is_bst = True
    min_value = head.value
    max_value = head.value
    left_info = process(head.left)
    right_info = process(head.right)
    if left_info:
        min_value = min(min_value, left_info.min_value)
        max_value = max(max_value, left_info.max_value)
        if left_info.is_bst is False:
            is_bst = False
        if left_info.max_value > head.value:
            is_bst = False
    if right_info:
        min_value = min(min_value, right_info.min_value)
        max_value = max(max_value, right_info.max_value)
        if right_info.is_bst is False:
            is_bst = False
        if right_info.min_value < head.value:
            is_bst = False
    return Info(is_bst, min_value, max_value)


def is_bst1(head: Node) -> bool:
    if not head:
        return True
    return process(head).is_bst


def mid_order(head: Node, res: list) -> None:
    if not head:
        return
    mid_order(head.left, res)
    res.append(head.value)
    mid_order(head.right, res)


def is_bst2(head: Node) -> bool:
    if not head:
        return True
    res = []
    mid_order(head, res)
    for index, num in enumerate(res):
        if index == 0:
            continue
        if res[index - 1] > res[index]:
            return False
    return True


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
