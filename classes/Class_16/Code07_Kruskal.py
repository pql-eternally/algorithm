"""
带权无向图
最小生成树算法Kruskal（克鲁斯卡尔算法）
（1）尽可能选取权值小的边，但不能构成回路；
（2）选取n－1条恰当的边以连通n个顶点；

思路：
1、使用并查集
2、将图中所有的点集初始化到并查集中，parent为自己，size为1
3、使边集按照边的权重生成小根堆
4、从小根堆中弹出一条边，看会不会连成环，会舍掉当前边
5、不会连成边就使用并查集连接两个点
4、直到所有的边都弹出
"""
from typing import List, Dict
from heapq import heapify, heappush, heappop
from graph import Node, Edge, Graph, GraphGenerator


class UnionFound:
    parents: Dict[Node, Node]
    sizes: Dict[Node, int]

    def __init__(self, nodes):
        self.parents = {}
        self.sizes = {}
        for node in nodes:
            self.parents[node] = node
            self.sizes[node] = 1

    def find(self, node):
        cur = node
        stack = []
        while cur != self.parents[cur]:
            stack.append(cur)
            cur = self.parents[cur]
        while stack:
            node = stack.pop()
            self.parents[node] = cur
        return cur

    def union(self, node1, node2):
        node1_parent = self.find(node1)
        node2_parent = self.find(node2)
        if node1_parent != node2_parent:
            node1_size = self.sizes[node1]
            node2_size = self.sizes[node2]
            if node1_size < node2_size:
                self.parents[node1_parent] = node2_parent
                self.sizes[node2_parent] = node1_size + node2_size
                self.sizes[node1_parent] = 0
            else:
                self.parents[node2_parent] = node1_parent
                self.sizes[node1_parent] = node1_size + node2_size
                self.sizes[node2_parent] = 0

    def is_same_set(self, node1, node2):
        node1_parent = self.find(node1)
        node2_parent = self.find(node2)
        return node1_parent == node2_parent


def kruskal_mst(graph: Graph) -> List[Edge]:
    """
    最小生成树边集
    """
    edges = []
    union_find = UnionFound(graph.nodes.values())
    # 构建小根堆
    min_heap = []
    for edge in graph.edges:
        heappush(min_heap, edge)
    while min_heap:
        edge = heappop(min_heap)
        node1, node2 = edge.from_node, edge.to_node
        # 加入当前边能否构成环路
        if not union_find.is_same_set(node1, node2):
            union_find.union(node1, node2)
            edges.append(edge)
    return edges


def print_edges(edges: List[Edge]):
    for edge in edges:
        print(edge)


def main():
    matrix = [
        [1, 1, 6],
        [6, 1, 2],
        [5, 1, 5],
        [3, 2, 3],
        [5, 2, 6],
        [5, 5, 6],
        [6, 3, 4],
        [6, 3, 6],
        [4, 4, 6],
        [2, 4, 5]
    ]
    graph = GraphGenerator.create_undigraph(matrix)
    edges = kruskal_mst(graph)
    print_edges(edges)


if __name__ == '__main__':
    main()
