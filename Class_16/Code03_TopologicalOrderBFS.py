"""
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.
"""


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # 初始化节点入度
        in_degree_map = {}
        for node in graph:
            in_degree_map[node] = 0
        # 设置节点入度值
        for node in graph:
            for cur in node.neighbors:
                in_degree_map[cur] += 1
        # 筛选入度值为0的节点
        zero_nodes = []
        for node, in_degree in in_degree_map.items():
            if in_degree == 0:
                zero_nodes.append(node)
        # 遍历入度值为0的节点
        res = []
        while zero_nodes:
            node = zero_nodes.pop(0)
            res.append(node)
            for cur in node.neighbors:
                in_degree = in_degree_map[cur] - 1
                in_degree_map[cur] = in_degree
                if in_degree == 0:
                    zero_nodes.append(cur)
        return res
