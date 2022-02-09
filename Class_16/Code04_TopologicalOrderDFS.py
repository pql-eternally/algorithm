"""
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.

lintcode链接：https://www.lintcode.com/problem/127/description
"""


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __str__(self):
        return f'{self.label}'


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    # FIXME：深度优先遍历，这里为什么没通过？？？
    def topSort(self, graph):
        # 计算图中节点的入度值，用来寻找开始节点
        in_degree_map = {node: 0 for node in graph}
        for cur in graph:
            for node in cur.neighbors:
                in_degree_map[node] += 1
        # 记录访问过的节点
        visitor_nodes = set()
        stack = []
        for node, in_degree in in_degree_map.items():
            if in_degree == 0:
                stack.append(node)
        res = []
        while stack:
            cur = stack.pop()
            # 当前节点有没有访问过
            if cur not in visitor_nodes:
                visitor_nodes.add(cur)
                res.append(cur)
            # 将当前节点的邻居节点加入到待访问列表中
            for node in cur.neighbors:
                if node not in visitor_nodes:
                    stack.append(cur)
                    stack.append(node)
                    break
        return res


def main():
    node0 = DirectedGraphNode(0)
    node1 = DirectedGraphNode(1)
    node2 = DirectedGraphNode(2)
    node3 = DirectedGraphNode(3)
    node4 = DirectedGraphNode(4)
    node3.neighbors = [node4]
    node2.neighbors = [node1, node4]
    node1.neighbors = [node3, node4]
    node0.neighbors = [node1, node2, node3, node4]
    graph = [node0, node1, node2, node3, node4]
    s = Solution()
    res = s.topSort(graph)
    for node in res:
        print(node)


if __name__ == '__main__':
    main()
