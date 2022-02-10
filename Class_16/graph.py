"""
图：一系列点 + 一系列边构成了图
"""
from typing import TypeVar, Generic, List, Dict

T = TypeVar('T')


class Node(Generic[T]):
    # 值
    value: T
    # 入度
    in_degree: int
    # 出度
    out_degree: int
    # 邻居节点
    neighbors: List
    # 节点连接的边
    edges: List

    def __init__(self, value: T):
        self.value = value
        self.in_degree = 0
        self.out_degree = 0
        self.neighbors = []
        self.edges = []

    def __str__(self):
        return f'Node-{self.value}'


class Edge:
    # 权重
    weight: int
    # 起点
    from_node: Node
    # 终点
    to_node: Node

    def __init__(self, w: int, f: Node, t: Node):
        self.weight = w
        self.from_node = f
        self.to_node = t

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'weight<{self.weight}> from {self.from_node} to {self.to_node}'


class Graph:
    # 点集
    nodes: Dict[int, Node]
    # 边集
    edges: List[Edge]

    def __init__(self):
        self.nodes = {}
        self.edges = []


class GraphGenerator:

    @staticmethod
    def create(matrix: List[List[int]]):
        """
        生成的是有向图
        matrix 所有的边
        N*3 的矩阵
        [weight, from节点上面的值，to节点上面的值]
        [ 5 , 0 , 7]
        """
        graph = Graph()
        for edge_info in matrix:
            # 节点加入到图中
            from_node_value = edge_info[1]
            if from_node_value not in graph.nodes:
                graph.nodes[from_node_value] = Node(from_node_value)
            to_node_value = edge_info[2]
            if to_node_value not in graph.nodes:
                graph.nodes[to_node_value] = Node(to_node_value)

            from_node = graph.nodes[from_node_value]
            to_node = graph.nodes[to_node_value]
            # 创建边
            weight = edge_info[0]
            edge = Edge(weight, from_node, to_node)
            # 设置节点的属性值
            from_node.out_degree += 1
            from_node.neighbors.append(to_node)
            from_node.edges.append(edge)
            to_node.in_degree += 1
            # 边加入到图中
            graph.edges.append(edge)
        return graph

    @staticmethod
    def create_undigraph(matrix: List[List[int]]):
        """
        生成带权重的无向图
        [weight, from节点上面的值，to节点上面的值]
        [ 5 , 0 , 7]
        """
        graph = Graph()
        for edge_info in matrix:
            weight, from_node_value, to_node_value = edge_info
            if from_node_value not in graph.nodes:
                graph.nodes[from_node_value] = Node(from_node_value)
            if to_node_value not in graph.nodes:
                graph.nodes[to_node_value] = Node(to_node_value)
            from_node = graph.nodes[from_node_value]
            to_node = graph.nodes[to_node_value]
            edge = Edge(weight, from_node, to_node)
            # 边加入到图中
            graph.edges.append(edge)
            # 设置点属性
            from_node.in_degree += 1
            from_node.out_degree += 1
            from_node.neighbors.append(to_node)
            from_node.edges.append(edge)
            to_node.in_degree += 1
            to_node.out_degree += 1
            to_node.neighbors.append(from_node)
            to_node.edges.append(edge)
        return graph
