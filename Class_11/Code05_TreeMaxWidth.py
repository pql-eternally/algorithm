"""
求二叉树的最大宽度
"""
from queue import Queue


class BinaryTree(object):
    value: int
    left: None
    right: None

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def max_width_with_map(root: BinaryTree) -> int:
    """
    1、二叉树的按层遍历
    2、使用map记录每个节点所在的层数
    3、计算每层节点数
    4、统计出最多节点数
    """
    if not root:
        return 0
    queue = Queue()
    queue.put(root)
    level_map = {root: 1}
    cur_level = 1
    cur_level_nodes = 0
    max_width = 0
    while not queue.empty():
        cur = queue.get()
        cur_node_level = level_map.get(cur)
        if cur.left:
            queue.put(cur.left)
            level_map[cur.left] = cur_node_level + 1
        if cur.right:
            queue.put(cur.right)
            level_map[cur.right] = cur_node_level + 1
        if cur_node_level == cur_level:
            cur_level_nodes += 1
        else:
            max_width = max(max_width, cur_level_nodes)
            cur_level += 1
            cur_level_nodes = 1
    max_width = max(max_width, cur_level_nodes)
    return max_width


def max_width_no_map(root: BinaryTree) -> int:
    """
    1、二叉树的按层遍历
    2、使用两个遍历记录当前层的结束节点和下一层的结束节点
    3、根据当前节点是否是当前层的结束节点来统计每层的节点数
    4、统计出最多节点数
    """
    if not root:
        return 0
    queue = Queue()
    queue.put(root)
    cur_end = root
    next_end = None
    cur_level_nodes = 0
    max_width = 0
    while not queue.empty():
        cur = queue.get()
        if cur.left:
            queue.put(cur.left)
            next_end = cur.left
        if cur.right:
            queue.put(cur.right)
            next_end = cur.right
        cur_level_nodes += 1
        if cur == cur_end:
            max_width = max(max_width, cur_level_nodes)
            cur_level_nodes = 0
            cur_end = next_end
    return max_width


def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    res = max_width_with_map(root)
    print(res)
    res = max_width_no_map(root)
    print(res)


if __name__ == '__main__':
    main()
