"""
1）假设以X节点为头，假设可以向X左树和X右树要任何信息
2）在上一步的假设下，讨论以X为头节点的树，得到答案的可能性（最重要）
3）列出所有可能性后，确定到底需要向左树和右树要什么样的信息
4）把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S
5）递归函数都返回S，每一棵子树都这么要求
6）写代码，在代码中考虑如何把左树的信息和右树信息整合出整棵树的信息

判断是否是完全二叉树
1、左子树是完全二叉树
2、右子树是完全二叉树
3、只要有右子树一定有左子树
4、找到某个节点有叶子几点，那么后面所有的节点都是只有叶子节点
"""
import random
from queue import Queue
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


def is_cbt1(head: Node) -> bool:
    """
    按层遍历加是否叶子节点的标志
    """
    if not head:
        return True

    is_leaf = False
    queue = Queue()
    queue.put(head)
    while not queue.empty():
        node = queue.get()
        left_node = node.left
        right_node = node.right
        if left_node is None and right_node:
            return False
        if is_leaf and left_node:
            return False
        if not left_node or not right_node:
            is_leaf = True
        if left_node:
            queue.put(left_node)
        if right_node:
            queue.put(right_node)
    return True


class Info:
    is_cbt: bool
    is_full: bool
    height: int

    def __init__(self, full: bool, cbt: bool, h: int):
        self.is_full = full
        self.is_cbt = cbt
        self.height = h


def process(head: Node) -> Info:
    if not head:
        return Info(True, True, 0)
    left_info = process(head.left)
    right_info = process(head.right)
    height = max(left_info.height, right_info.height) + 1
    is_full = left_info.is_full and right_info.is_full and left_info.height == right_info.height
    is_cbt = False
    # 满二叉树是完全二叉树
    if is_full:
        is_cbt = True
    else:
        # 不是满二叉树：左右两个子树都是完全二叉树
        if left_info.is_cbt and right_info.is_cbt:
            # 左右子树是满二叉树，左子树比右子树高一层
            if left_info.is_full and right_info.is_full and (left_info.height == right_info.height + 1):
                is_cbt = True
            # 左子树不满，右子树满的，左子树比右子树高一层
            if not left_info.is_full and right_info.is_full and (left_info.height == right_info.height + 1):
                is_cbt = True
            # 左子树满，右子树不满，则高度差可能差1或者不差
            if left_info.is_full and not right_info.is_full and (0 <= left_info.height - right_info.height <= 1):
                is_cbt = True
    return Info(is_full, is_cbt, height)


def is_cbt2(head: Node) -> bool:
    return process(head).is_cbt


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
        res1 = is_cbt1(root)
        res2 = is_cbt2(root)
        print(res1, res2)
        assert res1 == res2, (print_tree(root), res1, res2)


if __name__ == '__main__':
    main()
