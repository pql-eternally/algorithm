"""
Prim（普里姆算法）
（1）输入：一个加权连通图，其中顶点集合为V，边集合为E；
（2）初始化：Vnew = {x}，其中x为集合V中的任一节点（起始点），Enew = {},为空；
（3）重复下列操作，直到Vnew = V：
a.在集合E中选取权值最小的边<u, v>，其中u为集合Vnew中的元素，而v不在Vnew集合当中，并且v∈V（如果存在有多条满足前述条件即具有相同权值的边，则可任意选取其中之一）；
b.将v加入集合Vnew中，将<u, v>边加入集合Enew中；
（4）输出：使用集合Vnew和Enew来描述所得到的最小生成树。

步骤：
1、解锁任意一个点
2、将当前点相连的边放入到小根堆中
3、选取权重最小到边，需要校验使用当前边后会不会构成环路，这样就解锁了新的点，同时解锁了新的点连接的边
4、继续从小根堆里面弹出权重小的边重复3步骤直到所有的点都解锁
"""
from typing import List, Dict, Set
from heapq import heapify, heappush, heappop
from graph import Node, Edge, Graph, GraphGenerator


def prim_mst(graph: Graph):
    visitor_nodes = set()
    min_edge_heap = []
    edges = []
    for node in graph.nodes.values():
        if node in visitor_nodes:
            continue
        visitor_nodes.add(node)
        for edge in node.edges:
            heappush(min_edge_heap, edge)
        while min_edge_heap:
            edge = heappop(min_edge_heap)
            if edge.from_node not in visitor_nodes:
                new_node = edge.from_node
            elif edge.to_node not in visitor_nodes:
                new_node = edge.to_node
            else:
                continue
            edges.append(edge)
            visitor_nodes.add(new_node)
            # 解锁当前点连接的所有边
            for edge in new_node.edges:
                heappush(min_edge_heap, edge)
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
    edges = prim_mst(graph)
    print_edges(edges)


if __name__ == '__main__':
    main()
