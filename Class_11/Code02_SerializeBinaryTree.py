"""
二叉树的序列化和反序列化
1、先序遍历
2、后序遍历
3、中序遍历，不可以序列化，因为不同的两棵树，可能得到同样的中序序列，即便补了空位置也可能一样。
     *         __2
     *        /
     *       1
     中序遍历：#, 1, #, 2, #

     *       1__
     *          \
     *           2
     中序遍历：#, 1, #, 2, #
4、按层遍历
"""
from queue import Queue

NONE_STR = '#'


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


################################################
#                先序遍历编码解码                #
################################################
def pre_dump(node: BinaryTree, res: list) -> None:
    if node is None:
        res.append(NONE_STR)
    else:
        res.append(node.value)
        pre_dump(node.left, res)
        pre_dump(node.right, res)


def pre_dumps(node: BinaryTree) -> str:
    """
    使用先序遍历序列化二叉树
    1、需要记录每个节点的左右子节点
    """
    res = []
    pre_dump(node, res)
    res = ','.join(map(str, res))
    return res


def pre_load(values) -> BinaryTree or None:
    value = values.pop(0)
    if value == NONE_STR:
        return None
    head = BinaryTree(int(value))
    head.left = pre_load(values)
    head.right = pre_load(values)
    return head


def pre_loads(values: list) -> BinaryTree or None:
    if not values:
        return None
    return pre_load(values)


################################################
#                后序遍历编码解码                #
################################################
def last_dump(node: BinaryTree, res: list) -> None:
    if not node:
        res.append(NONE_STR)
    else:
        last_dump(node.left, res)
        last_dump(node.right, res)
        res.append(node.value)


def last_dumps(node: BinaryTree) -> str:
    res = []
    last_dump(node, res)
    return ','.join(map(str, res))


def last_load(stack: Stack) -> BinaryTree or None:
    value = stack.pop()
    if value == NONE_STR:
        return None
    # 左右根  使用栈  根右左
    head = BinaryTree(value)
    head.right = last_load(stack)
    head.left = last_load(stack)
    return head


def last_loads(values: list) -> BinaryTree or None:
    if not values:
        return None
    stack = Stack()
    while values:
        stack.push(values.pop(0))
    return last_load(stack)


################################################
#                按层遍历编码解码                #
################################################
def level_dumps(node: BinaryTree) -> str:
    res = []
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        if not node:
            res.append(NONE_STR)
        else:
            res.append(node.value)
            queue.put(node.left)
            queue.put(node.right)
    return ','.join(map(str, res))


def generate_node(value: str) -> BinaryTree or None:
    if value == NONE_STR:
        return None
    return BinaryTree(value)


def level_loads(values: list) -> BinaryTree or None:
    if not values:
        return None
    queue = Queue()
    head = generate_node(values.pop(0))
    queue.put(head)
    while not queue.empty():
        node = queue.get()
        node.left = generate_node(values.pop(0))
        node.right = generate_node(values.pop(0))
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    return head


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    # res = pre_dumps(root)
    # print(res)
    # values = res.split(',')
    # head = pre_loads(values)
    # print(pre_dumps(head))
    # assert pre_dumps(head) == res, pre_dumps(head)

    # res = last_dumps(root)
    # print(res)
    # root = last_loads(res.split(','))
    # print(last_dumps(root))
    # assert last_dumps(root) == res, last_dumps(root)

    res = level_dumps(root)
    print(res)
    root = level_loads(res.split(','))
    print(level_dumps(root))
    assert level_dumps(root) == res, level_dumps(root)


if __name__ == '__main__':
    main()
