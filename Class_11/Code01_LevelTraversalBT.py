"""
二叉树的按层遍历
"""
from queue import Queue


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


def level(node: Node) -> None:
    """
    1、准备一个队列
    2、头节点放入队列
    3、从队列中弹出的时候放入当前节点的左右孩子
    4、依次重复上述操作
    """
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node, end=',')
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    level(root)


if __name__ == '__main__':
    main()
