"""
二叉树先序、中序、后序的非递归遍历
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


class Stack(object):
    data: list

    def __init__(self):
        self.data = []

    def push(self, node: BinaryTree):
        self.data.insert(0, node)

    def pop(self) -> BinaryTree:
        if self.is_empty():
            raise RuntimeError('empty')
        return self.data.pop(0)

    def peek(self) -> BinaryTree:
        if self.is_empty():
            raise RuntimeError('empty')
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0


def pre(node: BinaryTree) -> None:
    """
    先序遍历：根左右
    1、创建栈
    2、将根节点压入栈
    3、只要栈有数据，弹出栈顶节点
    4、节点右孩子压入栈
    5、节点左孩子压入栈
    """
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        node = stack.pop()
        print(node, end=',')
        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)


def mid(node: BinaryTree) -> None:
    """
    中序遍历：左根右
    """
    stack = Stack()
    cur = node
    while not stack.is_empty() or cur is not None:
        if cur:
            stack.push(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            print(cur, end=',')
            cur = cur.right


def last(node: BinaryTree) -> None:
    """
    后序遍历：左右根
    """
    stack = Stack()
    stack.push(node)
    while not stack.is_empty():
        cur = stack.peek()
        if cur.left and node != cur.left and node != cur.right:
            stack.push(cur.left)
        elif cur.right and node != cur.right:
            stack.push(cur.right)
        else:
            cur = stack.pop()
            print(cur, end=',')
            node = cur


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
