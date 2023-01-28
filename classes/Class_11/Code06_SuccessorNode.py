"""
求二叉树某个节点的后继节点
二叉树结构如下定义：
Class Node {
    V value;
    Node left;
    Node right;
    Node parent;
}
给你二叉树中的某个节点，返回该节点的后继节点

            1
        2       3
     4    5   6   7

1、如果节点有右子树，则该节点的后继节点就是往右子树出发，然后转到右子树的左子树，一直到左子树的左子树为空
（即输入节点的右子树的最左子树，例如节点1，后继节点就是6）
2、如果节点没有右子树，则向上寻找父节点，直到父节点的左子树等于当前节点，则该父节点就是后继节点
（如节点5，没有右子树，则向上找，这时到2这个节点，因为2的左子树不等于5，所以继续向上找，这时到节点1，1的左子树等于当前节点2，所以返回1）
"""


class Node(object):
    value: int

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f'{self.value}'


def successor_node(node: Node) -> Node or None:
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
    else:
        parent = node.parent
        while node != parent.left:
            node = parent
            parent = node.parent
        return parent


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.left = node2
    node1.right = node3
    node2.parent = node3.parent = node1

    node2.left = node4
    node2.right = node5
    node4.parent = node5.parent = node2

    node3.left = node6
    node3.right = node7
    node6.parent = node7.parent = node3

    node = successor_node(node1)
    print(node)
    node = successor_node(node5)
    print(node)


if __name__ == '__main__':
    main()
