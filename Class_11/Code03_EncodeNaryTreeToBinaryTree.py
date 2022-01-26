"""
N叉树如何通过二叉树来序列化、并完成反序列化
Leetcode题目：https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
"""


class Node(object):
    value: int
    children: list = None

    def __init__(self, value: int, children: list = None):
        self.value = value
        self.children = children or []

    def __str__(self):
        return f'{self.value}, [{",".join(map(str, self.children))}]'


class TreeNode(object):
    value: int
    left: None
    right: None

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value},[{self.left},{self.right}]'


class Codec(object):
    def en(self, children: list) -> TreeNode:
        head = None
        cur = None
        for child in children:
            node = TreeNode(child.value)
            if head is None:
                head = node
            else:
                cur.right = node
            cur = node
            cur.left = self.en(child.children)
        return head

    def encode(self, root: Node) -> TreeNode:
        """
        1、N叉树的根节点为二叉树的根节点
        2、N叉树的第一个孩子节点作为父节点左节点，其余兄弟节点一次连接到长兄节点到右子树
        3、所有的子树都按上面的规则
        """
        tree_root = TreeNode(root.value)
        tree_root.left = self.en(root.children)
        return tree_root

    def de(self, node: TreeNode) -> list:
        children = []
        while node:
            cur = Node(node.value)
            cur.children = self.de(node.left)
            children.append(cur)
            node = node.right
        return children

    def decode(self, tree_root: TreeNode) -> Node:
        """
        二叉树解码N叉树
        """
        root = Node(tree_root.value)
        root.children = self.de(tree_root.left)
        return root


def main():
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    root.children = [node2, node3, node4]
    node2.children = [Node(5), Node(6), Node(7), Node(8)]
    node3.children = [Node(9), Node(10)]

    codec = Codec()
    tree_root = codec.encode(root)
    print(tree_root)
    node = codec.decode(tree_root)
    print(node)


if __name__ == '__main__':
    main()
